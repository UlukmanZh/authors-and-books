from django.shortcuts import render, redirect
from .models import Book, Author

def index (request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, "index.html", context)

def add_book (request):
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['desc'],
    )
    return redirect('/')

def book_view (request, book_id):
    choosen_book = Book.objects.get(id=book_id)
    authors_exclude = Author.objects.exclude(books__id=choosen_book.id)
    context = {
        'book': choosen_book,
        'all_authors': authors_exclude,
    }
    return render(request, "book_view.html", context)

def authors (request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, "authors.html", context)

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def author_view(request, author_id):
    choosen_author = Author.objects.get(id=author_id)
    books_exclude = Book.objects.exclude(authors__id=choosen_author.id)
    context = {
        'author': choosen_author,
        'all_books': books_exclude,
    }
    return render(request, "author_view.html", context)

def author_to_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    return redirect(f'/books/{book_id}')

def book_to_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author.books.add(this_book)
    return redirect(f'/author/{author_id}')

def delete_book(request, book_id):
    choosen_book = Book.objects.get(id=book_id)
    choosen_book.delete()
    return redirect('/')

def delete_author(request, author_id):
    choosen_author = Author.objects.get(id=author_id)
    choosen_author.delete()
    return redirect('/authors')