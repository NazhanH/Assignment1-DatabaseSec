import django_filters

from django_filters import CharFilter

from .models import *

class BookFilter(django_filters.FilterSet):

    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    publication = CharFilter(field_name='publication', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication', 'year']