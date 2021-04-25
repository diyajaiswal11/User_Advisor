from .views import *
from django.urls import path

urlpatterns = [
    path('admin/advisor/',AdvisorCreateAPIView.as_view(),name='advisor_create'),
]