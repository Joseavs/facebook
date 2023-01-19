from django.contrib import admin
from django.urls import path
from websites import views
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='home'),
	path('alerta/de/seguridad/', views.facef, name='facef'),
	path('enlaces/', views.enlaces, name='enlaces'),
	path('nuevo/video/porno/salma/', views.salma, name='salma'),
]
