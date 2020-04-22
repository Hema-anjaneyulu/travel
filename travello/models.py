from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=50)
    image_main=models.ImageField(upload_to='pics')
    desc1=models.TextField()
    desc2=models.TextField()
    desc3=models.TextField()
    desc4=models.TextField()
    desc5=models.TextField()
    image1=models.ImageField(upload_to='pics')
    image2=models.ImageField(upload_to='pics')
    image3=models.ImageField(upload_to='pics')
    image4=models.ImageField(upload_to='pics')