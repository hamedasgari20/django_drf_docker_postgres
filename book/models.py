from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter book name')

    def __str__(self):
        return self.name




class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.first_name, self.last_name)



class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre, help_text='Select a genre')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.status)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False