from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.timezone import  now

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

class DBHistory(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    add_date = models.DateTimeField(null=True,blank=True)
    change_date = models.DateTimeField(null=True,blank=True)
    delete_date = models.DateTimeField(null=True,blank=True)

@receiver(post_save, sender=Author)
def author_save(sender, **kwargs):
    created = kwargs.get('created',None)
    instance = kwargs.get('instance',None)
    if created:
        DBHistory.objects.create(content_object=instance,add_date = now())
    else:
        DBHistory.objects.create(content_object=instance,change_date = now())

@receiver(pre_delete, sender=Author)
def author_delete(sender, **kwargs):
    instance = kwargs.get('instance',None)
    DBHistory.objects.create(content_object=instance,delete_date = now())

@receiver(post_save, sender=Book)
def book_save(sender, **kwargs):
    created = kwargs.get('created',None)
    instance = kwargs.get('instance',None)
    if created:
        DBHistory.objects.create(content_object=instance,add_date = now())
    else:
        DBHistory.objects.create(content_object=instance,change_date = now())


@receiver(pre_delete, sender=Book)
def book_delete(sender, **kwargs):
    instance = kwargs.get('instance',None)
    DBHistory.objects.create(content_object=instance,delete_date = now())

