from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__, static_folder="./client", template_folder="client")  # Настройки приложения

msg_id = 1

DB_FILE = "db.json"


def load_messages():
    with open(DB_FILE, "r") as json_file:
        data = json.load(json_file)
        return data["messages"]


all_messages = load_messages()


def save_messages():
    with open(DB_FILE, "w") as json_file:
        data = {"messages": all_messages}
        json.dump(data, json_file)


@app.route("/chat")
def chat_page():
    return render_template("chat.html")


def add_message(sender, text):
    global msg_id
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
        "msg_id": msg_id
    }
    msg_id += 1
    all_messages.append(new_message)
    save_messages()


# страница для получения списка сообщений
# только новые сообщения: /get_messages?after=0
@app.route("/get_messages")
def get_messages():
    after = int(request.args["after"])
    return {"messages": all_messages[after:]}


@app.route("/send_message")
def send_message():
    sender = request.args["sender"]
    text = request.args["text"]
    add_message(sender, text)
    return {"result": True}


@app.route("/")
def hello_page():
    return "Wellcome to SkillMessenger"


app.run(host="0.0.0.0", port=80)
# app.run()