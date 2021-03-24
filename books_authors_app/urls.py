from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.book_view),
    path('authors',views.authors),
    path('add_author', views.add_author),
    path('author/<int:author_id>', views.author_view),
    path('author_to_book/<int:book_id>', views.author_to_book),
    path('book_to_author/<int:author_id>',views.book_to_author),
    path('delete/<int:book_id>',views.delete_book),
    path('delete_author/<int:author_id>',views.delete_author)
]