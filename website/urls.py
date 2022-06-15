from django.urls import path,include
from website import views
from django.contrib import admin

app_name = "webisite"

urlpatterns = [
        path('absorption/',views.absorption,name='absorption'),
        path('elongation/',views.elongation,name='elongation'),
        path('tensile/',views.tensile,name='tensile'),
        path('vickers/',views.vickers,name='vickers'),
        path('wearloss/',views.wearloss,name='wearloss'),
        path('youngs/',views.youngs,name='youngs'),
]
