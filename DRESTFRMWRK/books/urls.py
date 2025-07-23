from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet, book_create

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', book_list )
    path('books/<int:pk>/', book_create())
    path('books/add', book_create())
    path('books/edit/<int:pk>/', book_)
]