from django.urls import path
from .views import BookList, BookDetail, UserList, UserDetail

from django.urls import path, re_path


app_name = 'api'

urlpatterns = [
    path('book/', BookList.as_view(), name='list'),
    path('book/<int:pk>', BookDetail.as_view(), name='detail'),
    path('users/', UserList.as_view(), name='usersList'),
    path('users/<int:pk>', UserDetail.as_view(), name='userDetails'),

]



