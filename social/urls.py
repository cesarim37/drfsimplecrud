from django.urls import path
from .api import UserAPIView, PostListAPIView, PostCreateAPIView


urlpatterns = [
    path('api/create_user/', UserAPIView.as_view(), name='api_create_user'),
    path('api/post/list/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/post/create/', PostCreateAPIView.as_view(), name='api_post_create'),
]