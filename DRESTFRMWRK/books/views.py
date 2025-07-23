#------------CBV-------------------
# from django.shortcuts import render
# from django.views import View
# from rest_framework import viewsets
#
# from books.models import Book
# from books.serializers import BookSerializer
#
#
# # Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# ========================================================================================

#--------------FBV---------------------
from rest_framework import status, request
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def book_list(request):
    # if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH', 'DELETE'])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'PATCH':
    #     serializer = BookSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

