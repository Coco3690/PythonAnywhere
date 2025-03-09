## 一、創建cpanel的python網站(只能是子目錄)

---

## 到cpanel => setup python app 創建 create application

Python version 選最新版本
Application root : djgo
Application URL : djgo
Application startup file : app.py
Application Entry point : application
Passenger log file : /home/j8bghfeg3tig/djgo.log
Environment variables ==>這很重要，可以存放私密的api key

## 會創建一個網址如下(<mark>pythonanywhere不會有子目錄、配置和cpanel不一樣</mark>)

```
https://abc123.com/djgo/
```

### 此時，系統會自動造出兩個目錄和底下的檔案

1️⃣第一個目錄只有.htaccess，/home/j8bghfeg3tig/public_html/djgo/.htaccess

> 此htaccess就是要把 http://域名/djgo轉向去執行  /home/j8bghfeg3tig/djgo/app.py
> j8bghfeg3tig 是每個cpanel虛擬主機的根目錄代號

### 要把PassengerBaseURI "/djgo" 改為 PassengerBaseURI "/"

```sh
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION BEGIN
PassengerAppRoot "/home/j8bghfeg3tig/djgo"
PassengerBaseURI "/"
PassengerPython "/home/j8bghfeg3tig/virtualenv/djgo/3.11/bin/python"
PassengerAppLogFile "/home/j8bghfeg3tig/djgo.log"
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION END
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION BEGIN
<IfModule Litespeed>
</IfModule>
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION END
```

2️⃣第二個目錄會創建兩支檔案

>  /home/j8bghfeg3tig/djgo/app.py
>  /home/j8bghfeg3tig/djgo/passenger_wsgi.py

【此時www是可以抓到 https://abc123.com/djgo/index.html】



但python website的檔案不是放public_html下的位置

所以檔案不要放在  /home/j8bghfeg3tig/public_html/djgo/。
python檔案都放在  /home/j8bghfeg3tig/djgo/ ==>設定一個ftp帳號用FileZilla連到此目錄或使用cpanel的File Manager(可以查看log訊息)。

---

## 二、在本地端創建django網站

在win11創建一個本地端的django

為了迎合cpanel只採子目錄的方式、網址必須是 http://127.0.0.1:8000/digo

## 

## [這次不要用django-admin命令，手工創建目錄和程式]

<mark>不需要執行 django-admin startproject</mark>

先粗略定義目錄

> manage.py 放在 D:\\_sd\\_cursor\cpanel_python_cart\djgo\manage.py
> passenger_wsgi.py 放在 D:\\_sd\\_cursor\cpanel_python_cart\djgo\passenger_wsgi.py
> settings.py 放在 D:\\_sd\\_cursor\cpanel_python_cart\djgo\config\settings.py
> views.py 放在D:\\_sd\\_cursor\cpanel_python_cart\djgo\appfiles\views.py
> html檔案放在 D:\\_sd\\_cursor\cpanel_python_cart\djgo\templates
> css、js、images 放在 D:\\_sd\\_cursor\cpanel_python_cart\djgo\static

Django的目錄結構 
│── manage.py                     # Django 管理指令入口
│── passenger_wsgi.py
├── appfiles                      # 應用程式 (app)
│   ├── __init__.py               # 標記此目錄為 Python 套件
│   ├── views.py                  # 處理請求並回傳對應的 HTML
│   ├── models.py                 # 資料庫模型 (如果有的話)
│   ├── urls.py                    # app 層級的 URL 設定 (如果有的話)
│   ├── forms.py                   # 表單處理 (如果有的話)
│   ├── admin.py                   # Django 後台管理設定
│   ├── tests.py                   # 單元測試
│   ├── migrations/                # 資料庫遷移檔案
│
├── config                         # 專案設定 (Project Settings)
│   ├── __init__.py               # 標記此目錄為 Python 套件
│   ├── settings.py               # 專案設定 (Django 配置)
│   ├── urls.py                   # URL 路由設定
│   ├── wsgi.py                   # WSGI 入口 (用於部署)
│
├── static                         # 靜態檔案 (CSS、JS、圖片等)
│   ├── css/                      # CSS 檔案
│   ├── js/                       # JavaScript 檔案
│   ├── images/                   # 圖片檔案
│
├── templates                      # HTML 模板
│   ├── index.html                 # 首頁模板
│   ├── base.html                  # 頁面共用模板 (如果有的話)
│   ├── app/                       # 其他應用的模板 (如果有的話)
│
└── db.sqlite3                      # SQLite 資料庫 (Django 預設)

---

## 手動建立一個Django專案:創建以下目錄

├── appfiles
├── config
├── static
├── templates

> 本地端 (127.0.0.1:8000/) 會用 /static/
> cPanel (abc123.com/djgo/) 會用 /djgo/static/

