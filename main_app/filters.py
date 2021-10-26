from django_filters import FilterSet, CharFilter
from .models import Advert


class AdvertFilter(FilterSet):
    announcer__announcer = CharFilter(lookup_expr='icontains')
    category__cat_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Advert
        fields = ('adv_name', 'created', 'category', 'content')

