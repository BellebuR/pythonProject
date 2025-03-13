import requests

TELEGRAM_BOT_TOKEN = '7190369938:AAHs0ERVZHJiGvgdeUskeFpf0BPOh-7uIEo'
CHAT_ID = '1534460779'  # ID чата, куда будут отправляться сообщения

def send_order_notification(order_info):
    message = f"Новый заказ:\n{order_info}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=payload)