### cPanel (abc123.com/djgo/)有一個子目錄，但本地端 (127.0.0.1:8000/) 沒有，如何自動適應不同的 URL，必須注意四支檔案，而且要在本地製造staticfiles目錄，上傳到cpanel主機

> config/settings.py
> config/urls.py
> templates/index.html
> passenger_wsgi.py

---

> manage.py裡的DJANGO_SETTINGS_MODULE 為何設為 config.settings，因為settings.py 在config目錄中，這是python的package命令規則，所以創建目錄時，不要和python傳統的package名稱重複

✏️在 manage.py 同一個路徑中創建 passenger_wsgi.py

passenger_wsgi.py

```
import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# 設置環境變數
os.environ.setdefault("DJANGO_LOCAL", "False")  # cPanel 預設為 False
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# 設置 Django WSGI
application = get_wsgi_application()

# **用 WhiteNoise 提供靜態檔案**
application = WhiteNoise(application, root="/home/j8bghfeg3tig/djgo/staticfiles/")
```

✏️manage.py

```python
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
```

✏️config/settings.py

```python
import os
import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jqjg24x2fk1e78p6#%(6mw87a^!!#lgfc(usyyf(eej7u!1=i!'
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','abc123.com']

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
    STATIC_URL = '/djgo/static/'  # cPanel 需指向子目錄

# **(1) 本地開發模式**
if IS_LOCAL:
    STATICFILES_DIRS = [BASE_DIR / 'static']  # 靜態文件目錄 (適用於開發環境)
    STATIC_ROOT = None  # 不用 `collectstatic`

# **(2) cPanel 部署模式**
else:
    STATICFILES_DIRS = []  # cPanel 不需要這個
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # `collectstatic` 的目標目錄
```

✏️config/wsgi.py

```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
```

✏️config/urls.py

```python
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from appfiles import views
import os

# 判斷是否為本地開發環境
IS_LOCAL = os.getenv('DJANGO_LOCAL', 'False') == 'True'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djgo/', views.home, name='djgo_home'),
]

# 如果是本地開發環境，將根路徑 `/` 轉向 `/djgo/`
#if IS_LOCAL:
#    urlpatterns.insert(0, path('', lambda request: redirect('djgo/', permanent=True)))

# 加入靜態文件的處理
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

✏️appfiles/views.py

```python
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
```

✏️templates/index.html

```python
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django 測試頁面</title>
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}">

</head>
<body>
    <h1>歡迎來到 Django 測試頁面</h1>
</body>
</html>
```

✏️static/style.css

```python
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    text-align: center;
    padding: 50px;
}
h1 {
    color: blue;
}
```

產生靜態頁面目錄 staticfiles：

```
python manage.py collectstatic
```

遷移數據庫：

```sh
python manage.py migrate
```

啟動 Django 伺服器(本地端要設定DJANGO_LOCAL變數)：

```sh
set DJANGO_LOCAL=True
python manage.py runserver
```

---

## 三、上傳本地端的django檔案到cpanel

查看cpanel主機上的 public_html/djgo/.htaccess 得知python的路徑

```sh
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION BEGIN
PassengerAppRoot "/home/j8bghfeg3tig/djgo"
PassengerBaseURI "/"
PassengerPython "/home/j8bghfeg3tig/virtualenv/djgo/3.11/bin/python"
PassengerAppLogFile "/home/j8bghfeg3tig/djgo.log"
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION END
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION BEGIN
<IfModule Litespeed>
</IfModule>
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION END
```

### 進入cpanel的Terminal，啟動虛擬環境

```
source /home/j8bghfeg3tig/virtualenv/djgo/3.11/bin/activate
```

### 安裝 Django 和其他依賴

```
pip install django
pip install whitenoise
```

---

## 四、同樣的Django檔案，網址由https://abc123.com/djgo/改成https://abc123.com/cart/，需要更改：

**查 3d929.com/cart/ 底下的.htaccess，知道它的python虛擬環境路徑(cpanel->filemanager)**

### 將PassengerBaseURI "/cart" 改為 PassengerBaseURI "/"

```sh
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION BEGIN
PassengerAppRoot "/home/j8bghfeg3tig/cart"
PassengerBaseURI "/cart"
PassengerPython "/home/j8bghfeg3tig/virtualenv/cart/3.11/bin/python"
PassengerAppLogFile "/home/j8bghfeg3tig/cart.log"
# DO NOT REMOVE. CLOUDLINUX PASSENGER CONFIGURATION END
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION BEGIN
<IfModule Litespeed>
</IfModule>
# DO NOT REMOVE OR MODIFY. CLOUDLINUX ENV VARS CONFIGURATION END
```
