from django.db import models
from core.models import User

class Advisor(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='advisor/photo/')

    def __str__(self):
        return self.name


class Booking(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='booking') 
    booking_time=models.DateTimeField()
    advisor=models.ForeignKey(Advisor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.name) + " " + str(self.advisor.name) 