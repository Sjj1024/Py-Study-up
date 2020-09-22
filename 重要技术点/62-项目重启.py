重启项目，先获取当前项目进程，然后将当前进程内存清空，替换成新启动的进程

def restart():
    Logger.log("重新启动程序......")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
    
