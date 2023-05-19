from django.contrib import admin
from .models import HotelModel
# Register your models here.


@admin.register(HotelModel)
class HotelModelAdmin(admin.ModelAdmin):
    list_display = ("pic", "name","id")[::-1]
