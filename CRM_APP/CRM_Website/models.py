from django.db import models

# Create your models here.

class Record(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  created_at = models.DateField(auto_now_add=True)
  Phone = models.CharField(max_length=12)
  Address = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  zipcode = models.CharField(max_length=10)

  def __str__(self):
    return (f"{self.first_name} {self.last_name}")
