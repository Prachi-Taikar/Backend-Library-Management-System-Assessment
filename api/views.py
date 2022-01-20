from django.shortcuts import render, HttpResponse
from .models import Book
from .serializers import BookSerializer, UserSerializer
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




"""
#class based View
class BookList(APIView):
    
    def get(self, request):
        books = Book.objects.all()
        serializer =BookSerializer(books, many = True)

        return Response(serializer.data)

    def post (self, request):
        serializer =BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id = id)

        except Book.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        book = self.get_object(id)
        serializer =BookSerializer(book)

        return Response(serializer.data)

    def put(self, request, id):
        book = self.get_object(id)
        serializer = BookSerializer(book, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = self.get_object(id)
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""
"""

# function based API_VIEW

@api_view(['GET', 'POST'])
def book_list(request):
    
    if request.method == "GET" :
        books = Book.objects.all()
        serializer =BookSerializer(books, many = True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer =BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request,pk):
    try:
        book = Book.objects.get(pk = pk)

    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

"""