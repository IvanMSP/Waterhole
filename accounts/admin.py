from django.contrib import admin
from .models import User, ClientProfile, AdminWaterHoleProfile
# Register your models here.
admin.site.register(User)
admin.site.register(ClientProfile)
admin.site.register(AdminWaterHoleProfile)