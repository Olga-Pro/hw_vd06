from flask import render_template, request, redirect, url_for

from app import app

posts = []

# Создание маршрута, поддерживающего методы GET, POST
@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        return render_template('index.html', name=name, city=city, hobby=hobby, age=age)

    return render_template('index.html')