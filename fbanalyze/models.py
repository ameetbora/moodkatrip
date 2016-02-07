from django.db import models

class Places(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=150)
	rank = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Places"