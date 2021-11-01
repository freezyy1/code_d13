from django_filters import FilterSet, CharFilter
from .models import Advert


class AdvertFilter(FilterSet):
    class Meta:
        model = Advert
        fields = ('adv_name', 'created', 'category', 'content')

