# Imports
from django.test import TestCase

from .models import FoodSelection, DrinkSelection


class TestModels(TestCase):

    def test_new_foods(self):
        food = FoodSelection.objects.create(
            name_food='Test Food',
            description='Test description',
            price='4.99',
            food_choice='2',
            )
        self.assertFalse(food.available)
        self.assertEqual(food.price, '4.99')
        self.assertEqual(food.description, 'Test description')
        self.assertEqual(food.food_choice, '2')

    def test_new_drinks(self):
        drink = DrinkSelection.objects.create(
            name_drink='Test drink',
            description='Test description',
            price='4.99',
            drink_choice= '2',
            )
        self.assertFalse(drink.available)
        self.assertEqual(drink.price, '4.99')
        self.assertEqual(drink.description, 'Test description')
        self.assertEqual(drink.drink_choice, '2')
