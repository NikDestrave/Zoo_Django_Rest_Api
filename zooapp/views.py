from django.db.models import Value, PositiveIntegerField, Count
from django.shortcuts import render
from rest_framework import generics

from zooapp.models import Animal, Place, Employee, Family, Genus, AnimalToEmployee
from zooapp.serializers import AnimalSerializer, PlaceSerializer, EmployeeSerializer, PlaceFilterSerializer, \
    MainSerializer, EmployeesSerializer, AnimalEmployeeSerializer
from zooapp.service import AnimalFilter, PlaceFilter, AnimalToEmployeeFilter


def main(request):
    """Передача моделей из базы в шаблон"""
    animals = Animal.objects.all()
    employee = Employee.objects.all()
    family = Family.objects.all()
    genus = Genus.objects.all()
    animals_employee = AnimalToEmployee.objects.all()

    content = {
        'employee': employee,
        'family': family,
        'genus': genus,
        'animals': animals,
        'animals_employee': animals_employee
    }

    return render(request, 'zooapp/base.html', content)


class AnimalList(generics.ListAPIView):
    """Вывод животных c сортировкой по названию отряда"""
    queryset = Animal.objects.all().order_by('subspecies__subspecies_name')
    serializer_class = AnimalSerializer
    filterset_class = AnimalFilter


class PlaceFilterList(generics.ListAPIView):
    """Вывод мест в зоопарке"""
    queryset = Place.objects.annotate(dcount=Value(0, output_field=PositiveIntegerField()))
    serializer_class = PlaceFilterSerializer
    filterset_class = PlaceFilter


class AnimalDetail(generics.RetrieveAPIView):
    """Вывод детальной информации одного животного"""
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalCreate(generics.CreateAPIView):
    """Добавление нового животного"""
    queryset = Animal.objects.all()
    serializer_class = MainSerializer


class AnimalUpdate(generics.RetrieveUpdateAPIView):
    """Обновление информации о животном"""
    queryset = Animal.objects.all()
    serializer_class = MainSerializer


class AnimalDelete(generics.DestroyAPIView):
    """Удаление животного"""
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class EmployeeList(generics.ListAPIView):
    """Вывод сотрудников"""
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer


class EmployeeDetail(generics.RetrieveAPIView):
    """Вывод детальной информации одного сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    """Добавление нового сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    """Обновление информации о сотруднике"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDelete(generics.DestroyAPIView):
    """Удаление сотрудника"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PlaceList(generics.ListAPIView):
    """Вывод мест нахождения животных"""
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceCreate(generics.CreateAPIView):
    """Добавление нового места"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PlaceUpdate(generics.RetrieveUpdateAPIView):
    """Обновление информации о месте"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class PlaceDelete(generics.DestroyAPIView):
    """Удаление места"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AnimalsToEmployees(generics.ListAPIView):
    """Вывод связей для моделей Animal и Employee"""
    queryset = AnimalToEmployee.objects.all()
    serializer_class = AnimalEmployeeSerializer
    filterset_class = AnimalToEmployeeFilter
