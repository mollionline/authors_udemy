from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='django-insecure-x+xls8zi(@4-qn0k&ht+&3($*72at#4hpt=qkxeebbee%5vbi8'
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
