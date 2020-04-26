import time
import asyncio


async def hello(i):
    print("Waiting:", i)
    # 使用await asyncio.sleep(i)模拟耗时操作，例如网络请求，文件读写等等
    await asyncio.sleep(i)
    # print("Done after {}s".format(i))
    return "Done after {}s".format(i)


def run():
    # 创建一个事件循环
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(10):
        task = asyncio.ensure_future(hello(i))
        tasks.append(task)
    # asyncio.wait是将耗时操作挂起，继续下一个任务
    # loop.run_until_complete(asyncio.wait(tasks))

    # 用来存储结果结合列表
    tasks_res = []
    for task in tasks:
        loop.run_until_complete(task)
        # 获取结果对象是task.result()方法
        res = task.result()
        tasks_res.append(res)
        # 只有当事件循环中的任务全部执行完，才会执行后面的操作
        print("222222222")
    # 任务还是全部挂起同时执行的，所以总耗时还是10秒，只有等所有任务执行完了，才会继续后面的操作

    # 这就比线程好太多了，线程就像脱缰的野马，
    print(tasks_res)


if __name__ == '__main__':
    now = time.time()
    run()
    end = time.time()
    print(f"总耗时：{end - now}")
