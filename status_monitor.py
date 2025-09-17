def system_status():
    import platform, psutil
    return {
        "系统": platform.system(),
        "Python版本": platform.python_version(),
        "CPU使用率": f"{psutil.cpu_percent()}%",
        "内存使用率": f"{psutil.virtual_memory().percent}%"
    }
