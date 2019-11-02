# 创建一个 src 文件夹,里面有一个 commons.py 文件，内容如下
def add():
    print("add ....")


# 创建一个 app.py 文件，内容如下：
module = 'src.commons'
func_name = 'add'

import importlib
m = importlib.import_module(module)
print(m)
func = getattr(m, func_name)
func()

# 运行 app.py ，结果：
add ....
