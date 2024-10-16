from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=200,db_index =True)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to='receipe/')
    receipe_slug = models.SlugField(unique=True)
    receipe_type = models.CharField(max_length=200,choices=(("veg","veg"),("non-veg","non-veg")))

class Ingrdients(models.Model):
    reciepe = models.ForeignKey(Receipe,on_delete=models.CASCADE,related_name="receipe_ingredents")
    ingredient_name = models.CharField(max_length=200)




