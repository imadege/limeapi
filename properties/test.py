#from django.urls import reverse, resolve

from rest_framework.test import APITestCase
from properties.models import Property
from properties.serializers import *

class PropertyTests(APITestCase):

    def setUp(self):
        self.properyattributes = {
            "name": "property one",
            "latitude": "122.454350",
            "longitude": "123.343420",
            "price_per_day": "3424.00"
        }

        self.property = Property.objects.create(**self.properyattributes)
        self.serializer = PropertySerializers(instance=self.property)

    def test_property_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.properyattributes.get('name'))

    def test_latitude_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['latitude'], self.properyattributes.get('latitude'))

    def test_longitude_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['longitude'], self.properyattributes.get('longitude'))


class BookingTest(APITestCase):

    def setUp(self):
        self.properyattributes = {
            "name": "property one",
            "latitude": "122.454350",
            "longitude": "123.343420",
            "price_per_day": "3424.00"
        }

        self.property = Property.objects.create(**self.properyattributes)

        self.bookingattributes = {
            "contact_person": "Ian Madege",
            "checkin_date": "2020-02-28",
            "checkout_date": "2020-02-29",
            "property_booking": self.property,
        }

        self.booking = Booking.objects.create(**self.bookingattributes)
        self.serializer = BookingSerializer(instance= self.booking)

    def test_booking_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['contact_person'], self.bookingattributes.get('contact_person'))
