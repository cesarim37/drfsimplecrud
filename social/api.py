from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from social.models import Post
from social.serializers import UserSerializer, PostSerializer


class UserAPIView(APIView):
    def post(self, request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           user = serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
