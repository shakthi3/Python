from django.db import models

# Create your models here.
class UserDetails(models.Model):
  username = models.CharField(max_length=255)
  password= models.CharField(max_length=255)
  # 333 notes let we use a sqlite3