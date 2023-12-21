from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('', include('home.urls')),
]
