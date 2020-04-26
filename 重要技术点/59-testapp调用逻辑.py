import os
from functools import partial

import grpc
import json
from flask import Blueprint, render_template, request
import traceback
from apptest.call_invoker import CallInvoker
from common import Common
from grpc_all import service_pb2_grpc, service_pb2
from kafka_tool.kafka_tool import KafkaUtility
from logger import Logger
from start import getIP

Common.AREA = Common.get_config('AREA', 'area')  # 地域配置
kafka_server_ip = Common.get_config('SERVER_%s' % Common.AREA.upper(), 'kafka_server_ip')  # 从配置文件中根据地域获取kafka-ip
kafka_server_port = int(Common.get_config('SERVER_%s' % Common.AREA.upper(), 'kafka_server_port'))  # 从配置文件中根据地域获取kafka-port
Logger.kafka = KafkaUtility(kafka_server_ip, kafka_server_port)
callobj = CallInvoker()

testblue = Blueprint("testblue", __name__)


@testblue.route('/')
def index():
    return render_template("index.html")


# 使用grpc通讯的方式调用app中的方法
# @testblue.route('/invoke', methods=['POST'])
# def invoke():
#     # 调用app中的方法
#     app_name = request.form.get("appName", type=str, default=None)
#     route = request.form.get("appRoute", type=str, default=None)
#     method_name = request.form.get("funcName", type=str, default=None)
#     paramsstr = request.form.get("params", type=str, default=None)
#     try:
#         # 建立grpc客户端连接，发送grpc请求
#         conn = grpc.insecure_channel(getIP() + ":9999")
#         stub = service_pb2_grpc.CallInvokerStub(conn)
#         response = stub.call(service_pb2.CallRequest(app_name=app_name, method=method_name, parameters=paramsstr, route=route))
#         success = f"success:{response.success}\n"
#         message = f"message:{response.message}\n"
#         data = f"data:{response.data}\n"
#         result = f"result:{response.result}\n"
#         resultstr = success + message + data + result
#         print(resultstr)
#         return resultstr
#     except Exception as e:
#         print(f"'repr(e):\t'{repr(e)}")
#         Logger.log_error(traceback.format_exc())
#         traceback.print_exc()
#         return traceback.format_exc()

# 直接本地调用call方法调用app中的方法
@testblue.route('/invoke', methods=['POST'])
def invoke():
    # 调用app中的方法
    print("调用了app方法")
    app_name = request.form.get("appName", type=str, default=None)
    route = request.form.get("appRoute", type=str, default=None)
    method_name = request.form.get("funcName", type=str, default=None)
    paramsstr = request.form.get("params", type=str, default=None)
    try:
        params = eval(paramsstr)
        app = callobj.apps[app_name]
        if hasattr(app, "call"):
            Logger.log_caution("Invoker get method success [{0}].".format(method_name))
            method_call = getattr(app, "call")
            new_func = partial(method_call, method_name, params, route)
            call_result2 = new_func()
            success = f"success:{call_result2.success}\n"
            message = f"message:{call_result2.message}\n"
            data = f"data:{call_result2.data}\n"
            result = f"result:{call_result2.result}\n"
            resultstr = success + message + data + result
            return resultstr
    except Exception as e:
        print(f"'repr(e):\t'{repr(e)}")
        Logger.log_error(traceback.format_exc())
        traceback.print_exc()
        return traceback.format_exc()
