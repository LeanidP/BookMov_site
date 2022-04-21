from django.contrib import admin

from .models import *


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title', 'book_image', 'author', 'release_year', 'time_create')
    list_display_links = ('id', 'book_title')
    search_fields = ('book_title', 'author')


admin.site.register(Books, BooksAdmin)
