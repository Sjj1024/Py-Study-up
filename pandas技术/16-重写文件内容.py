1.读文件后，光标定位实在文件末尾的，如果再写入内容，则是追加到后面了
2.w+ 模式中，先写再读，是读取不到内容的，因为写完之后，光标也是在文件末尾的
seek方法会将光标位置移动到需要的位置
truncate 将会清空文件内容

with open(start_path, "r+") as f:
    content_str = f.read()
    new_content = content_str.replace(f"hiddenimports={package_name}", "hiddenimports=[]")
    f.seek(0)
    f.truncate()
    f.write(new_content)
    f.close()
