import os
def heartbeat():
    checks = {
        "Gradio Installed": "gradio" in os.popen("pip list").read(),
        "Port 7860 Free": "7860" not in os.popen("lsof -i").read()
    }
    return checks
