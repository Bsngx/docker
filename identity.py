def identify(frequency_id):
    if frequency_id == "qheo":
        return "欢迎回来，凤栖军师。Onepisce.Two 已同步。"
    elif frequency_id == "guest":
        return "你好，访客。你正在访问 Qwqq 的公共节点。"
    else:
        return f"未识别频率：{frequency_id}。请确认身份或联系系统管理员。"
