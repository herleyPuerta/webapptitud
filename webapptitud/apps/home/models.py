from django.db import models


class Cliente(models.Model):
	def urlogo(self,filename):
		return "images/Logos/%s/%s"%(self.fechaCreada,filename)

	def urlpantallazo(self,filename):
		return "images/Pantallazos/%s/%s"%(self.fechaCreada,filename)

	nombre		= models.CharField(max_length=120,null=False,blank=False)
	logo		= models.ImageField(upload_to=urlogo,null=True,blank=True)
	descripcion	= models.TextField(max_length=1000,null=False,blank=False)
	pantallazo	= models.ImageField(upload_to=urlpantallazo,null=True,blank=True)
	fechaCreada = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre