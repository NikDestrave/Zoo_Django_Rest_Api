from collections import Counter

from rest_framework import serializers

from zooapp.models import Animal, Place, Employee, AnimalToEmployee


class MainSerializer(serializers.ModelSerializer):
    """Вывод списка животных"""
    class Meta:
        model = Animal
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    """Вывод списка сотрудников"""
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Employee
        exclude = ['updated_at', 'is_active']


class AnimalSerializer(serializers.ModelSerializer):
    """Вывод списка животных с использованием параметров фильтрации."""
    gender = serializers.CharField(source='get_gender_display')
    subspecies = serializers.SlugRelatedField(slug_field='subspecies_name', read_only=True)
    place = serializers.SlugRelatedField(slug_field='place_name', read_only=True)
    place_square = serializers.SlugRelatedField(slug_field='place_square', read_only=True)
    employee = EmployeesSerializer(many=True)

    class Meta:
        model = Animal
        fields = '__all__'


class AnimalEmployeeSerializer(serializers.ModelSerializer):
    """Связь многие ко многим. Животное - сотрудник."""
    animal = MainSerializer()
    employee = EmployeesSerializer()

    class Meta:
        model = AnimalToEmployee
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
    """Вывод мест нахождения животных."""
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
    """Вывод мест нахождения животных."""
    class Meta:
        model = Place
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Вывод списка сотрудников"""
    class Meta:
        model = Employee
        fields = '__all__'
