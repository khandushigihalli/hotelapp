from django.contrib import admin
# Register your models here.
from .models import Room,Menu,Food,Order,Starters
# Register your models here.
admin.site.register(Room)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Starters)