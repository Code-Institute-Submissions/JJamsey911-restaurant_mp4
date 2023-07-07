# Bookings model Tests
from django.test import TestCase
from datetime import date

from .models import Booking, User


class TestModels(TestCase):
    def setUp(self):
        self.user = User(username="Tester", email="test@mail.com")
        self.booking = Booking(
            booking_id=32,
            user=self.user,
            guest_count=6,
            created_date="2023-06-05",
            requested_date="2023-06-15",
            requested_time="12:00",
            status="awaiting confirmation",
            name="Tester",
            phone="+353123456789",
            email="test@mail.com",
        )

    def test_create_booking(self):
        self.assertEqual(self.booking.name, "Tester")
        self.assertEqual(self.booking.booking_id, 32)
        self.assertEqual(self.booking.requested_date, "2023-06-15")
        self.assertEqual(self.booking.created_date, "2023-06-05")
        self.assertEqual(self.booking.requested_time, "12:00")
        self.assertEqual(self.booking.guest_count, 6)
        self.assertEqual(self.booking.status, "awaiting confirmation")
        self.assertEqual(self.booking.name, "Tester")
        self.assertEqual(self.booking.phone, "+353123456789")
        self.assertEqual(self.booking.email, "test@mail.com")
