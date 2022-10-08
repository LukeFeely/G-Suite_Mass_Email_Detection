from django.db import models

# Create your models here.
class Hashes(models.Model):
    hashValue = models.CharField(primary_key = True, max_length=100, null=False)
    count = models.IntegerField(null=False, default=1)
