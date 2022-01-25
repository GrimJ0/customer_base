import os

base_dir = 'C:\Dev\customer_base'
os.system(fr"cd {base_dir} && venv\Scripts\activate && start chrome http://127.0.0.1:8000/ && python manage.py runserver")
