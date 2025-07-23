from django.urls import path

from booksmgmt import views

urlpatterns = [
    path('',views.book_list, name='book_list'),

]