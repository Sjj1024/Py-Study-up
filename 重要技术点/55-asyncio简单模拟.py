import time
import asyncio


async def hello(i):
    print("Waiting:", i)
    # 使用await asyncio.sleep(i)模拟耗时操作，例如网络请求，文件读写等等
    await asyncio.sleep(i)
    print("Done after {}s".format(i))


def run():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(10):
        task = asyncio.ensure_future(hello(i))
        tasks.append(task)
    # asyncio.wait是将耗时操作挂起，继续下一个任务
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    now = time.time()
    run()
    end = time.time()
    print(f"总耗时：{end - now}")
