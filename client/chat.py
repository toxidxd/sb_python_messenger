import document as document

from utils import set_timeout, fetch

last_seen_id = 0
send_message = document.getElementById("send_message")


def append_message(message):
    pass


async def send_message_click(e):
    pass


async def load_fresh_messages():
    pass


send_message.onclick = send_message_click
set_timeout(2, load_fresh_messages)
