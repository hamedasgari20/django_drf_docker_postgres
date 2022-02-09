
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from book.models import Book
from .serializers import BookSerializer, UserSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly


# class BookList(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    filterset_fields = ['title', 'summary']
    search_fields = ['title', 'summary']
    ordering_fields = ['isbn']
    ordering = ["-isbn"]

    serializer_class = BookSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

# class BookDetail(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer    

# class BookDetail(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer   

# class BookDetail(RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer  

# class BookDetail(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetail(RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)







class UserList(ListCreateAPIView):
    # queryset = User.objects.all()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsSuperUser,)
    # permission_classes = (IsStaffOrReadOnly,)
    

class UserDetail(RetrieveUpdateDestroyAPIView):
    # queryset = User.objects.all()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsSuperUser,)
    # permission_classes = (IsStaffOrReadOnly,)