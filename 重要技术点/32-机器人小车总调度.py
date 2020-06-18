import time
from app.app import AwProvider
from app.charging_master.charg_tcp import ChargClient
from app.charging_master.robot_tcp import RobotClient
from call_result import CallResult
from common import Common
from common.Common import get_config
from logger import Logger


class ChargRobat(AwProvider):
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, app=""):
        """
        自动充电流程总调度机器人
        """
        super().__init__()
        self.app = app
        # AW包用到的仪表设备，可以有多个
        self.device = None
        # AW包的路由
        self.route_path = "charge_robot/charging"
        Logger.kafka = None
        Logger.log("自动充电机器人总调度")
        self.result = None
        # 创建小车对象
        self.seer = None
        # 创建机械臂对象
        self.aubo = None
        # 创建充电桩对象
        self.power = None
        # 创建暗室门机械门
        self.door = None

        # 创建总调度客户端套接字
        self.charge_socket = ChargClient()
        charge_ip_port = get_config("ROBOT", "CHARGE_PLATFORM")
        self.charge_ip = charge_ip_port.split(":")[0]
        self.charge_port = int(charge_ip_port.split(":")[1])
        self.charge_socket.connect(self.charge_ip, self.charge_port)
        # 配置机械臂服务端通讯
        self.arm_socket = RobotClient()
        arm_ip_port = get_config("ROBOT", "ARM_SERVER")
        self.arm_ip = arm_ip_port.split(":")[0]
        self.arm_port = int(arm_ip_port.split(":")[1])
        self.arm_socket.connect(self.arm_ip, self.arm_port)

    def back_approach_sequence(self):
        Logger.log("从暗室抓手机图像识别出错，开始回退...")
        # 机械臂移动到最后一次位置
        point3 = [97.50574519472937, 50.05251757754012, -37.54022915019665, 95.50226629605704, 92.62892182544857,
                  1.8424947550297146]
        self.aubo.mvc_byj(point3)
        self.seer.seer_move_translate(0.215, 0.02, 0)
        # 机械臂从暗室抓取手机安全位置调度点
        point_into6 = [91.491104, 52.504063, -37.296215, 90.32386, 87.184875, 1.8391324]
        point_into5 = [113.3051270469386, 35.98150484951887, -62.043935778778426, 95.49638550318166, 92.62534963651265,
                       1.8424947550297146]
        point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
        point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
        point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
        point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
        Logger.log("收回机械臂...")
        # 机械臂伸出
        self.aubo.mvc_byj(point_into6, vel=6)
        self.seer.seer_move_translate(0.710, 0.02, 0)
        self.aubo.mvc_byj(point_into5, vel=6)
        self.aubo.mvc_byj(point_into4, vel=6)
        self.aubo.mvc_byj(point_into3, vel=6)
        self.aubo.mvc_byj(point_into2, vel=6)
        self.aubo.mvc_byj(point_into1, vel=6)
        # 收回后小车前往指定空旷位置
        self.seer.seer_move_to_locatin("LM22")
        # 然后再重新回到初始点
        self.seer.seer_move_to_locatin("LM25")

    def back_place_sequence(self):
        Logger.log("放手机进暗室图像识别出错，开始回退...")
        point3 = [99.35160381792531, 54.94131768353055, -21.268165764023987, 106.8159419014279, 94.64816480072528,
                  2.053077597990847]
        self.aubo.mvc_byj(point3)
        self.seer.seer_move_translate(0.205, 0.01, 0)
        point2 = [99.42222114375407, 53.06078218991845, -28.516898681091366, 101.44839676103835, 94.71962223982196,
                  2.057911450932512]
        self.aubo.mvc_byj(point2)
        self.seer.seer_move_translate(0.100, 0.01, 0)
        # 机械臂从暗室抓取手机安全位置调度点
        point_into6 = [91.491104, 52.504063, -37.296215, 90.32386, 87.184875, 1.8391324]
        point_into5 = [113.3051270469386, 35.98150484951887, -62.043935778778426, 95.49638550318166, 92.62534963651265,
                       1.8424947550297146]
        point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
        point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
        point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
        point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
        Logger.log("收回机械臂...")
        # 机械臂伸出
        self.aubo.mvc_byj(point_into6, vel=6)
        self.seer.seer_move_translate(0.690, 0.02, 0)
        self.aubo.mvc_byj(point_into5, vel=6)
        self.aubo.mvc_byj(point_into4, vel=6)
        self.aubo.mvc_byj(point_into3, vel=6)
        self.aubo.mvc_byj(point_into2, vel=6)
        self.aubo.mvc_byj(point_into1, vel=6)
        # 收回后小车前往指定空旷位置
        self.seer.seer_move_to_locatin("LM22")
        # 然后再重新回到初始点
        self.seer.seer_move_to_locatin("LM25")

    def auto_approach_sequence(self, params=""):
        if self.seer.status == "free":
            Logger.log("从暗室里抓取手机调度流程")
            self.seer.Lock()
            # 将暗室的门打开
            self.door.open_door()
            print(self.aubo.get_joint())
            # 机械臂从暗室抓取手机安全位置调度点
            point_into6 = [91.491104, 52.504063, -37.296215, 90.32386, 87.184875, 1.8391324]
            point_into5 = [113.3051270469386, 35.98150484951887, -62.043935778778426, 95.49638550318166, 92.62534963651265, 1.8424947550297146]
            point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
            point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
            point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
            point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
            # 收回后小车前往指定空旷位置
            self.seer.seer_move_to_locatin("LM22")
            # 然后再重新回到初始点
            self.seer.seer_move_to_locatin("LM25")

            print("前往初始点...")
            Logger.log("机械臂前往初始点...")
            # 机械臂伸出
            self.aubo.mvc_byj(point_into1, vel=10)
            self.aubo.mvc_byj(point_into2, vel=10)
            self.aubo.mvc_byj(point_into3, vel=10)
            self.aubo.mvc_byj(point_into4, vel=10)
            self.aubo.mvc_byj(point_into5, vel=10)
            self.aubo.mvc_byj(point_into6, vel=10)
            self.seer.seer_move_translate(0.710, -0.02, 0)

            # 机械臂移动到最后一次位置
            point3 = [95.90115617377495, 49.06538448774403, -39.72216381640849, 94.30433990809601, 91.0258012951657, 1.7550672664364937]
            self.aubo.mvc_byj(point3)
            self.seer.seer_move_translate(0.215, -0.02, 0)
            Logger.log("发送消息71")
            self.arm_socket.send_bin(b'71')
            self.arm_socket.wait_message(b'71', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            # 判断接收到的消息是不是错误码171
            if "171" in status_code:
                Logger.log(f"等待回复71出错,收到的内容是:{status_code}")
                self.back_approach_sequence()
                self.seer.unLock()
                raise Exception(f"等待回复71出错,收到的内容是:{status_code}")
            Logger.log("发送消息72")
            self.arm_socket.send_bin(b'72')
            self.arm_socket.wait_message(b'72', 300)
            status_code = self.arm_socket.read().decode("utf-8")
            # 判断接收到的消息是不是错误码72
            if "72" not in status_code:
                Logger.log("重新发送消息72")
                self.arm_socket.send_bin(b'72')
                self.arm_socket.wait_message(b'72', 300)
                status_code = self.arm_socket.read().decode("utf-8")
                # 判断接收到的消息是不是错误码72
                if "72" not in status_code:
                    Logger.log(f"等待回复72出错,收到的内容是:{status_code}")
                    self.back_approach_sequence()
                    self.seer.unLock()
                    raise Exception(f"等待回复72出错,收到的内容是:{status_code}")
            Logger.log("发送消息74")
            self.arm_socket.send_bin(b'74')
            self.arm_socket.wait_message(b'74', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            # 判断接收到的消息是不是错误码74
            if "74" not in status_code:
                self.seer.unLock()
                Logger.log(f"等待回复74出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复74出错,收到的内容是:{status_code}")

            # 旋转1.5度
            point_into6 = self.aubo.get_joint()
            print(point_into6)
            point_into6[4] = point_into6[4] + 3
            print(point_into6)
            self.aubo.mvc_byj(point_into6)
            # 改变第四个轴坐标
            point_into6 = self.aubo.get_joint()
            print(point_into6)
            point_into6[3] = 93.30933394257168
            print(point_into6)
            self.aubo.mvc_byj(point_into6)
            # 发送消息接收激光测距
            Logger.log("发送消息80")
            self.arm_socket.send_bin(b'80')
            self.arm_socket.wait_message(b'.', 120)
            distance = self.arm_socket.read().decode("utf-8")
            if "." not in distance:
                self.seer.unLock()
                Logger.log(f"等待回复80距离出错,收到的内容是:{distance}")
                raise Exception(f"等待回复80距离出错,收到的内容是:{distance}")
            move_dist = (int(float(distance)) - 136) / 1000
            self.seer.seer_move_translate(move_dist, -0.01, 0)
            time.sleep(2)
            Logger.log("发送消息76")
            self.arm_socket.send_bin(b'76')
            self.arm_socket.wait_message(b'76', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "76" not in status_code:
                self.seer.unLock()
                Logger.log(f"等待回复76出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复76出错,收到的内容是:{status_code}")

            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")

            # 抓完手机后，退出序列
            print("夹持手机后退出...")
            Logger.log("夹持手机后退出...")
            # 抬起手机
            pos1 = self.aubo.get_joint()
            pos1[2] = pos1[2] + 3.672
            Logger.log(f"抬起手机，抬起位置{pos1}")
            self.aubo.mvc_byj(pos1, vel=0.1)
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")

            # 旋转90度
            pos2 = self.aubo.get_joint()
            pos2[5] = pos2[5] - 90
            Logger.log(f"旋转90度，旋转位置{pos2}")
            self.aubo.mvc_byj(pos2, vel=5)
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")

            # 小车向外移动23cm，
            self.seer.seer_move_translate(0.100, 0.02, 0)
            # 降低手机高度
            pos3 = self.aubo.get_joint()
            pos3[1] = pos3[1] + 2
            pos3[0] = pos3[0] - 2
            Logger.log(f"降低手机高度，降低位置{pos3}")
            self.aubo.mvc_byj(pos3)
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")

            # 小车向外移动150
            self.seer.seer_move_translate(0.240, 0.04, 0)

            # 降低手机高度
            pos4 = self.aubo.get_joint()
            pos4[1] = pos4[1] + 4
            pos4[0] = pos4[0] - 2
            Logger.log(f"降低手机高度，降低位置{pos4}")
            self.aubo.mvc_byj(pos4)
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")
            # 开始推出小车
            self.seer.seer_move_translate(0.850, 0.04, 0)

            # 收回机械臂
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")
            point_into6 = [91.491104, 52.504063, -37.296215, 90.32386, 87.184875, 1.8391324]
            point_into5 = [113.30512, 35.98150, -62.04393, 95.49638, 92.62534, 1.84249]
            point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
            point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
            point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
            point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
            self.aubo.mvc_byj(point_into6, vel=6)
            self.aubo.mvc_byj(point_into5, vel=6)
            self.aubo.mvc_byj(point_into4, vel=6)
            self.aubo.mvc_byj(point_into3, vel=6)
            self.aubo.mvc_byj(point_into2, vel=6)
            self.aubo.mvc_byj(point_into1, vel=6)
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                self.seer.unLock()
                Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复75出错,收到的内容是:{status_code}")
            # 将手机送到指定位置，开始充电
            # self.auto_charging_phone(params)
            # 返回执行结果
            call_result = CallResult()
            call_result.message = "夹持手机后退出成功执行!"
            call_result.success = True
            call_result.result = "成功！"
            self.seer.unLock()
            return call_result
        else:
            self.seer.unLock()
            Logger.log("小车繁忙，从暗室取手机出错!")
            raise Exception("小车繁忙，从暗室取手机出错!")

    def auto_place_sequence(self, params=""):
        Logger.log("放置手机进暗室...")
        if self.seer.status == "free":
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "175" == status_code:
                # 说明有手机，不能去取手机
                self.seer.unLock()
                Logger.log(f"等待回复175出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复175出错,收到的内容是:{status_code}")
            self.seer.Lock()
            self.door.open_door()
            print(self.aubo.get_joint())

            # 最后一次
            point_into6 = [91.491104, 52.504063, -37.296215, 90.32386, 87.184875, 1.8391324]
            point_into5 = [113.30512, 35.98150, -62.04393, 95.49638, 92.62534, 1.84249]
            point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
            point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
            point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
            point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]

            # 收回后小车前往指定空旷位置
            self.seer.seer_move_to_locatin("LM22")
            # 然后再重新回到初始点
            self.seer.seer_move_to_locatin("LM25")

            print("前往初始点...")
            Logger.log("机械臂前往初始点...")
            # 机械臂伸出
            self.aubo.mvc_byj(point_into1, vel=6)
            self.aubo.mvc_byj(point_into2, vel=6)
            self.aubo.mvc_byj(point_into3, vel=6)
            self.aubo.mvc_byj(point_into4, vel=6)
            self.aubo.mvc_byj(point_into5, vel=6)
            self.aubo.mvc_byj(point_into6, vel=6)

            self.seer.seer_move_translate(0.690, -0.02, 0)

            print(self.aubo.get_joint())

            point2 = [99.42222114375407, 53.06078218991845, -28.516898681091366, 101.44839676103835, 94.71962223982196, 2.057911450932512]
            self.aubo.mvc_byj(point2)
            self.seer.seer_move_translate(0.100, -0.01, 0)

            print(self.aubo.get_joint())
            point3 = [99.35160381792531, 54.94131768353055, -21.268165764023987, 106.8159419014279, 94.64816480072528, 2.053077597990847]
            self.aubo.mvc_byj(point3)
            self.seer.seer_move_translate(0.205, -0.01, 0)
            Logger.log("发送消息71")
            self.arm_socket.send_bin(b'71')
            self.arm_socket.wait_message(b'71', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if status_code == "171":
                Logger.log(f"等待回复71出错,收到的内容是:{status_code}")
                self.back_place_sequence()
                self.seer.unLock()
                raise Exception(f"等待回复71出错,收到的内容是:{status_code}")
            Logger.log("发送消息77")
            # 进行图像识别
            self.arm_socket.send_bin(b'77')
            self.arm_socket.wait_message(b'77', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "77" not in status_code:
                # 如果不在的话,重新发送77
                Logger.log("发送消息77")
                # 进行图像识别
                self.arm_socket.send_bin(b'77')
                self.arm_socket.wait_message(b'77', 120)
                status_code = self.arm_socket.read().decode("utf-8")
                if "77" not in status_code:
                    self.seer.unLock()
                    Logger.log(f"等待回复77出错,收到的内容是:{status_code}")
                    raise Exception(f"等待回复77出错,收到的内容是:{status_code}")
            Logger.log("发送消息80")
            self.arm_socket.send_bin(b'80')
            self.arm_socket.wait_message(b'.', 120)
            distance = self.arm_socket.read().decode("utf-8")
            if "." not in distance:
                self.arm_socket.send_bin(b'80')
                self.arm_socket.wait_message(b'.', 120)
                distance = self.arm_socket.read().decode("utf-8")
                if "." not in distance:
                    self.seer.unLock()
                    Logger.log(f"等待回复80距离出错,收到的内容是:{distance}")
                    raise Exception(f"等待回复80距离出错,收到的内容是:{distance}")
            move_dist = (277 - int(float(distance))) / 1000
            self.seer.seer_move_translate(move_dist, 0.01, 0)

            Logger.log("发送消息81")
            self.arm_socket.send_bin(b'81')
            self.arm_socket.wait_message(b'81', 180)
            status_code = self.arm_socket.read().decode("utf-8")
            if "81" not in status_code:
                self.seer.unLock()
                Logger.log(f"等待回复81出错,没有等到距离，收到的内容是:{status_code}")
                raise Exception(f"等待回复81出错,没有等到距离，收到的内容是:{status_code}")
            # 放完手机后退出
            self.seer.seer_move_translate(0.150, 0.01, 0)
            # 降低机械臂高度，判断获取到的位置是否为0
            pos4 = self.aubo.get_joint()
            pos4[1] = pos4[1] + 3
            pos4[0] = pos4[0] - 3
            Logger.log(f"降低手机高度，降低位置{pos4}")
            self.aubo.mvc_byj(pos4)

            self.seer.seer_move_translate(0.200, 0.03, 0)
            # 降低手机高度
            pos4 = self.aubo.get_joint()
            pos4[1] = pos4[1] + 2
            pos4[0] = pos4[0] - 2
            Logger.log(f"降低手机高度，降低位置{pos4}")
            self.aubo.mvc_byj(pos4)

            self.seer.seer_move_translate(0.730, 0.04, 0)
            # 收回机械臂
            self.aubo.mvc_byj(point_into5, vel=10)
            self.aubo.mvc_byj(point_into4, vel=10)
            self.aubo.mvc_byj(point_into3, vel=10)
            self.aubo.mvc_byj(point_into2, vel=10)
            self.aubo.mvc_byj(point_into1, vel=10)
            # 关门
            self.door.close_door()
            # # 让小车去充电
            # self.seer.move_to_power()

            # 返回执行结果
            call_result = CallResult()
            call_result.message = "放置手机进暗室成功执行!"
            call_result.success = True
            call_result.result = "成功！"
            self.seer.unLock()
            return call_result
        else:
            Logger.log("小车繁忙，放手机进暗室出错!...")
            raise Exception("小车繁忙，放手机进暗室出错!...")

    def auto_charging_phone(self, params=None):
        if self.seer.status == "free":
            Logger.log("去给手机充电流程")
            self.seer.Lock()
            # 查询空闲充电台坐标点
            free_point = self.power.get_free_point()
            # 将充电台坐标和小车坐标、放手机命令、充电命令形成对应关系，防止小车位置和充电台位置对照出错，
            """
            下面取放手机的指令是给1.20,50000发的：
            放手机到充电台是：11/12/13/14/15,例如发送11，表示放在1号位
            
            开始充电和停止充电指令是给1.5,60000发的：
            self.power.power_point(1)表示开始给1号位充电
            """
            point = params.get("point")
            # 1: ["AP5", 11, 1]表示到1号充电台，小车走到AP5点，发送11指令放手机到1号位，1表示让充电台开始给1号位充电
            # route_point = {1: ["AP5", "11", 1], 2: ["AP5", "12", 2], 3: ["AP4", "13", 3], 4: ["AP4", "14", 4], 5: ["AP5", "15", 5]}
            route_point = {1: ["AP5", "11", 1], 2: ["AP5", "12", 2], 3: ["AP4", "13", 3], 4: ["AP4", "14", 4],
                           5: ["AP5", "15", 5]}
            if free_point:
                if point in free_point and point in route_point.keys():
                    # print(f"执行放手机到{point}充电位开始充电序列")
                    Logger.log(f"执行放手机到{point}充电位开始充电序列")
                    sequence_list = route_point[point]
                    seer_target = sequence_list[0]
                    place_cmd = sequence_list[1]
                    charging_point = sequence_list[2]
                    self.seer.seer_move_to_locatin(seer_target)
                    self.arm_socket.send(place_cmd)
                    self.arm_socket.wait_message(bytes(place_cmd, encoding='utf-8'), 300)
                    statu = self.arm_socket.read().decode("utf-8")
                    if place_cmd not in statu:
                        self.seer.unLock()
                        Logger.log(f"等待消息{place_cmd}出错，程序停止")
                        raise Exception(f"等待消息{place_cmd}出错，程序停止")
                    self.power.power_point(charging_point)
                    call_result = CallResult()
                    call_result.message = f"放手机到{point}充电位开始充电成功执行!"
                    call_result.success = True
                    call_result.data = {"powering_point": point}
                    call_result.result = "充电成功！"
                    self.seer.unLock()
                    return call_result
                else:
                    self.seer.unLock()
                    Logger.log(f"充电台坐标非法，{point}号充电台繁忙或坐标越界...")
                    raise Exception(f"充电台坐标非法，{point}号充电台空闲或坐标越界...")
            else:
                self.seer.unLock()
                Logger.log("没有空闲充电台...")
                raise Exception("没有空闲充电台...")
        else:
            Logger.log("小车繁忙，流程失败...")
            raise Exception("小车繁忙，流程失败...")

    def auto_patch_phone(self, params={}):
        Logger.log("从充电台获取手机流程")
        if self.seer.status == "free":
            # 发送75检测是否抓到手机，75有手机，175没手机
            Logger.log("发送消息75")
            self.arm_socket.send_bin(b'75')
            self.arm_socket.wait_message(b'75', 120)
            status_code = self.arm_socket.read().decode("utf-8")
            if "75" == status_code:
                # 说明有手机，不能去取手机
                self.seer.unLock()
                Logger.log(f"等待回复175出错,收到的内容是:{status_code}")
                raise Exception(f"等待回复175出错,收到的内容是:{status_code}")
            self.seer.Lock()
            # 查询空闲充电台坐标点
            working_point = self.power.get_working_point()
            point = params.get("point")
            # 将充电台坐标和小车坐标、放手机命令、充电命令形成对应关系，防止小车位置和充电台位置对照出错，
            """
            下面取放手机的指令是给1.20,50000发的：
            从充电台取手机是：1/2/3/4/5,例如发送1，表示从一号位开始取手机
    
            开始充电和停止充电指令是给1.5,60000发的：
             self.power.grab_point(1)表示停止1号位充电并拔出手机
            """
            # 1: ["AP5", 11, 1]表示到1号充电台，小车走到AP5点，发送11指令放手机到1号位，1表示让充电台开始给1号位充电
            route_point = {1: ["AP5", "1", 1], 2: ["AP5", "2", 2], 3: ["AP4", "3", 3], 4: ["AP4", "4", 4],
                           5: ["AP5", "5", 5]}
            if working_point:
                # 判断要抓取的坐标是否合法
                if point is None:
                    point = working_point[0]
                if point in working_point and point in route_point.keys():
                    # print(f"执行取{point}充电位手机序列")
                    Logger.log(f"执行取{point}充电位手机序列")
                    sequence_list = route_point[point]
                    seer_target = sequence_list[0]
                    patch_cmd = sequence_list[1]
                    charging_point = sequence_list[2]
                    self.power.grab_point(charging_point)
                    self.seer.seer_move_to_locatin(seer_target)
                    self.arm_socket.send(patch_cmd)
                    self.arm_socket.wait_message(bytes(patch_cmd, encoding='utf-8'), 300)
                    statu = self.arm_socket.read().decode("utf-8")
                    if patch_cmd not in statu:
                        Logger.log(f"等待消息{patch_cmd}出错，程序停止")
                        raise Exception(f"等待消息{patch_cmd}出错，程序停止")
                    # 发送75检测是否抓到手机，75有手机，175没手机
                    Logger.log("发送消息75")
                    self.arm_socket.send_bin(b'75')
                    self.arm_socket.wait_message(b'75', 120)
                    status_code = self.arm_socket.read().decode("utf-8")
                    if "175" == status_code:
                        self.seer.unLock()
                        Logger.log(f"等待回复75出错,收到的内容是:{status_code}")
                        raise Exception(f"等待回复75出错,收到的内容是:{status_code}")
                    call_result = CallResult()
                    call_result.message = "拔出手机并抓取成功!"
                    call_result.success = True
                    call_result.data = {"patch_point": point}
                    call_result.result = "顺利通过测试！"
                    self.seer.unLock()
                    return call_result
                else:
                    self.seer.unLock()
                    Logger.log(f"充电台坐标非法，{point}号充电台空闲或坐标越界...")
                    raise Exception(f"充电台坐标非法，{point}号充电台空闲或坐标越界...")
            else:
                self.seer.unLock()
                Logger.log("没有工作中的充电台，拔出手机流程出错...")
                raise Exception("没有工作中的充电台，拔出手机流程出错...")
        else:
            Logger.log("小车繁忙，流程出错...")
            raise Exception("小车繁忙，流程出错...")

    def reset(self, params=""):
        Logger.log("总调度加载依赖APP：小车、机械臂、充电桩、机械门...")
        # 从框架加载小车对象
        self.seer = Common.APPS['SeerAgent'].aw_libs["aubo_robot/agv"]
        Logger.log("总调度加载依赖<小车>完成！")
        # 从框架加载机械臂对象
        self.aubo = Common.APPS['RobotAgent'].aw_libs["aubo_robot/aubo"]
        Logger.log("总调度加载依赖<机械臂>完成！")
        # 从框架加载充电桩对象
        self.power = Common.APPS['PowerAgent'].aw_libs["power_pile/power"]
        self.power.set_charg_socket(self.charge_socket)
        Logger.log("总调度加载依赖<充电桩>完成！")
        # 从框架加载暗室机械门对象
        self.door = Common.APPS['DoorAgent'].aw_libs["an_door/door"]
        self.door.set_charg_socket(self.charge_socket)
        Logger.log("总调度加载依赖<机械门>完成！")
        call_result = CallResult()
        call_result.message = "加载依赖APP完成!"
        call_result.success = True
        call_result.result = "顺利加载依赖！"
        return call_result

    def replay(self):
        # 收回机械臂
        point_into5 = [113.30512, 35.98150, -62.04393, 95.49638, 92.62534, 1.84249]
        point_into4 = [97.67766, 49.42056, 30.00275, 6.27188, 95.76539, 109.079185]
        point_into3 = [97.67451, 64.07729, 111.62077, 6.2695684, 95.76749, 109.08108]
        point_into2 = [101.88953, 57.124275, 97.308205, 21.119442, 89.73919, 87.82146]
        point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
        self.aubo.mvc_byj(point_into5, vel=10)
        self.aubo.mvc_byj(point_into4, vel=10)
        self.aubo.mvc_byj(point_into3, vel=10)
        self.aubo.mvc_byj(point_into2, vel=10)
        self.aubo.mvc_byj(point_into1, vel=10)

    def check_robot_is_safe_position(self):
        point_into1 = [95.746056, 4.4022746, 110.66593, 1.335793, 98.49435, 98.72721]
        point_into2 = self.aubo.get_joint()
        for i in range(6):
            if abs(point_into1[i]-point_into2[i]) > 1:
                # print("机械臂不在安全位置范围内")
                Logger.log("机械臂不在安全位置范围内")
                raise Exception("机械臂不在安全位置范围内")
        return True


if __name__ == '__main__':
    charg = ChargRobat()
    from app.agv_robot.seer_robot import SeerRobo
    from app.door_robot.an_door import Door
    from app.power_pile.power_pile import PowerPile
    from app.aubo_robot.aubomotion import AuboControl

    # 创建小车对象
    charg.seer = SeerRobo()
    # 创建机械臂对象
    charg.aubo = AuboControl()
    # 创建充电桩对象
    charg.power = PowerPile()
    # 创建暗室机械门对象
    charg.door = Door()
    # 给充电桩和暗室赋值通讯对象
    charg.power.set_charg_socket(charg.charge_socket)
    charg.door.set_charg_socket(charg.charge_socket)

    # 从暗室抓手机流程
    # charg.auto_approach_sequence()

    # 小车移动到对应位置去给手机充电流程
    charg.auto_charging_phone({"point": 1})

    # time.sleep(5)
    # 充电台停止充电并抓取手机流程
    # charg.auto_patch_phone()

    # 放手机进暗室流程
    # charg.auto_place_sequence()

    # 收回机械臂
    # charg.replay()

