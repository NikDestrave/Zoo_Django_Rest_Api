from datetime import date

from django.db import models


class TypeOfAnimal(models.Model):
    animal_type = models.CharField(verbose_name='Название', max_length=64)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'отряд'
        verbose_name_plural = 'отряды'

    def __str__(self):
        return self.animal_type


class Place(models.Model):
    place_name = models.CharField(verbose_name='Название', max_length=64)
    square = models.DecimalField(verbose_name='Площадь', max_digits=4, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'место нахождения'
        verbose_name_plural = 'места нахождения'

    def __str__(self):
        return f'{self.place_name} ({self.square} кв.м.)'


# Дополнительные справочники

class Family(models.Model):
    family_name = models.CharField(verbose_name='Название', max_length=64)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'семейство'
        verbose_name_plural = 'семейства'

    def __str__(self):
        return self.family_name


class Genus(models.Model):
    genus_name = models.CharField(verbose_name='Название', max_length=64)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'род'
        verbose_name_plural = 'род'

    def __str__(self):
        return self.genus_name


class Subspecies(models.Model):
    subspecies_name = models.CharField(verbose_name='Название', max_length=64)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'вид'
        verbose_name_plural = 'виды'

    def __str__(self):
        return self.subspecies_name


# Модель сотрудников

class Employee(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    gender = models.CharField(max_length=1, verbose_name='Пол', blank=True, choices=GENDER_CHOICES)
    position = models.CharField(verbose_name='Должность', max_length=64)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'работники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Модель животных

class Animal(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    name = models.CharField(verbose_name='Название', max_length=64)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    gender = models.CharField(max_length=1, verbose_name='Пол', blank=True, choices=GENDER_CHOICES)
    animal_type = models.ForeignKey(TypeOfAnimal, verbose_name='Отряд', on_delete=models.CASCADE)
    family = models.ForeignKey(Family, verbose_name='Семейство', on_delete=models.CASCADE)
    genus = models.ForeignKey(Genus, verbose_name='Род', on_delete=models.CASCADE)
    subspecies = models.ForeignKey(Subspecies, verbose_name='Вид', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    place = models.ForeignKey(Place, verbose_name='Место нахождения', on_delete=models.CASCADE)
    employee = models.ManyToManyField(Employee, verbose_name='Работники', through='AnimalToEmployee')
    employee_date = models.DateField(verbose_name='Дата закрепления', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.was_employee = self.employee

    def save(self, *args, **kwargs):
        if self.employee != self.was_employee:
            self.employee_date = date.today()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'животное'
        verbose_name_plural = 'животные'

    def __str__(self):
        return f'{self.subspecies} ({self.family})'


class AnimalToEmployee(models.Model):
    animal = models.ForeignKey(Animal, verbose_name='Животное', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    created = models.DateField(verbose_name='Создан')

    class Meta:
        verbose_name = 'связь жив. с сотр.'
        verbose_name_plural = 'связи жив. с сотр.'

    def __str__(self):
        return f'{self.animal} - {self.employee}'
