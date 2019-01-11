from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
# Create your models here.
from waterhole.models import WaterHole,ZoneModel
import uuid

class User(AbstractUser):
	is_client = models.BooleanField(default=False)
	is_admin_waterhole = models.BooleanField(default= False)


	def get_adminwaterhole_profile(self):
		admin_waterhole_profile = None
		if hasattr(self,'adminwaterhole'):
			admin_waterhole_profile = self.adminwaterhole
		return admin_waterhole_profile

	def get_client_profile(self):
		client_profile = None
		if hasattr(self, 'clientprofile'):
			client_profile = self.clientprofile
		return client_profile

	class Meta:
		db_table = 'auth_user'




class ClientProfile(models.Model):
	user_client = models.OneToOneField(User, related_name='clientprofile', on_delete = models.CASCADE)
	waterhole_client = models.ForeignKey(WaterHole, related_name='waterholeclient')
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	photo_avatar = models.ImageField(upload_to ='avatar-client', default='/default/default-avatar.png',blank=True,null=True)
	

	def __str__(self):
		return self.user_client.username

	def get_detail_client(self):
		return reverse('account:detail-client',args=[self.user_client.id, self.user_client.username])

class WaterHoleProfile(models.Model):
	user_admin_waterhole = models.OneToOneField(User, related_name='adminwaterhole', on_delete = models.CASCADE)
	waterhole_admin = models.ForeignKey(WaterHole, related_name='waterholadmin')
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	photo_avatar = models.ImageField(upload_to ='avatar-admin', blank=True,null=True)

	def __str__(self):
		return self.user_admin_waterhole.username

	def get_clients(self):
		clients_waterhole = ClientProfile.objects.filter(waterhole_client = self.waterhole_admin)
		return clients_waterhole

class ContractModel(models.Model):
	waterhole_admin = models.ForeignKey(WaterHole, related_name = 'waterhole')
	user_profile = models.OneToOneField(ClientProfile, related_name='userprofile')
	zone_waterhole = models.ForeignKey(ZoneModel, related_name = 'zone')
	date_register = models.DateTimeField(auto_now_add = True)
	number_register = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False)
	ine_ide = models.BooleanField(default = False)
	free_copaci = models.BooleanField(default = False)
	formatt = models.BooleanField(default = False)
	cost = models.DecimalField(max_digits = 10, decimal_places = 2)
	permission_adress = models.BooleanField(default = False)

	def __str__(self):
		return '{} - {} '.format(self.user_profile.user_client.first_name, self.zone_waterhole.name)

class AdressModel(models.Model):
	contract = models.ForeignKey(ContractModel,related_name='contract')
	street = models.CharField(max_length = 120)
	interior_number = models.IntegerField()
	ext_number = models.IntegerField()
	neighborhood = models.CharField(max_length = 150)
	cp = models.CharField(max_length = 5)
	delegation = models.CharField(max_length = 150)
	state = models.CharField(max_length = 150)

	def __str__(self):
		return '{} - {} - {}'.format(self.contract.user_profile.user_client.username, self.street,self.neighborhood)

class Ticket(models.Model):
	
	def get_folio():
		return Ticket.objects.count() + 1

	date = models.DateTimeField(auto_now_add = True)
	cost = models.DecimalField(max_digits = 10, decimal_places = 2)
	concept = models.TextField(blank=True, null=True)
	folio = models.IntegerField(default = get_folio)
	profile_client = models.ForeignKey(ClientProfile, related_name='contract',blank=True, null=True)

	def __str__(self):
		return 'Usuario: {} - Folio: {}'.format(self.profile_client,self.folio)

		
	