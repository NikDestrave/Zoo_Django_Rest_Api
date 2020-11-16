from django.urls import path

from zooapp import views

urlpatterns = [
    path('animals/', views.AnimalList.as_view()),
    path('animal/<int:pk>/', views.AnimalDetail.as_view()),
    path('animal/create/', views.AnimalCreate.as_view()),
    path('animal/<int:pk>/update/', views.AnimalUpdate.as_view()),
    path('animal/<int:pk>/delete/', views.AnimalDelete.as_view()),

    path('employees/', views.EmployeeList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('employee/create/', views.EmployeeCreate.as_view()),
    path('employee/<int:pk>/update/', views.EmployeeUpdate.as_view()),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view()),

    path('place/', views.PlaceList.as_view()),
    path('place/create/', views.EmployeeCreate.as_view()),
    path('place/<int:pk>/update/', views.EmployeeUpdate.as_view()),
    path('place/<int:pk>/delete/', views.EmployeeDelete.as_view()),
    path('placefilter/', views.PlaceFilterList.as_view()),
]
