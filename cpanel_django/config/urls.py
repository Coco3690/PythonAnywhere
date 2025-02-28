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
    path('djgo.test/', views.home, name='djgo_home'),
]

# 如果是本地開發環境，將根路徑 `/` 轉向 `/djgo/`
#if IS_LOCAL:
#    urlpatterns.insert(0, path('', lambda request: redirect('djgo/', permanent=True)))

# 加入靜態文件的處理
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)