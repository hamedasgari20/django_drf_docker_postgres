from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status = 'a').count()
    num_author = Author.objects.all().count()
    num_genre = Genre.objects.all().count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_author': num_author,
        'num_genre': num_genre
    }
    return render(request, 'book/index.html', context)


## Generic view for book list
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    context_object_name = 'book'

    # ## query in Generic view
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains = 'Time')

        

## Generic view for author list (generic ListView)
class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = 'author'


## Generic view for Book details (generic DetailView)
class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    context_object_name = 'detail'


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'book/bookinstance_borrowing.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o')