from dataclasses import fields
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ 'pk','title','description','num_pages', 'price','publication_date','isbn13']
        extra_kwargs = {
            'publication_date':{'required': False},
            'price':{'required': False},
            'isbn13':{'required': False},
        }