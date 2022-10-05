from utils import set_timeout, fetch
from datetime import datetime

last_seen_id = 0
send_message = document.getElementById("send_message")
sender = document.getElementById("sender")
message_text = document.getElementById("message_text")
chat_window = document.getElementById("chat_window")


# Добавляет новое сообщение в список сообщений
def append_message(message):
    # Создаем HTML-элемент представляющий сообщения
    item = document.createElement("li") # li - это HTML-тег для элемента списка
    item.className = "list-group-item"
    # Добавляем его в список сообщений (chat_window)
    item.innerHTML = f'[<b>{message["sender"]}</b>]: <span>{message["text"]}</span> ' \
                     f'<span class="badge text-bg-dark text-warning">{message["time"]}</span>'
    chat_window.prepend(item)


# Вызывается при клике на send_message
async def send_message_click(e):
    # Отправить запрос к странице /send_message
    await fetch(f"/send_message?sender={sender.value}&text={message_text.value}", method="GET")
    message_text.value = ""


# Загружает новые сообщения с сервера и отображает их
async def load_fresh_messages():
    global last_seen_id
    result = await fetch(f"/get_messages?after={last_seen_id}", method="GET")
    # chat_window.innerHTML = ""  # Очищаем окно с сообщениями
    # append_message({"sender": "GOD", "text": "Welcome to toxidxd Chat", "time": "00:00"})
    data = await result.json()
    all_messages = data["messages"]  # берем список сообщений из ответа сервера
    for msg in all_messages:
        last_seen_id = msg["msg_id"]
        append_message(msg)

    set_timeout(1, load_fresh_messages)  # Загружаем сообщения через 1 секунду

# Устанавливаем действие при клике
send_message.onclick = send_message_click
load_fresh_messages()
