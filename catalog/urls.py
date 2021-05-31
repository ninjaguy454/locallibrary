from django.http import Http404
from django.shortcuts import render
from django.urls import path

from catalog import views
from catalog.models import Book, Author

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'catalog/book_detail.html', context={'book': book})

def author_detail_view(request, primary_key):
    try:
        author = Author.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Author does not exist')

    return render(request, 'catalog/author_detail.html', context={'author': author})

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]