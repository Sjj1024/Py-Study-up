sys模块的常见函数列表
sys.argv: 实现从程序外部向程序传递参数。

sys.exit([arg]): 程序中间的退出，arg=0为正常退出。

sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。

sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）

sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.

sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

sys.platform: 获取当前系统平台。

sys.stdin,sys.stdout,sys.stderr: stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们

sys.argv
功能：在外部向程序内部传递参数
示例：sys.py

#!/usr/bin/env python

import sys
print sys.argv[0]
print sys.argv[1]
运行：

# python sys.py argv1
sys.py
argv1
自己动手尝试一下，领悟参数对应关系

sys.exit(n)
功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）

示例：exit.py

#!/usr/bin/env python

import sys

def exitfunc(value):
    print value
    sys.exit(0)

print "hello"

try:
    sys.exit(1)
except SystemExit,value:
    exitfunc(value)

print "come?"
运行：

# python exit.py
hello
1
sys.path
功能：获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

示例：

>>> import sys
>>> sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']
sys.path.append("自定义模块路径")

sys.modules
功能：sys.modules是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。

示例：modules.py

#!/usr/bin/env python

import sys

print sys.modules.keys()

print sys.modules.values()

print sys.modules["os"]
运行：

python modules.py
['copy_reg', 'sre_compile', '_sre', 'encodings', 'site', '__builtin__',......
sys.stdin\stdout\stderr
功能：stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
