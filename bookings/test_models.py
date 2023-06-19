# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from datetime import date

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Booking, User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# These test will create a new food and drink item,
# it will check the name, description and price


class TestModels(TestCase):
    def setUp(self):
        self.user = User(username="Testing", email="test@email.com")
        self.booking = Booking(
            booking_id=14,
            user=self.user,
            guest_count= 3,
            date_created="2023-12-12",
            date_requested="2023-12-12",
            time_requested="14:00",
            status="awaiting confirmation",
            name="Testing",
            phone="+353123456789",
            email="test@email.com",
        )

    def test_create_booking(self):
        self.assertEqual(self.booking.name, "Testing")
        self.assertEqual(self.booking.booking_id, 14)
        self.assertEqual(self.booking.date_requested, "2023-12-12")
        self.assertEqual(self.booking.time_requested, "10:00")
        self.assertEqual(self.booking.guest_count, 3)
        self.assertEqual(self.booking.status, "awaiting confirmation")
        self.assertEqual(self.booking.name, "Testing")
        self.assertEqual(self.booking.phone, "+353123456789")
        self.assertEqual(self.booking.email, "test@email.com")
