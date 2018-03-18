from django.urls import path
from . import views

app_name = 'blog'  # 命名空间
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.detail, name='detail')
]