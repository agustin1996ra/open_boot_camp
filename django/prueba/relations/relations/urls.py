from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one/', include('onetoone.urls')),
    path('manytoone/', include('manytoone.urls')),
    path('manytomany/', include('manytomany.urls'))
]
