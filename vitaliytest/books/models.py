from django.db import models
from django.forms import ModelForm
from django.conf import settings

from tinymce.widgets import TinyMCE

# Create your models here.
class Author(models.Model):
    FIO = models.CharField(max_length=255)
    birthday = models.DateField('data birthday')
    dieday = models.DateField('data died',null=True, blank=True)

    def __unicode__(self):
        return self.FIO

    @models.permalink
    def get_absolute_url(self):
        return ('author_view', [str(self.id)])

class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    yearbook = models.DateField('year publish')
    short_describe = models.TextField(max_length=500)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('book_view', [str(self.id)])


class AuthorForm(ModelForm):
    class Meta:
        model = Author

class BookForm(ModelForm):
    class Meta:
        model=Book
        widgets = {
            'short_describe': TinyMCE(attrs={'cols': 80, 'rows': 20}, mce_attrs= settings.TINYMCE_DEFAULT_CONFIG)
        }
