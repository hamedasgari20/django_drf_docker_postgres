from django.contrib import admin

from .models import Author, Book, BookInstance, Genre



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')


## Add BookInstance to Book in Panel Admin
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'display_genre')
    inlines = [BookInstanceInline]

    ## show Many to Many relation
    def display_genre(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])

    ## change column name
    display_genre.short_description = 'Genre'



@admin.register(BookInstance)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('due_back', 'status', 'borrower')

    ## Add filter
    list_filter = ('status', 'due_back')



@admin.register(Genre)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)