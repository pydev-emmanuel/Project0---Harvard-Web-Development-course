from django.urls import path
from . import views


urlpatterns = [
    path('', views.search, name="search"),
    path('image_search/', views.image_search, name="image_search"),
    path('advanced_search/', views.advanced_search, name="advanced_search"),
]
