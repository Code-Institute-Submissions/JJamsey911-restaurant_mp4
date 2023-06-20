# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from menus import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for the food and drinks menu
urlpatterns = [
    path('menus/menu_food', views.menu_food, name='menu_food'),
    path('menus/menu_drink', views.menu_drink, name='menu_drink'),
]