from collections import Counter

from rest_framework import serializers

from zooapp.models import Animal, Place, Employee


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    """Вывод списка животных с использованием параметров фильтрации.
    http://127.0.0.1:8000/api/animals/?age_min=&employee_date_after=&&place__place_name=&&place= ...
    Несколько из принимаемых параметров:
        age_min - минимальный возраст
        age_max - максимальный возраст
        employee_date_after = дата закрепления животного за сотрудником (от)
        place - место нахождения животного
        place_square - площадь места
        subspecies - вид животного
    """
    gender = serializers.CharField(source='get_gender_display')
    subspecies = serializers.SlugRelatedField(slug_field='subspecies_name', read_only=True)
    place = serializers.SlugRelatedField(slug_field='place_name', read_only=True)
    place_square = serializers.SlugRelatedField(slug_field='place_square', read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'


class AnimalDetailSerializer(serializers.ModelSerializer):
    """Детальный вывод данных о животном"""
    animal_type = serializers.SlugRelatedField(slug_field='animal_type', read_only=True)
    family = serializers.SlugRelatedField(slug_field='family_name', read_only=True)
    genus = serializers.SlugRelatedField(slug_field='genus_name', read_only=True)
    subspecies = serializers.SlugRelatedField(slug_field='subspecies_name', read_only=True)
    place = serializers.SlugRelatedField(slug_field='place_name', read_only=True)
    employee = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Animal
        fields = '__all__'


class PlaceFilterSerializer(serializers.ModelSerializer):
    """Вывод мест нахождения животных.
    dcount - переменная для запуска метода get и вывода итогов в объекты
    """
    dcount = serializers.SerializerMethodField('get')

    class Meta:
        model = Place
        fields = '__all__'

    """Метод для расчета количества уникальных отрядов животных для каждого места"""

    def get(self, obj):
        squads = []
        for e in Animal.objects.all():
            if e.place.id == obj.id:
                squads.append(e.animal_type.animal_type)
        result_place = len(Counter(squads))
        return result_place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
