from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .serializers import PropertySerializers, BookingSerializer
from .models import Property, Booking
import math
from django.db.models.expressions import RawSQL


class MixinDistance:

    def distance(origin_destination, destination):
        lat1, lon1 = origin_destination
        lat2, lon2 = destination
        radius = 6371  # km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c
        return d

    def get_locations_nearby_coords(self, latitude, longitude, max_distance=None):
        """
        Return objects sorted by distance to specified coordinates
        which distance is less than max_distance given in kilometers
        """
        # Great circle distance formula
        gcd_formula = "6371 * acos(least(greatest(\
        cos(radians(%s)) * cos(radians(latitude)) \
        * cos(radians(longitude) - radians(%s)) + \
        sin(radians(%s)) * sin(radians(latitude)) \
        , -1), 1))"
        distance_raw_sql = RawSQL(
            gcd_formula,
            (latitude, longitude, latitude)
        )
        qs = Property.objects.all().annotate(distance=distance_raw_sql).order_by('distance')

        if max_distance is not None:
            qs = qs.filter(distance__lte=max_distance)
        return qs


class PropertyView(MixinDistance, viewsets.ModelViewSet):
    serializer_class = PropertySerializers
    distance = 20

    def get_queryset(self):
        point = None
        properties = Property.objects.filter()
        if 'at' in self.request.query_params:
            point = self.request.query_params.get('at', None)
        if 'distance' in self.request.query_params:
            self.distance = self.request.query_params.get('distance', None)
        if point is not None:
            try:
                lat, lng = point.split(',')
                self.distance = self.distance * 1000
                return self.get_locations_nearby_coords(lat, lng, self.distance)
            except Exception as e:
                return properties
        return properties

    @detail_route(methods=['GET'], )
    def bookings(self, request, pk=None):
        if pk is None:
            return Response({'error': 'Missing property iD'}, 400)
        bookings = Booking.objects.filter(property_booking=pk)
        serialzer = BookingSerializer(bookings, many=True)
        return Response(serialzer.data, 200)


class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
