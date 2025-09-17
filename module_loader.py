import importlib

def load_module(name):
    try:
        mod = importlib.import_module(name)
        return f"模块 {name} 已加载"
    except Exception as e:
        return f"加载失败：{e}"
