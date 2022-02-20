from django.contrib import admin
from .models import Booking, Payment, PaymentType,Room,RoomStatus,RoomType,Receptionist,User
# Register your models here.
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(PaymentType)
admin.site.register(Room)
admin.site.register(RoomStatus)
admin.site.register(RoomType)
admin.site.register(Receptionist)
admin.site.register(User)