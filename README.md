# ticker-python

Скрипт для создания бегущей строки на языке python. Используется библиотека moviepy и matplotlib:
> pip install moviepy

> pip install matplotlib

Написана версия для запуска в google colab - ticker.ipynb

-----------------

Создан также django-проект для взаимодействия со скриптом. 

![site](https://github.com/d0ggzi/ticker-python/assets/43131496/8c88d99c-9f70-4c6a-abb1-acd9520d8633)
![gif1](https://github.com/d0ggzi/ticker-python/assets/43131496/c218f305-be86-4a81-b591-e427ffa8ba4b)
![gif2](https://github.com/d0ggzi/ticker-python/assets/43131496/b8a08e59-0b5d-4464-be06-22104fee56a4)

API для взаимодействия из поисковой строки:

> 127.0.0.1:8000/create/?message=hello%20world!!&duration=5&bg_color=chocolate&text_color=white

Можно указать только message, остальные поля заполнятся автоматически

> 127.0.0.1:8000/create/?message=hello%20world

-----------------

Все записывается в базу данных SQLite. 
![image](https://github.com/d0ggzi/ticker-python/assets/43131496/f141eeb0-cc7c-4c05-96e0-dc0ee8efa055)

-----------------

Запуск:
> cd djangoticker

> pip install requirements.txt

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver

-----------------
При желании можно запустить в Docker, в проекте уже написаны Dockerfile и docker-compose.yml