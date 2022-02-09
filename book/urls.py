from django.urls import path
from .import views

app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.BookListView.as_view(), name='bookList'),
    path('authors', views.AuthorListView.as_view(), name='authorList'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='BookDetail'),
    path('mybooks/', views.LoanedBookByUserListView.as_view(), name='mybooks'),
]
