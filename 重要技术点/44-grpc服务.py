# 重要点：定义请求和返回的消息的时候，要加上位置参数赋值，不然会报错！

定义的协议：
// 定义语法版本
syntax = "proto3";

// 定义服务
service Test{
    rpc SayHello(HelloRequest) returns (HelloReply) {}
}

message HelloRequest{
    string name = 1;
}

message HelloReply{
    string message = 1;
}

# 客户端
import grpc
import server_pb2
import server_pb2_grpc


def run():
    # 连接grpc服务
    channel = grpc.insecure_channel("127.0.0.1:50051")
    # 调用rpc服务
    stub = server_pb2_grpc.TestStub(channel)
    # 使用发送消息的时候，一定指明name=“x小明”
    response = stub.SayHello(server_pb2.HelloRequest(name='小明'))
    print(f"返回的消息是:{response.message}")


if __name__ == '__main__':
    run()
    
    
# 服务端
import grpc
from concurrent import futures
import time
import server_pb2
import server_pb2_grpc


class Greeter(server_pb2_grpc.TestServicer):
    def SayHello(self, request, context):
        # 实现服务端定义的方法
        print(f"接收到的消息是:{request.name}")
        res = request.name + "你真的太漂亮了"
        # 指明返回消息的时候，也一定指明message="字符串"
        return server_pb2.HelloReply(message=res)


def run():
    # 开启rpc服务
    serverqi = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_TestServicer_to_server(Greeter(), serverqi)
    serverqi.add_insecure_port("127.0.0.1:50051")
    serverqi.start()
    print("服务器开始运行了")
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        serverqi.stop(0)


if __name__ == '__main__':
    run()
