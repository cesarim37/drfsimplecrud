from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer

    # def post(self, request, *args, **kwargs):
    #     print(self.request.data)
    #     return self.create(request, *args, **kwargs)


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def put(self, request, *args, **kwargs):
    #     print(self.request.data)
    #     return self.update(request, *args, **kwargs)


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def delete(self, request, *args, **kwargs):
    #     instance = self.queryset.get(pk=self.kwargs['pk'])
    #     instance.delete()
    #     return Response({'msg': f"Se ha eliminado correctamente el pk {self.kwargs['pk']}"})


class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        return Response({'resp': False})

    def post(self, request, *args, **kwargs):
        print(self.request.data)
        return Response({'resp': True})

