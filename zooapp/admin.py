from django.contrib import admin

from zooapp import models

admin.site.register(models.Animal)
admin.site.register(models.Employee)
admin.site.register(models.TypeOfAnimal)
admin.site.register(models.Place)
admin.site.register(models.Family)
admin.site.register(models.Genus)
admin.site.register(models.Subspecies)
admin.site.register(models.AnimalToEmployee)
