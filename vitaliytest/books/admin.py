from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from tinymce.widgets import TinyMCE

from books.models import Book, Author
from books.form import UserCreateForm, CustomUserChangeForm

class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ['author']
    list_filter = ['author']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20, }, )},
        }

class UserAdmin(UserAdmin):
    add_form  = UserCreateForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (None, {'fields':('username','email','password1','password2',),}),)




admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)