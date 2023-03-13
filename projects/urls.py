from django.urls import path

from rest_framework import routers

from .api import ProjectViewSet
from .views import CategoryListAPIView, ProductListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView, CategoryAPIView

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='api_category'),
    path('category/list/', CategoryListAPIView.as_view(), name='api_category_list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='api_category_create'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='api_category_update'),
    path('category/delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='api_category_delete'),
    path('product/list/', ProductListAPIView.as_view(), name='api_product_list'),
]
urlpatterns += router.urls
