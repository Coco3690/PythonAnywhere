這個項目是一個基於Django框架的圖像分析應用，主要用途是接收用戶上傳的圖像文件，並對其進行視覺描述。

### 功能概述

- **圖像上傳**：用戶可以通過前端頁面上傳圖像文件。   
- **圖像分析**：後端調用Google Gemini API對上傳的圖像進行分析，生成圖像的文字描述。   
- **結果返回**：將生成的圖像描述以JSON格式返回給前端。
- ### 詳细工作流程
1. **前端頁面**
   - 用戶訪問 `image_analyze.html` 頁面，該頁面包含一個文件上傳表單。用戶可以選擇要上傳的圖像文件。 
   - 當用戶選擇圖像文件時，會觸發 `change` 事件，將選中的圖像顯示在頁面上。
   - 點擊“Upload and Analyze”按鈕可提交表單。
2. **後端處理**
   - 表單提交后，請求會發送到 `convert_view` 視圖函數。
   - `convert_view` 函數會檢查請求方法是否為 `POST`，如果是，則嘗試從請求中獲取上傳的圖像文件。
   - 如果獲取到圖像檔案，會讀取其內容並調用 `describe_image` 函數進行圖像分析。
   - `describe_image` 函數會加載環境變量中的 `GEMINI_API_KEY`，使用該密鑰對Google Gemini API進行身份驗證，然後將圖像的二進制數據發送給API進行分析，並返回生成的描述。
   - 最後，`convert_view` 函式將生成的描述以 JSON 格式返回給前端。
     
     ### 代碼關鍵部分
- **前端代碼**：`image_visual_description/templates/image_analyze.html` 負責圖像上傳和顯示，以及表單提交。
- **後端視圖函數**：`image_visual_description/mysite/views.py` 中的 `convert_view` 和 `describe_image` 函數負責處理請求和調用API。
- **Django配置文件**：`image_visual_description/mysite/settings.py` 包含項目的配置信息，如數據庫設置、靜態文件路徑等。
