from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters.rest_framework import DateFromToRangeFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['title', 'created_at', 'status']
