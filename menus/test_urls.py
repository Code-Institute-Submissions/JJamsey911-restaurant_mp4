# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from menus.views import menu_food, menu_drink
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Test that the correct url for food and drinks page are used


class TestMenuUrls(SimpleTestCase):
    """
    This class is for testing the food
    and drink menu urls
    """
    def test_menu_food_resolved(self):
        url = reverse('menu_food')
        self.assertEquals(resolve(url).func, menu_food)

    def test_menu_drink_resolved(self):
        url = reverse('menu_drink')
        self.assertEquals(resolve(url).func, menu_drink)