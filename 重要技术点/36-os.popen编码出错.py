python 使用 os的 popen(‘命令’) 如果命令行输出中 有中文乱码， 提示 'gbk' 无法解析的错误 解决办法:


        output = os.popen(commond)
        temp = output._stream
        resultStr = temp.buffer.read().decode(encoding='utf-8')
