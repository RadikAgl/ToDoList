import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist_back.config.settings")

celery_app = Celery("bot")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()