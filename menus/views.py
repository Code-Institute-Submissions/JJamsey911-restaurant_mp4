# Imports
from django.shortcuts import render
from .models import FoodSelection, DrinkSelection


def menu_food(request):
    """
    a view to display the food menu
    """
    list_food = FoodSelection.objects.all()
    return render(
        request, 'menus/menu_food.html', {'list_food': list_food})


def menu_drink(request):
    """
    a view to display the drinks menu
    """
    list_drink = DrinkSelection.objects.all()
    return render(
        request, 'menus/menu_drink.html', {'list_drink': list_drink})