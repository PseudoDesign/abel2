from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('', views.regions, name='items'),
    path('region', views.regions, name="regions"),
    path('regions/<int:region_id>', views.region, name="region"),
    path('constellations/<int:constellation_id>', views.constellation, name="constellation"),
    path('systems/<int:system_id>', views.system, name="system"),
    path("stations/<int:station_id>", views.station, name="station")
]