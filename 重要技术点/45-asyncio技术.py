参考文档:https://segmentfault.com/a/1190000008814676

例子说明：
import asyncio
import time


async def first():
    print("nihao shijie")
    await asyncio.sleep(3)


async def second():
    print("woshi d")
    await asyncio.sleep(1)


def call_back():
    print("调用回调函数")


if __name__ == '__main__':
    start = time.time()
    # 获得时间循环对象
    loop = asyncio.get_event_loop()
    # 创建异步协成列表
    geater = [first(), second()]
    # 使用ayncio.gather将事件添加进时间循环
    loop.run_until_complete(asyncio.gather(*geater))
    # 循环完成后，关闭事件循环
    loop.close()
    ends = time.time()
    print(ends-start)
