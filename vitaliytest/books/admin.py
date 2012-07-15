from django.contrib import admin
from books.models import Book, Author
from django.db import models

from tinymce.widgets import TinyMCE

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ['author']
    list_filter = ['author']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20, }, )},
        }

admin.site.register(Book, BookAdmin)
admin.site.register(Author)