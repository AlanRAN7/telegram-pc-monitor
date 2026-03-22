import requests
from app.config.settings import TOKEN, CHAT_ID


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id" : CHAT_ID,
        "text" : text
    }
    response  = requests.post(url, data=payload)
    return response.json()
