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
application = WhiteNoise(application, root="/home/j8bghfeg3tig/djgo.test/staticfiles/")