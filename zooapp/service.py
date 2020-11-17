from django_filters import rest_framework as filters

from zooapp.models import Animal, Place, AnimalToEmployee


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AnimalFilter(filters.FilterSet):
    """Фильтрация модели Animal.
    http://127.0.0.1:8000/api/animals/?age_min=&employee_date_after=&&place__place_name=&&place= ...
    Несколько из принимаемых параметров:
        age_min - минимальный возраст
        age_max - максимальный возраст
        employee_date_after = дата закрепления животного за сотрудником (от)
        place - место нахождения животного
        place_square - площадь места
    """
    age = filters.RangeFilter()
    employee_date = filters.DateFromToRangeFilter()
    place = CharFilterInFilter(field_name='place__place_name', lookup_expr='in')

    class Meta:
        model = Animal
        fields = ['age', 'employee_date', 'place__place_name', 'place__square']


class PlaceFilter(filters.FilterSet):
    """Вывод мест нахождения животных.
        dcount - переменная для запуска метода get и вывода итогов в объекты
    """
    dcount = filters.RangeFilter(label='dcount')

    class Meta:
        model = Place
        fields = ['dcount']


class AnimalToEmployeeFilter(filters.FilterSet):
    """Фильтрация связей по дате создания"""
    created = filters.DateFromToRangeFilter()

    class Meta:
        model = AnimalToEmployee
        fields = ['created', 'animal__gender', 'employee']
