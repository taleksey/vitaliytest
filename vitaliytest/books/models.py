from django.db import models

# Create your models here.
class Author(models.Model):
    FIO = models.CharField('max_length=255')
    birthday = models.DateField('data birthday')
    dieday = models.DateField('data died',blank=True)

    def __unicode__(self):
        return self.FIO

class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField('max_length=100')
    yearbook = models.DateField('year publish')
    short_describe = models.CharField('max_length=255')

    def __unicode__(self):
        return self.title
