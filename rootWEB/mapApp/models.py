from django.db import models

# Create your models here.

class WwgUser(models.Model) :
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_birthyear = models.CharField(max_length=50)

    def __str__(self) :
        return self.user_id

# class wwg_place(models.Model) :
#     # id
#     index = models.IntegerField()
#     name = models.CharField(max_length=200)
#     number = models.IntegerField(default=0)
#     address = models.CharField(max_length=200)
#     category = models.CharField(max_length=100)
#     about = models.TextField()
#     imgURL = models.CharField(max_length=1000)
#     img = models.CharField(max_length=300)
#     lat = models.IntegerField()
#     lng = models.IntegerField()

class WwgZerowaste(models.Model) :
    # id
    index = models.IntegerField()
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    about = models.TextField()
    imgURL = models.CharField(max_length=1000)
    img = models.CharField(max_length=300)
    lat = models.IntegerField()
    lng = models.IntegerField()

    def __str__(self) :
        return self.name

class WwgVegan(models.Model) :
    # id
    index = models.IntegerField()
    name = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    about = models.TextField()
    imgURL = models.CharField(max_length=1000)
    img = models.CharField(max_length=300)
    lat = models.IntegerField()
    lng = models.IntegerField()

    def __str__(self) :
        return self.name

class WwgClick(models.Model) :
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    cnt = models.IntegerField()

    def __str__(self):
        return self.user_id + self.name + self.cnt