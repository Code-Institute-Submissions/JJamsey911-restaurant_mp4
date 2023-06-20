# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from menu import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for the food and drinks menu
urlpatterns = [
    path('menu/food_menu', views.food_menu, name='food_menu'),
    path('menu/drink_menu', views.drink_menu, name='drink_menu'),
]