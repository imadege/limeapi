from  .models import Property, Booking
from  rest_framework import serializers

class PropertySerializers(serializers.ModelSerializer):

    """ Serializer to get and add property"""
    class Meta:
        model = Property
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """serializer booking details to json """
    class Meta:
        model = Booking
        fields = ('id', 'contact_person','price_per_day', 'price','checkin_date',
                  'checkout_date','property_booking','property_name')
        read_only_fields = ('property_name','price','price_per_day')

    def create(self, validated_data):
        """create booking """
        booking = Booking.objects.create(**validated_data)
        no_of_days = (booking.checkout_date - booking.checkin_date).days
        booking.price_per_day = booking.property_booking.price_per_day
        booking.price = round(float(booking.property_booking.price_per_day) * float(no_of_days), 2)
        booking.save()
        return booking