這是一個基於Django框架的網頁應用：

### 1. 前端頁面展示

- **HTML模板**：在`cpanel_django/templates/index.html`文件中，有關於頁面佈局的代碼，包括頂部欄、產品卡片、側邊欄（分類側邊欄和購物車側邊欄）等。這些代碼定義了頁面的基本結構和樣式，例如產品的圖片、名稱、價格展示以及購物車圖標的顯示等。
  
  ```html
  <!-- Product Card -->
  <div class="col-lg-4 col-md-6 col-12">
  <div class="card shadow-sm">
  <img src="{% static 'images/400x300.png' %}" class="card-img-top" alt="Product">
  <div class="card-body">
  <h5 class="card-title">猪肉汉堡</h5>
  <p class="card-text">$129.99</p>
  <button class="btn btn-primary">Add to Cart</button>
  </div>
  </div>
  </div>
  ```

- **CSS樣式**：`cpanel_django/static/style.css`和`cpanel_django/static/css/bootstrap.min.css`文件定義了頁面的樣式，如字體、顏色、布局等，使得頁面更加美觀和易於閱讀。
  
  ### 2. 後端邏輯處理

- **視圖函數**：在`cpanel_django/appfiles/views.py`文件中，`home`函數負責渲染`index.html`模板，將頁面返回給用戶。
  
  ```python
  from django.shortcuts import render
  def home(request):
  return render(request, 'index.html')
  ```

- **URL路由**：`cpanel_django/config/urls.py`文件配置了URL路由，將特定的URL路徑映射到對應的視圖函數。例如，`/djgo.test/`路徑會調用`views.home`函數。
  
  ```python
  from django.contrib import admin
  from django.urls import path
  from appfiles import views
  urlpatterns = [
  path('admin/', admin.site.urls),
  path('djgo.test/', views.home, name='djgo_home'),
  ]
  ```
  
  ### 3. 專案運行與部署

- **運行腳本**：`cpanel_django/run.bat`文件是一個批處理腳本，用於在本地開發環境中啓動Django開發服務器。cpanel則是需要到Terminal`set DJANGO_LOCAL=True`
  
  ```batch
  set DJANGO_LOCAL=True
  python manage.py runserver
  ```

- **WSGI配置**：`cpanel_django/config/wsgi.py`和`cpanel_django/passenger_wsgi.py`文件用于配置WSGI應用，方便項目在生產環境中部署。
