import asyncio
import time

now = lambda: time.time()


async def do_some(x):
    print((f"等待{x}"))
    # await 相当于调用一个携程，可以使用这个方法实现携程嵌套
    await asyncio.sleep(0.5)
    print((f"等待完成{x}"))

async def main():
    # 创建一个携程
    coroutine1 = do_some(1)
    coroutine2 = do_some(2)
    coroutine3 = do_some(3)
    coroutine4 = do_some(4)
    coroutine5 = do_some(5)
    coroutine6 = do_some(6)
    coroutine7 = do_some(7)
    coroutine8 = do_some(8)
    # task是用来保存携程运行的状态,可以保存多个携程
    task1 = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3),
             asyncio.ensure_future(coroutine4),
             asyncio.ensure_future(coroutine5),
             asyncio.ensure_future(coroutine6),
             asyncio.ensure_future(coroutine7),
             asyncio.ensure_future(coroutine8)]
    print(task1)
    # 使用事件循环执行task任务
    await asyncio.wait(task1)
    print(2222222)
    print(task1)
    print(1111111)

start = now()
# 创建一个事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(now() - start)


C:\Users\swx829949\Envs\py_study\Scripts\python.exe D:/Pyup_study/Py异步加载/1-asyncio异步.py
[<Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>, <Task pending coro=<do_some() running at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7>>]
等待1
等待2
等待3
等待4
等待5
等待6
等待7
等待8
等待完成1
等待完成3
等待完成7
等待完成6
等待完成8
等待完成5
等待完成2
等待完成4
2222222
[<Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>, <Task finished coro=<do_some() done, defined at D:/Pyup_study/Py异步加载/1-asyncio异步.py:7> result=None>]
1111111
0.5027174949645996
