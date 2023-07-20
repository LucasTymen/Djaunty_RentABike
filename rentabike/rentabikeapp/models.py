from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.

class Bike(models.Model):
  STANDARD = "ST"
  TANDEM = "TA"
  ELECTRIC = "EL"
  BIKE_TYPE_CHOICES = [
    (STANDARD, "Standard"),
    (TANDEM, "Tandem"),
    (ELECTRIC, "Electric")
  ]

  bike_type = models.Charflied(max_length=2,choices=BIKE_TYPE_CHOICES,default=STANDARD)
  color = models.Charfield(max_length=10,default="")

  def __str__(self):
    return self.bike_type + " - " + self.color
