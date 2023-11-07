from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
RoomStatus = [
                ('Shared','Shared'),
                ('Private','Private'),

        ]

class room(models.Model):
    room_name     = models.CharField(max_length=50)
    room_status   = models.CharField(max_length=50, null=True, blank=True, choices=RoomStatus)

    class Meta:
        verbose_name = _("Rooms")
        verbose_name_plural = _('Rooms')
 
    def __str__(self):
        return self.room_name



class reservation(models.Model):
    rev_id      = models.AutoField(primary_key=True)
    customer    = models.ForeignKey(User, verbose_name = ("Customer Name "), on_delete=models.CASCADE)
    user_phone  = models.CharField(max_length=50, null=True, blank=True, verbose_name = ("Customer Phone "))
    user_email  = models.EmailField(max_length=254,null=True, blank=True,  verbose_name = ("Customer E-mail "))
    check_in    = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name = ("Check in "))
    check_out   = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False, verbose_name = ("Check out "))
    room_number = models.ForeignKey(room, on_delete=models.CASCADE, verbose_name = ("Room Number "))
    status      = models.CharField(max_length=50, null=True, blank=True, choices=RoomStatus)
    custumers_numbers =  models.IntegerField(default=1)
    price       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = ("Cost "))
    # table_number= models.CharField(max_length=50, null=True, blank=True)      To be add in Version 2
    total_1= models.CharField(max_length=50, null=True, blank=True, verbose_name = ("Total "))
    # buffet= models.CharField(max_length=50, null=True, blank=True)            To be add in Version 2
    notes       = models.TextField(null=True, blank=True, )



    class Meta:
        verbose_name = _("reservation")
        verbose_name_plural =  _('reservation')
 
    # def __str__(self):
    #     return self.customer
