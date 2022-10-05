from utils import set_timeout, fetch

last_seen_id = 0
send_message = document.getElementById("send_message")


def append_message(message):
    pass


async def send_message_click(e):
    pass


async def load_fresh_messages():
    global last_seen_id
    result = await fetch(f"/get_messages?after={last_seen_id}", method="GET")
    payload = await result.json()
    messages = payload["messages"]
    for message in messages:
        msg_id = message["msg_id"]
        if msg_id >= last_seen_id:
            last_seen_id = msg_id + 1
        append_message(message)
    set_timeout(2, load_fresh_messages)


send_message.onclick = send_message_click
set_timeout(2, load_fresh_messages)
