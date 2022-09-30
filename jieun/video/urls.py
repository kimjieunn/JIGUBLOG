from django.urls import path, re_path
from . import views

app_name = 'video'
urlpatterns =[
    path('', views.video, name= 'video'),

    path('add/', views.VideoCreateView.as_view(), name='video_add'),
    path('change/', views.VideoChangeLV.as_view(), name='video_change'),
    path('<int:pk>/update/', views.VideoUpdateView.as_view(), name='video_update'),
    path('<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video_delete'),
]