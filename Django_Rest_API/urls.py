from django.contrib import admin
from django.urls import path, include

import zooapp.views as zooapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('zooapp.urls')),
    path('', zooapp.main, name='main'),
]
