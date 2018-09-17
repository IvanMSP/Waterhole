
#Traer al user
me = User.objects.get(username='felix')
#Traer al perfil
me.adminwaterhole
#Traer al pozo que administra
pro.waterhole_admin
#Traer a todos los clientes del Pozo
ClientProfile.objects.filter(waterhole_client = pro.waterhole_admin)
