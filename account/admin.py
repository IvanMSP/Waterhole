from django.contrib import admin
from .models import User, ClientProfile, WaterHoleProfile,ContractModel,AdressModel,Ticket
# Register your models here.
admin.site.register(User)
admin.site.register(ClientProfile)
admin.site.register(WaterHoleProfile)
admin.site.register(ContractModel)
admin.site.register(AdressModel)
admin.site.register(Ticket)