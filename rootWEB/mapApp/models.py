from django.db import models

# Create your models here.

class WwgUser(models.Model) :
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self) :
        return self.user_id + "\t" + self.user_pwd + "\t" + self.user_name

class zerowaste(models.Model) :
    # id
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    about = models.TextField()
    imgURL = models.CharField(max_length=1000)
    img = models.CharField(max_length=300)
    lat = models.IntegerField()
    lng = models.IntegerField()
