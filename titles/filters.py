import django_filters
from django_filters import rest_framework as filters

from .models import Title


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name='genre__slug', lookup_expr='iexact'
    )
    category = django_filters.CharFilter(
        field_name='category__slug', lookup_expr='iexact'
    )
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = ['genre', 'category', 'year', 'name']
