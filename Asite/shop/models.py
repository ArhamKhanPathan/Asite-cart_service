from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sunCategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    pro_disc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default=" ")


    def __str__(self):
        return self.pro_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=500, default=" ")

    def __str__(self):
        return self.name