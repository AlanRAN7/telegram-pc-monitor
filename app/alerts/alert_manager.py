alert_state = {
    "cpu": False,
    "ram": False,
    "gpu_temp": False
}

def check_alerts(status):
    alerts = []

    # CPU
    if status["cpu"] > 80:
        if not alert_state["cpu"]:
            alerts.append(f"🚨 CPU alta: {status['cpu']}%")
            alert_state["cpu"] = True
    else:
        alert_state["cpu"] = False

    # RAM
    if status["ram"]["percent"] > 85:
        if not alert_state["ram"]:
            alerts.append(f"🚨 RAM alta: {status['ram']['percent']}%")
            alert_state["ram"] = True
    else:
        alert_state["ram"] = False

    # GPU TEMP
    if status["gpu"]["temp"] > 75:
        if not alert_state["gpu_temp"]:
            alerts.append(f"🌡 GPU caliente: {status['gpu']['temp']}°C")
            alert_state["gpu_temp"] = True
    else:
        alert_state["gpu_temp"] = False

    return alerts