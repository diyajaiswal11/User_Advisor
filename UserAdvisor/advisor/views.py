from django.shortcuts import render
from .models import *
from core.models import User
from .serializers import *
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class AdvisorCreateAPIView(generics.CreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = AdvisorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class AdvisorListAPIView(generics.ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AdvisorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class BookCallwithAdvisorAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def post(self,request,user,advisor):

        try:
            user_selected=User.objects.get(id=user)
        except ObjectDoesNotExist:
            return Response({"USER_DOES_NOT_EXIST":"User does not exist"},status=400)

        try:
            advisor_selected=Advisor.objects.get(id=advisor)
        except ObjectDoesNotExist:
            return Response({"ADVISOR_DOES_NOT_EXIST":"Advisor does not exist"},status=400)

        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user_selected,advisor=advisor_selected)

        return Response(serializer.data, status=200)



class GetAllBookedCallsAPIView(generics.ListAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    
    def list(self, request,user):

        try:
            user_selected=User.objects.get(id=user)
        except ObjectDoesNotExist:
            return Response({"USER_DOES_NOT_EXIST":"User does not exist"},status=400)


        bookings=user_selected.booking.all()
        serializer = BookingListSerializer(bookings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    