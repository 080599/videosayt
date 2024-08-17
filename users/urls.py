from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('upload/', views.upload_video, name='upload_video'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('comment/<int:video_id>/', views.add_comment, name='add_comment'),
    path('like/<int:video_id>/', views.like_video, name='like_video'),
    path('dislike/<int:video_id>/', views.dislike_video, name='dislike_video'),
]