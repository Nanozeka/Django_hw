from django.shortcuts import render

from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Мой первый сайт на Джанго</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'

def main(request):
    title = 'Главная страница сайта'
    body_text = 'Текст главной страницы сайта, с наполнением разной информацией'
    logger.info(f'Page "main" is open')
    return HttpResponse(text(title, body_text))

def about(request):
    title = 'О себе'
    body_text = 'Меня зовут Евгений, и я студент онлайн платформы Geekbrains<br>' \
                'Группа - Программист разработчик языка Python'
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
