from utils import set_timeout, fetch

last_seen_id = 0
send_message = document.getElementById("send_message")
sender = document.getElementById("sender")
message_text = document.getElementById("message_text")

# Добавляет новое сообщение в список сообщений
def append_message(message):
    pass


# Вызывается при клике на send_message
async def send_message_click(e):
    # Отправить запрос к странице /send_message
    await fetch(f"/send_message?sender={sender.value}&text={message_text.value}", method="GET")
    message_text.value = ""


# Загружает новые сообщения с сервера и отображает их
async def load_fresh_messages():
    pass


# Устанавливаем действие при клике
send_message.onclick = send_message_click

# Загружаем сообщения через 1 секунду
# set_timeout(1, load_fresh_messages)
