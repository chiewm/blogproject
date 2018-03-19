from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comments/post/<int:post_pk>', views.post_comments, name='post_comments'),
]