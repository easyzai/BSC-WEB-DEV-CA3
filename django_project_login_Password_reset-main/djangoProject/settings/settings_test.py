from djangoProject.settings.settings import *
from dotenv import load_dotenv


load_dotenv()  

DEBUG = True

SECRET_KEY = str(os.getenv('SECRET_KEY'))

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':BASE_DIR + 'db.sqlite3'
        

    }
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True