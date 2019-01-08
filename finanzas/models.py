from django.db import models
from account.models import WaterHoleProfile
from django.utils.timezone import datetime
import uuid
from decimal import Decimal
from django.db.models import Sum
# Create your models here.

class Earning(models.Model):
	number_registry = models.UUIDField(primary_key=False,default = uuid.uuid4, editable=False)
	subject = models.TextField()
	quantity = models.DecimalField(blank=True, null=True, max_digits = 10, decimal_places = 2)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	admin_waterhole_earning = models.ForeignKey(WaterHoleProfile, related_name='earning_admin',on_delete = models.CASCADE)

	def __str__(self):
		return '{} de {}'.format(self.subject,self.admin_waterhole_earning)

class OutflowsModel(models.Model):
	number_registry = models.UUIDField(primary_key = False, default = uuid.uuid1, editable = False)
	subject = models.TextField()
	quantity = models.DecimalField(blank=True, null=True, max_digits = 10 , decimal_places = 2)
	date = models.DateTimeField(auto_now_add = True)
	admin_waterhole_outflow = models.ForeignKey(WaterHoleProfile,related_name='outflow_admin',on_delete = models.CASCADE)

	def __str__(self):
		return '{} de {}'.format(self.subject,self.quantity)

