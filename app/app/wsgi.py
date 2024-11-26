import os
from django.core.wsgi import get_wsgi_application

# Укажите настройки вашего проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

