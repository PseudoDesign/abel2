from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.items, name='items'),
    path('region', views.regions, name="regions"),
    path('region/<int:region_id>', views.regions, name="region"),
]