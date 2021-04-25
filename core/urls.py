from django.urls import path
from .views import *
from advisor.views import *


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('<int:id>/advisor/', AdvisorListAPIView.as_view(), name='advisor_create'),
    path('<int:user>/advisor/<int:advisor>/', BookCallwithAdvisorAPIView.as_view(), name='advisor_book'),
    path('<int:user>/advisor/booking/', GetAllBookedCallsAPIView.as_view(), name='booking_list'),
]