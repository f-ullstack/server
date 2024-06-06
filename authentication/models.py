from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    password = models.CharField(blank=False, max_length=20)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(blank=False, max_length=10)
    lastName = models.CharField(blank=False, max_length=10)
    fullName = models.CharField(blank=False, max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.fullName

class Product(models.Model):
    userProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=10)
    description = models.CharField(blank=False, max_length=30)
    quantityInStock = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name