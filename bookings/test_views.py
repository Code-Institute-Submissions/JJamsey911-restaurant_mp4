# Bookings Views Test
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase, Client
from django.urls import reverse


# test that the correct views are used when requested


class TestBookingsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.reservations_url = reverse("reservations")
        self.confirmed_url = reverse("confirmed")
        self.edit_booking_url = reverse("booking_list")

    def test_reservations_GET(self):
        response = self.client.get(self.reservations_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/reservations.html")

    def test_confirmed_GET(self):
        response = self.client.get(self.confirmed_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/confirmed.html")

    # def test_booking_list_GET(self):
    #     response = self.client.get(self.booking_list_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "bookings/booking_list.html")

