# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodSelection, DrinkSelection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def menu_food(request):
    """
    a view to display the food menu
    """
    list_food = FoodSelection.objects.all()
    return render(
        request, 'menu/menu_food.html', {'list_food': list_food})


def menu_drink(request):
    """
    a view to display the drinks menu
    """
    list_drink = DrinkSelection.objects.all()
    return render(
        request, 'menu/drink_menu.html', {'list_drink': list_drink})