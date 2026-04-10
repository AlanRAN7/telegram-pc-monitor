from app.bot.telegram_client import send_message
from app.monitor.system_monitor import get_system_status
from app.alerts.alert_manager import check_alerts
import time

if __name__ == "__main__":
    status = get_system_status()

    message = f"""
📊 Estado del sistema:

CPU: {status['cpu']}%
RAM: {status['ram']['percent']}% ({status['ram']['used']} / {status['ram']['total']})

GPU: {status['gpu']['used']}MB / {status['gpu']['total']}MB
🌡 GPU Temp: {status['gpu']['temp']}°C
"""

    send_message(message)
    
    alerts = check_alerts(status)
    for alert in alerts:
        send_message(alert)