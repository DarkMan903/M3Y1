from flask import Flask
import random

app = Flask(__name__)

@app.route("/fact_list")
def hello_world():
    facts_list = [
        'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
        'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
        'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.'
    ]
    return f'<h1> Ну если так интересно, то: </h1> <p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def secret():
    return '<h1>ТЕБЕ НЕЛЬЗЯ БЫТЬ <a href = "/warning">ЗДЕСЬ</a>!</h1>'

@app.route("/warning")
def warning():
    return '<h1>Я <a href = "/cat">ПРЕДУПРЕЖДАЮ</a>!<h1>'

@app.route("/cat")
def cat():
    return '<img src = "https://i.pinimg.com/originals/bc/a5/6e/bca56e4dcce9cf6929b5b44a85dc93cf.jpg"> <p> Уйдите, пожалуйста \U0001F643 </p>'

@app.route("/")
def index():
    return f'<h1> Здрасте! Это для просмотра <a href = "/fact_list">факта</a> :3 </h1> <h2> Если что есть секретная страничка, но лучше не ищи \U0001F642 </h2> <p> Не приписывай /secret \U0001F609 </p>'
app.run(debug=True)
