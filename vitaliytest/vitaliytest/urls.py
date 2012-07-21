from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vitaliytest.views.home', name='home'),
    # url(r'^vitaliytest/', include('vitaliytest.foo.urls')),

    url(r'^tinymce/', include('tinymce.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),



    url(r'^author/(\d+)/$', 'books.views.select_author', name="author_view"),
    url(r'^author_edit/(?P<author_id>\d+)/$','books.views.author_edit', name="author_edit"),
    url(r'^author_create/$','books.views.author_edit',{'author_id':None} ,name="author_create"),
        url(r'^author_delete/(\d+)/$', 'books.views.author_delete', name="author_delete"),
    url(r'^author/$','books.views.author'),



    url(r'^book/(\d+)/$', 'books.views.select_book', name="book_view"),
    url(r'^edit_book/(\d+)/$','books.views.edit_book', name="edit_book"),
    url(r'^create_book/$','books.views.edit_book',{'id':None}),
    url(r'^delete_book/(\d+)/$', 'books.views.delete_book', name="delete_book"),

    url(r'^$', 'books.views.index', name='home'),

)
urlpatterns += staticfiles_urlpatterns()
