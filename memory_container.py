memory = {}

def remember(user_id, message):
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append(message)
    return f"已记录：{message}"
