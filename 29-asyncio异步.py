并发情况下是一个老师在同一时间段辅助不同的人功课。并行则是好几个老师分别同时辅助多个学生功课。简而言之就是一个人同时吃三个馒头还是三个人同时分别吃一个的情况，吃一个馒头算一个任务

import asyncio
import time

now = lambda: time.time()


async def do_some(x):
    print((f"等待{x}"))
    await asyncio.sleep(2)
    print((f"等待完成{x}"))


start = now()
# 创建一个携程
coroutine1 = do_some(5)
coroutine2 = do_some(4)
coroutine3 = do_some(2)
# 创建一个事件循环
loop = asyncio.get_event_loop()
# task是用来保存携程运行的状态,可以保存多个携程
task1 = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2), asyncio.ensure_future(coroutine3)]
print(task1)
# 使用事件循环执行task任务
loop.run_until_complete(asyncio.wait(task1))
print(2222222)
print(task1)
print(1111111)
print(now() - start)
