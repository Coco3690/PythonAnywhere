import os
import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jqjg24x2fk1e78p6#%(6mw87a^!!#lgfc(usyyf(eej7u!1=i!'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','3d929.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appfiles',  # 註冊你的 app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 確認是否在本地端運行
IS_LOCAL = os.getenv('DJANGO_LOCAL', 'False') == 'True'

# 設置 STATIC_URL 根據環境自動調整
if IS_LOCAL:
    STATIC_URL = '/static/'
else:
    STATIC_URL = '/djgo.test/static/'  # cPanel 需指向子目錄

# **(1) 本地開發模式**
if IS_LOCAL:
    STATICFILES_DIRS = [BASE_DIR / 'static']  # 靜態文件目錄 (適用於開發環境)
    #STATIC_ROOT = None  # 不用 `collectstatic`
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # `collectstatic` 的目標目錄

# **(2) cPanel 部署模式**
else:
    STATICFILES_DIRS = []  # cPanel 不需要這個
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # `collectstatic` 的目標目錄