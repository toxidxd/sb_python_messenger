from flask import Flask

app = Flask(__name__) # Настройки приложения

@app.route("/hello")
def hello_page():
    return "Wellcome to SkillMessenger"


app.run()

# def add_message(sender, text):
#     new_message = {
#         "sender": sender,
#         "text": text,
#         "time": "25:79" # TODO подставлять автоматом
#     }

#     all_messages.append(new_message)


# def print_msg(message):
#     print(f"[{message['sender']}]: {message['text']} / {message['time']}")


# all_messages = []

# add_message("Misha", "Python is cool")
# add_message("pavel", "not cool")
# add_message("max", "Python is bad")
# add_message("kit", "hello")

# # print_msg(all_messages[0])

# for msg in all_messages:
#     print_msg(msg)
