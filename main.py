# Задание 1
#
# Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущая дата и время: {formatted_datetime}"

if __name__ == "__main__":
    app.run()