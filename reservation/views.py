from django.shortcuts import render

# Create your views here.
def total(room_status, shared, private):
    if room_status == shared : 
        return (10)
    else :
        return (60)
    