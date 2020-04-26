from common import Common
from logger import Logger
from visa_manager.visa_manager import VisaManager
from app.ue_controller import UeController
from app.communication_adaptor import CommunicationAdaptor
from tcp.Tcp import TcpClient
from call_result import CallResult
from functools import partial
from abc import abstractmethod
import os
import sys
import inspect


# APP基础类，管理APP中的可用资源
class App(object):

    def __init__(self):
        # 用户资源
        self.io_resource = {}
        # 日志打印模块
        self.logger = Logger()
        # STOP标志
        self.stop_flag = False
        # App名称，在继承类中设置
        self.name = ""
        # App支持的业务名称，在继承类中设置
        self.business_type = ""
        # AW库
        self.aw_libs = {}
        # 前置过滤器
        self.pre_call_filter = []
        # 后置过滤器
        self.post_call_filter = []
        # UE控制器
        self.ue_controller = None
        # 通讯适配器
        self.communication_adaptor = None

    def get_name(self):
        return self.name

    def get_business_type(self):
        return self.business_type

    def get_info(self):
        return "名称:{0}; 业务种类:{1};".format(self.name, self.business_type)

    def stop(self):
        Logger.log('用户停止标志已设置')
        self.stop_flag = True
        # self.device.stop = True

    def add_aw_lib(self, route_path, aw_lib):
        self.aw_libs[route_path] = aw_lib

    def open_instrument(self, params):
        result = CallResult()
        instrument_addr = params["instrument_addr"]
        instrument_addr = "10.121.20.163"
        if not self.device.open(instrument_addr):
            result.message = "仪表打开失败:" + instrument_addr
            result.success = False
            return result
        else:
            self.device.stop = False
            result.success = True
            return result

    def get_comm_port(self, type, address, port=None):
        """
        返回指定类型的通讯端口
        :param type:
        :param address:
        :param port:
        :return:
        """
        comm_obj = None
        if type == "visa":
            comm_obj = VisaManager()
            comm_obj.addr = address
            self.io_resource[address] = (comm_obj)
        if type == "tcpip":
            comm_obj = TcpClient()
            comm_obj.addr = address
            self.io_resource[address] = (comm_obj, port)
        if type == "telnet":
            comm_obj = TcpClient()
            self.io_resource[address] = (comm_obj, port)
        return comm_obj

    def call(self, method, params, route):
        Logger.log_caution('++++++++++++++++%s' % params)
        route = params['route']  # "nrsa/siso"
        params["testitem"] = method
        result = CallResult()
        if method == 'reset':
            return self.reset(params)
        elif method == 'stop':
            return self.stop()
        else:
            test_boj = None
            method_dict = None
            if route in self.aw_libs:
                test_boj = self.aw_libs[route]
                method_dict = test_boj.get_method_dict()
            else:
                Logger.log_error("不支持的模块:%s" % route)
                result.success = False
                result.message = "不支持的模块:%s" % route
                return result

            if method in method_dict:
                method = method_dict[method]

            if hasattr(test_boj, method):
                Logger.log(self.name + " 获取方法成功 [{0}].".format(method))
                filter_res_list = []
                for pre_call in self.pre_call_filter:
                    filter_res, params = pre_call.run(params, self)
                    filter_res_list.append(filter_res)
                method = getattr(test_boj, method)
                try:
                    call_result = ""
                    if all(filter_res_list):
                        new_func = partial(method, params)
                        call_result = new_func()
                    for post_call in self.post_call_filter:
                        call_result = post_call.run(params, call_result, self)
                    result.result = call_result
                    result.success = True
                    return call_result
                except Exception as e:
                    Logger.log_caution('{"error":%s}' % str(e))
                    result.message = "Exception: %s %s" % (type(e), e.args[0])
                    result.success = False
                    return result
            else:
                Logger.log_error("method not find [{0}].".format(method))
                Logger.log_error("method must in {0}".format(tuple(dir(test_boj))))

    def reset(self, params):
        print("--->", self.aw_libs)
        for aw_lib_key in self.aw_libs:
            result = self.aw_libs[aw_lib_key].reset_action(params)
            if not result.success:
                return CallResult.Error("组件初始化失败")
        return CallResult.Success()

    def find_instrument(self, params, instrument_type):
        # 从界面上获取测试环境信息
        for device_info in params['instrument']:
            if device_info['type'] == instrument_type:
                return (device_info['addr'])
        return None

    def pre_call_handler(self):
        pass

    def post_call_handler(self):
        pass

    @staticmethod
    def recursive_dir(path, f, file_list):
        fileNames = os.listdir(os.path.join(path, f))  # 获取当前路径下的文件名，返回List
        for file in fileNames:
            newDir = path + '/' + f + '/' + file  # 将文件命加入到当前文件路径后面
            if os.path.isfile(newDir):  # 如果是文件
                if "pycache" not in f and "pycache" not in file:
                    file_list.append("%s.%s" % (f, file))
            else:
                App.recursive_dir("/".join(newDir.split("/")[0:-1]), newDir.split("/")[-1],
                                  file_list)  # 如果不是文件，递归这个文件夹的路径

    @staticmethod
    def get_recursive_dir_files(path, f):
        file_list = []
        App.recursive_dir(path, f, file_list)
        return file_list

    @staticmethod
    def load_modules_from_path(path, class_type, init_params=None):
        """
        Import all modules from the given directory
        """
        # Check and fix the path
        if path[-1:] != '/':
            path += '/'
        # Get a list of files in the directory, if the directory exists
        if not os.path.exists(path):
            raise OSError("Directory does not exist: %s" % path)
        app_dict = {}
        # Add path to the system path
        sys.path.append(path)
        # Load all the files in path
        for f in os.listdir(path):
            # f is a file or a directory, directory is not considered
            file_list = []
            file_list.append(f)
            if os.path.isdir(os.path.join(path, f)) and "pycache" not in os.path.join(path, f):
                file_list.clear()
                file_list += App.get_recursive_dir_files(path, f)  # 获得所有的文件
            for file in file_list:
                # Ignore anything that isn't a .py file
                if len(file) > 3 and (file[-3:] == '.py' or file[-4:] == '.pyc'):
                    module_name = ''
                    if file[-3:] == '.py':
                        module_name = file[:-3]
                    if file[-4:] == '.pyc':
                        module_name = file[:-4]
                    # Import the module
                    __import__(module_name, globals(), locals(), [], 0)
                    module = sys.modules[module_name]
                    module_attrs = dir(module)
                    for name in module_attrs:
                        var_obj = getattr(module, name)
                        if inspect.isclass(var_obj):
                            if issubclass(var_obj, class_type) and var_obj.__name__ != class_type.__name__:
                                if app_dict.get(name) is None:
                                    if init_params is None:
                                        app_dict[name] = var_obj()
                                    else:
                                        app_dict[name] = var_obj(init_params)
                                    Logger.log("注入 %s 模块 %s 成功" % (class_type.__name__, var_obj.__name__))
        return app_dict

    # 安装AwProvider
    def mount_aw_provider(self, path):
        aw_module_dict = App.load_modules_from_path(path, AwProvider, self)
        for aw_module_name in aw_module_dict:
            aw_module = aw_module_dict[aw_module_name]
            self.add_aw_lib(aw_module.get_route_path(), aw_module)
            Logger.log("%s 安装 AwProvider [%s] 成功，路由 [%s]" % (path, aw_module_name, aw_module.get_route_path()))

    # 安装前置过滤器
    def mount_pre_filter(self, path):
        aw_module_dict = App.load_modules_from_path(path, PreCallFilter)
        for aw_module_name in aw_module_dict:
            aw_module = aw_module_dict[aw_module_name]
            self.pre_call_filter.append(aw_module)
            Logger.log("%s 安装 PreCallFilter [%s] 成功" % (path, aw_module_name))

    # 安装后置过滤器
    def mount_post_filter(self, path):
        aw_module_dict = App.load_modules_from_path(path, PostCallFilter)
        for aw_module_name in aw_module_dict:
            aw_module = aw_module_dict[aw_module_name]
            self.post_call_filter.append(aw_module)
            Logger.log(" %s 安装 PostCallFilter [%s] 成功" % (path, aw_module_name))

    # 安装UE控制器
    def mount_ue_controller(self, path):
        ue_controller_dict = App.load_modules_from_path(path, UeController)
        user_ue_controller = Common.get_config('SERVER_%s' % Common.AREA.upper(), 'ue_controller_name')
        for ue_controller_name in ue_controller_dict:
            ue_controller = ue_controller_dict[ue_controller_name]
            self.ue_controller = ue_controller
            if user_ue_controller and ue_controller_name == user_ue_controller:
                break
            Logger.log(" %s 安装 UE控制器 [%s] 成功 " % (path, ue_controller_name))

    # 安装UE通讯适配器
    def mount_communication_adaptor(self, path):
        adaptor_dict = App.load_modules_from_path(path, CommunicationAdaptor)
        for adaptor_name in adaptor_dict:
            adaptor = adaptor_dict[adaptor_name]
            if self.ue_controller is not None:
                self.communication_adaptor = adaptor
                self.ue_controller.set_communication_adaptor(adaptor)
                Logger.log(" %s 安装 通讯适配器 [%s] 成功" % (path, adaptor_name))


# AW函数包。用于扩展仪表测试功能
class AwProvider:

    def __init__(self):
        self.initialization = False
        self.route_path = ""

    def reset_action(self, params):
        try:
            result = self.reset(params)
            return result
        except Exception as e:
            Logger.log_caution(e)
            result.message = self.__class__.__name__ + " Exception: %s %s" % (type(e), e.args[0])
            result.success = False
            return result

    def get_method_dict(self):
        return self.method_dict

    def get_route_path(self):
        return self.route_path

    @abstractmethod
    def reset(self, params):
        '''please Implement in subclass'''
        result = CallResult()
        result.success = True
        return result


# 调用前过滤器
class PreCallFilter:

    def run(self, params):
        return params


# 调用后过滤器
class PostCallFilter:

    def run(self, params, result):
        return result


# AwProvider的配置类，AwProvider被初始化时被系统调用
class AwProviderConfiguration:

    def __init__(self, aw_provider_name, logger):
        self.aw_provider_name = aw_provider_name
        self.logger = logger

    def config(self, params):
        return True
