# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodSelection, DrinkSelection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Registration of the food items for the admin panel,
# display and search filters
@admin.register(FoodSelection)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('name_food', 'food_choice', 'price', 'available')
    search_fields = ('name_food', 'description')
    list_filter = ('available', 'food_choice')
    summernote_fields = ('description')


# Registration of the drinks items for the admin panel,
# display and search filters
@admin.register(DrinkSelection)
class DrinkAdmin(SummernoteModelAdmin):
    list_display = ('name_drink', 'drink_choice', 'price', 'available')
    search_fields = ('name_drink', 'description')
    list_filter = ('available', 'drink_choice')
    summernote_fields = ('description')