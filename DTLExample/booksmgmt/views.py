from django.shortcuts import render

# Create your views here.
def book_list(request):
    books = [
        {"title": "C pgm", "author": "ABC", "available": False},
        {"title": "C++ pgm", "author": "XYZ", "available": True},
        {"title": "Java pgm", "author": "MNO", "available": False},
        {"title": "Python", "author": "DEF", "available": True},
    ]

    return render(request, 'booksmgmt/base.html', {'books': books})