from random import choice  # Исправляем импорт
from flask import Flask
from datetime import datetime, timedelta
import os
import re
import random

app = Flask(__name__)

# Определяем базовый каталог проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Путь к файлу книги
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


cars_list = ["Chevrolet", "Renault", "Ford", "Lada", "BMW"]
cats_list = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]


@app.route("/hello/<username>")
def hello_world(username):
    return f' Привет, <b>{username}</b>!'


@app.route("/cars/")
def cars():
    return ', '.join(cars_list)

@app.route("/cats/")
def cats():
    return choice(cats_list)  # Используем только choice для выбора случайного элемента

@app.route("/get_time/now")
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущее время и форматируем его
    return f"Точное время: {current_time}"  # Возвращаем строку с текущим временем

@app.route("/get_time/future")
def get_time_in_future():
    # Получаем текущее время
    current_time = datetime.now()
    # Прибавляем 1 час с помощью timedelta
    future_time = current_time + timedelta(hours=1)
    # Форматируем будущее время
    current_time_after_hour = future_time.strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем строку с временем через 1 час
    return f"Точное время через час будет {current_time_after_hour}"

# Функция для получения списка слов из текста
def load_words():
    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        text = book.read()
    # Удаляем знаки препинания и разбиваем текст на слова
    words = re.findall(r'\b\w+\b', text)
    return words

# Загружаем слова один раз при запуске приложения
words_list = load_words()

@app.route("/get_random_word")
def get_random_word():
    # Выбираем случайное слово из списка
    random_word = random.choice(words_list)
    return f"Случайное слово: {random_word}"



@app.route("/counter")
def counter():
    # Увеличиваем счётчик посещений на 1
    counter.visits += 1
    # Возвращаем количество посещений
    return f"Страница открывалась {counter.visits} раз."

# Инициализируем атрибут для хранения числа посещений
counter.visits = 0

from flask import Flask

app = Flask(__name__)


@app.route('/smile')
def smile():
    # Рисуем "улыбку" с использованием букв
    smile_art = """
    :-D

    """
    return f"<pre>{smile_art}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
