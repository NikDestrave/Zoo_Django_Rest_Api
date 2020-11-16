from django_filters import rest_framework as filters

from zooapp.models import Animal, Place


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimalFilter(filters.FilterSet):
    age = filters.RangeFilter()
    employee_date = filters.DateFromToRangeFilter()
    place = CharFilterInFilter(field_name='place__place_name', lookup_expr='in')

    class Meta:
        model = Animal
        fields = ['age', 'employee_date', 'place__place_name', 'place__square']


class PlaceFilter(filters.FilterSet):
    dcount = filters.RangeFilter(label='dcount')

    class Meta:
        model = Place
        fields = ['dcount']
