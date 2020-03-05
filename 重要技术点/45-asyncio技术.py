import asyncio
import time
import functools


async def first():
    print("nihao shijie")
    await asyncio.sleep(3)
    return "first"

async def second():
    print("woshi d")
    await asyncio.sleep(1)
    return "second"

async def three():
    print("woshi disange")
    await asyncio.sleep(1)
    return "three"


def call_back(loop, futu):
    print("调用回调函数")
    # 在回调函数中，同样会将future对象传进来，因此获取到一步函数的返回值
    print(futu.result(), 111111111)
    loop.stop()


if __name__ == '__main__':
    start = time.time()
    # 获得时间循环对象
    loop = asyncio.get_event_loop()
    # 创建异步协成列表
    geater = [first(), second(), three()]
    # 可以创建一个future对象，将多个异步任务合并成一个future
    futu = asyncio.gather(*geater)
    # 使用future添加异步任务都完成后的回调函数
    # functools.partial会先将函数的部分参数传递进去，等所有参数都传递完了，再开始调用
    futu.add_done_callback(functools.partial(call_back, loop))
    # 使用ayncio.gather将事件添加进时间循环
    # loop.run_until_complete(asyncio.gather(*geater))
    loop.run_forever()
    # 循环完成后，关闭事件循环
    # loop.close()
    ends = time.time()
    print(ends-start)
