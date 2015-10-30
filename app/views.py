from flask import render_template
from app import app

@app.route('/')
def root():
    return "Root!"

@app.route('/index')
def index():
    #fake database
    user = {'login': 'nick'}

    boats = [
    {
        "name": "Николай Иванов",
        "number": "1234",
        "sea": False
    },
    {
        "name": "Анна Зайцева",
        "number": "54321",
        "sea": True
    },
    {
        "name": "Петр Сидоров",
        "number": "153215",
        "sea": True
    }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        boats = boats)