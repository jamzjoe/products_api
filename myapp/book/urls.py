from rest_framework.urls import path

from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, BookListCreate, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]