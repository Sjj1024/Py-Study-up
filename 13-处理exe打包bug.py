1. 增加一个获取路径的方法，将原py中使用os.path路径的地方，都改成这种，
import os
import sys


def get_path():
    pathname = ""
    if getattr(sys, 'frozen', False):  # 如果是exe状态，sys会有frozen属性，
        pathname = sys._MEIPASS  # 当处于冻结状态，也就是exe状态的时候，使用这个路径
    else:
        pathname = os.path.abspath('.')  # 否则使用原本路径
    return pathname
    
 2.先生成spec文件，然后将需要用的资源目录添加到datas中：
 生成方式：pyi-makespec -F start.py
 
 # -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['start.py'],
             pathex=['D:\\Py_main\\breeze'],
             binaries=[],
             datas=[('app','app')],  # 修改这里
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

3.第三步：使用spec文件打包exe

pyinstaller -F start.spec

 
