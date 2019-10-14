第一种简单方法：

生产pyc文件: python3 -m compileall -b .
删除py文件: find . -name “*.py” |xargs rm -rf
删除pycache目录: find . -name “pycache” |xargs rm -rf
第二种：
项目同名文件下 创建 pyc_compile.py 本地测试linunx环境

import os
import sys
import shutil
from py_compile import compile

#print "argvs:",sys.argv
if len(sys.argv) == 3:
    comd = sys.argv[1]  #输入的命令
    path = sys.argv[2]  #文件的地址
    if os.path.exists(path) and os.path.isdir(path):
        for parent,dirname,filename in os.walk(path):
            for cfile in filename:
                fullname = os.path.join(parent,cfile)
                if comd == 'clean' and cfile[-4:] == '.pyc':
                    try:
                        os.remove(fullname)
                        print("Success remove file:%s" % fullname)
                    except:
                        print("Can't remove file:%s" % fullname)
                if comd == 'compile' and cfile[-3:] == '.py':   #在这里将找到的py文件进行编译成pyc，但是会指定到一个叫做__pycache__的文件夹中
                    try:
                        compile(fullname)
                        print("Success compile file:%s" % fullname)
                    except:
                        print("Can't compile file:%s" % fullname)
                if comd == 'remove' and cfile[-3:] == '.py' and cfile != 'settings.py' and cfile != 'wsgi.py':
                    try:
                        os.remove(fullname)
                        print("Success remove file:%s" % fullname)
                    except:
                        print("Can't remove file:%s" % fullname)
                if comd=='copy' and cfile[-4:] == '.pyc':
                    parent_list = parent.split("/")[:-1]
                    parent_up_path = ''
                    for i in range(len(parent_list)):
                        parent_up_path+=parent_list[i]+'/'
                    print(fullname, parent_up_path)
                    shutil.copy(fullname,parent_up_path)
                    print('update the dir of file successfully')
                if comd=='cpython' and cfile[-4:] =='.pyc':
                    cfile_name = ''
                    cfile_list = cfile.split('.')
                    for i in range(len(cfile_list)):
                        if cfile_list[i]=='cpython-36':
                            continue
                        cfile_name+=cfile_list[i]
                        if i==len(cfile_list)-1:
                            continue
                        cfile_name+='.'
                    shutil.move(fullname,os.path.join(parent,cfile_name))
                    print('update the name of the file successfully')

    else:
        print("Not an directory or Direcotry doesn't exist!")
else:
    print("Usage:")
    print("\tpython compile_pyc.py clean PATH\t\t#To clean all pyc files")
    print("\tpython compile_pyc.py compile PATH\t\t#To generate pyc files")
    print("\tpython compile_pyc.py remove PATH\t\t#To remove py files")

先将文件编译成pyc文件:，
python pyc_cpmpile.py compile project
但是文件都存在各个文件夹的__pycache__中
将__pycache__中的pyc文件拷贝到原来py存在的位置：
python pyc_compile copy project
文件的根路径；这样就将编译的文件存在原来py文件的位置了
将原来的py文件删掉就可以了：
python pyc_compile remove project
将文件的名字进行更改:
python pyc_compile cpython project
我这里使用的是pyhon 3.6版本的，所以文件的名字变	成了*.cpython-36.pyc,	要将其中的cpython-36去掉，不然不能正常运行，因为文件的名字默认最后一个后缀是扩展名，其他的为文件名字
