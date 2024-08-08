from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # /admin/ 관리자 페이지로 이동!
    path('', include('blog.urls')), # blog 앱의 URL을 include 함수를 사용해 연결
    # www.example.com/post/ -> post 앱의 URL을 연결
]