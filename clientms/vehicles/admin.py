from django.contrib import admin

from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle


admin.site.register(Vehicle, VehicleAdmin)
