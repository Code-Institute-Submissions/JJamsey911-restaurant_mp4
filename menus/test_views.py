# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase, Client
from django.urls import reverse



# Test that the correct views are used for food and drinks menu


class TestMenusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_food_url = reverse('menu_food')
        self.menu_drink_url = reverse('menu_drink')

    def test_menu_food_GET(self):
        response = self.client.get(self.menu_food_url)

        self.assertEqual(response.status_code, 200)

    def test_menu_drink_GET(self):
        response = self.client.get(self.menu_drink_url)

        self.assertEqual(response.status_code, 200)