from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import google.generativeai as genai
from dotenv import load_dotenv
import os


def describe_image(image_bytes):
    # 获取当前文件所在目录的父目录
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建.env.local 文件的相对路径
    env_path = os.path.join(parent_dir, '..', '.env.local')
    # 加载.env.local 文件
    load_dotenv(env_path)
    # 读取 GEMINI_API_KEY 环境变量
    gemini_key = os.getenv('GEMINI_API_KEY')
    if not gemini_key:
        raise ValueError("GEMINI_API_KEY not found in.env.local")
    # 进行身份验证
    genai.configure(api_key=gemini_key)
    # 选择新的图像描述模型，使用 gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    try:
        # 发送请求，将图像的二进制数据作为输入，仅保留 data 和 mime_type 信息
        response = model.generate_content([
            {"data": image_bytes, "mime_type": "image/jpeg"},
            "Describe what you see in this image."
        ])
        # 获取生成的内容
        description = response.text
        return description
    except Exception as e:
        return f"Error occurred: {str(e)}"


@csrf_exempt  # 如果需要，可以根据需求调整 CSRF 保护
def convert_view(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            # 读取上传的图片文件内容
            image_bytes = image_file.read()
            # 调用图像识别函数
            description = describe_image(image_bytes)
            return JsonResponse({'description': description})
        else:
            return JsonResponse({'error': 'No image file provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def home(request):
    return render(request, 'image_analyze.html')  # 确保这里的 'image_analyze.html' 是存在的模板