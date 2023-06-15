from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from book.serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework.permissions import IsAuthenticated
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
@permission_classes([IsAuthenticated])
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@permission_classes([IsAuthenticated])
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():
            book = serializer.save()
            author = Author.objects.get(id=book.author_id)
            author_serializer = AuthorSerializer(author)
            response_data = {
                'book': serializer.data,
                'author': author_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([IsAuthenticated])
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer