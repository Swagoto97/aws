from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Userupdate((models.Model)):
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)
    mobile = models.IntegerField(max_length=10, blank=True, null=False)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'userdetails'
