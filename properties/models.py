from django.db import models
import uuid


class Property(models.Model):

    """
    Property Entity
    NB: Some fields might be missing for now, but just need to capture lat, long for now
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=6)
    longitude = models.DecimalField(max_digits=20, decimal_places=6)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
     Booking Entity
     NB: Some fields might be missing for now, but just need to capture lat, long for now
     """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_person = models.CharField(max_length=100)
    property_booking = models.ForeignKey(Property, related_name='book_property')
    price_per_day = models.DecimalField(decimal_places=2, max_digits=9, default=0.00)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    checkin_date = models.DateField(blank=False)
    checkout_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def property_name(self):
        return self.property_booking.name