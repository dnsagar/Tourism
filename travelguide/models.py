from django.db import models

# Create your models here.


class place(models.Model):

	pid = models.AutoField(primary_key=True)
	pname=models.CharField(max_length=300)
	pdes=models.CharField(max_length=300)
	pimage1=models.CharField(max_length=300)
	pimage2=models.CharField(max_length=300)
	pimage3=models.CharField(max_length=300)
	prating=models.CharField(max_length=300)
	pcity=models.CharField(max_length=300)
	
	
class hotel(models.Model):

	pid=models.CharField(max_length=300)
	hdes=models.CharField(max_length=300)
	hrating=models.CharField(max_length=300)
	hname=models.CharField(max_length=300)
	hphone=models.CharField(max_length=300)
	hemail=models.CharField(max_length=300)
	himage1=models.CharField(max_length=300)
	himage2=models.CharField(max_length=300)
	himage3=models.CharField(max_length=300)
	city=models.CharField(max_length=300)
	address=models.CharField(max_length=300)



	
