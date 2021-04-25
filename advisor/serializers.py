from . import models
from rest_framework import serializers

class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Advisor
        fields='__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Booking
        fields=('booking_time',)



class BookingListSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Booking
        fields=('booking_time','advisor','id',)
        depth=2