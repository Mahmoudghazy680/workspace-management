from django.contrib import admin
from .models import reservation, room 
# Register your models here.

@admin.register(reservation)
class toolAdmin(admin.ModelAdmin):
    list_display = ["rev_id","customer", "check_in", "check_out", "room_number", "notes"]

@admin.register(room)
class toolAdmin(admin.ModelAdmin):
    list_display = ["room_name","room_status"]