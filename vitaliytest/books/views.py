from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from books.models import Author,Book, AuthorForm, BookForm

@login_required
def index(request):
    book_all = Book.objects.prefetch_related('author')
    return render_to_response('books/index.html', {'books_all':book_all, 'class_name':'home-page'}, context_instance=RequestContext(request))

@login_required
def author(request):
    author_all = Author.objects.all()
    return render_to_response('books/author.html',{'authors':author_all, 'class_name':'author-home'})

@login_required
def select_author(request, id):
    ref_page = request.META['HTTP_REFERER']
    selected_author = get_object_or_404(Author, pk=id)
    books_author = selected_author.book_set.all()
    return render_to_response('books/page_author.html',{'select_author':selected_author,'books_author':books_author, 'author_id':id, 'ref_page':ref_page}, context_instance=RequestContext(request))

@login_required
def edit_book(request,id):
    ref_page = request.META['HTTP_REFERER']
    if id is None:
        book = None
        create_message = 'Book success create!'
    else:
        book = Book.objects.get(pk=id)
        create_message = 'Book success update!'

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            instance_form = form.save()
            messages.success(request, create_message)
            if id is None:
                return redirect(reverse('edit_book',args=[instance_form.id]))
    else:
        form =  BookForm(instance=book)

    return render_to_response('books/edit_book.html',{'form':form,'id':id,'class_name':'edit-book','ref_page':ref_page}, context_instance=RequestContext(request))

@login_required
def delete_book(request,id):
    selected_author = get_object_or_404(Book, pk=id)
    selected_author.delete()
    return redirect(reverse('home_page'))

@login_required
def select_book(request):
    pass

@login_required
def author_edit(request,author_id):
    if author_id is None:
        selected_author = None
        create_message = 'Author success create!'
    else:
        selected_author = get_object_or_404(Author, pk=author_id)
        create_message = 'Author success edit!'

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=selected_author)
        if form.is_valid():
            instance_form = form.save()
            messages.success(request,create_message)
            if author_id is None:
                return redirect(reverse('author_view', args=[instance_form.id]))
    else:
        form = AuthorForm(instance=selected_author)
    return render_to_response('books/author_edit.html',{'form':form,'author_id':author_id}, context_instance=RequestContext(request))

@login_required
def author_delete(request,id):
    selected_author = get_object_or_404(Author, pk=id)
    selected_author.delete()
    Book.objects.filter(author__pk__isnull = True).delete()
    return redirect(reverse('home_page'))