# Customer base

## Описание

Customer base это онлайн-сервис, для добавления клиентов в базу.


## Стек технологий

- проект написан на Django
- база данных - SQLite3
- система управления версиями - git
- Bootstrap5
- JavaScript
- django-filters
- django-tables2

## Как запустить проект:

1) Клонируйте репозитроий с проектом:
   ```
   https://github.com/GrimJ0/customer_base.git
   ```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
   ```
   python -m venv venv
   ```
   on Windows 
   ```
   venv\Scripts\activate
   ```
   on Unix or MacOS
   ```
   source venv/bin/activate
   ```
   ```
   pip install -r requirements.txt
   ```
3) Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта
    - SECRET_KEY= # сгенерировать ключ можно на сайте [Djecrety](https://djecrety.ir/)


4) Выполните миграции:
   ```
   python manage.py migrate
   ```
5)Cоздайте суперпользователя:
   ```
   python manage.py createsuperuser
   ```
6)Запустите сервер:
   Через команду:
   ```
   python manage.py runserver
   ```
   или через файл setup.py предварительно изменив base_dir:

   ```
   on Windows
   base_dir = 'C:\Dev\customer_base'
   
   ```

__________________________________
Ваш проект запустился на http://localhost:8000/

## Ресурсы cd Customer base

- ### Главная страница:
    - Содержимое главной страницы — фильтр клиентов и таблица с клиентами.

- ### Страница Новый клиент:
    - На странице форма для добавления клиентов с возможностью одновременно добавить несколько клиентов.
