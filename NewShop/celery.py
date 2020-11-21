import os
from celery import Celery

# Задаем переменную окружения, содержащую название файла настроек нашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewShop.settings')

app = Celery('NewShop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

