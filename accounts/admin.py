from django.contrib import admin
from .models import User, ClientProfile, WaterHoleProfile
# Register your models here.
admin.site.register(User)
admin.site.register(ClientProfile)
admin.site.register(WaterHoleProfile)