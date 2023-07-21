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
    (ELECTRIC, "Electric"),
  ]
  bike_type = models.CharField(max_length=2,choices=BIKE_TYPE_CHOICES,default=STANDARD)
  color = models.CharField(max_length=10,default="")

  def __str__(self):
    return self.bike_type + " - " + self.color


class Renter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=15)
  vip_num = models.IntegerField(default=0)

  def __str__(self):
    return self.first_name + " " + self.last_name + " - #" + self.phone


class Rental(models.Model):
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE),
  renter = models.ForeignKey(Renter, on_delete=models.CASCADE),
  date = models.DateField(default=datetime.date.today),
  price = models.FloatField(default=0.0),

  def calc_price(self):
    curr_price = BASE_PRICE
    if self.bike.bike_type == "TA":
      curr_price += TANDEM_SURCHARGE
    if self.bike.bike_type == "EL":
      curr_price += ELECTRIC_SURCHARGE
    if self.renter.vip_num > 0:
      curr_price *= 0.8
    self.price = curr_price

"""
seed :

bike_standard_white = Bike(bike_type="ST", color="white")
bike_standard_white.save()
bike_electric_blue = Bike(bike_type="EL", color="blue")
bike_electric_blue.save()
bike_pink_tandem = Bike(bike_type="TA", color="pink")
bike_pink_tandem.save()
bike_red_tandem = Bike(bike_type="TA", color="red")
bike_red_tandem.save()
bike_silver = Bike(bike_type="ST", color="silver")
bike_silver.save()
bike_blackbolt = Bike(bike_type="EL", color="black")
bike_blackbolt.save()


renter_ernest = Renter(first_name="Ernest",last_name="Borgnine",phone="0555698388", vip_num=3)
renter_ernest.save()
renter_bob = Renter(first_name="Bob",last_name="Hoskins",phone="094589432")
renter_bob.save()
renter_greg = Renter(first_name="Gregory",last_name="Gadebois",phone="0165424676")
renter_greg.save()
renter_manu = Renter(first_name="Emmanuel",last_name="Macron",phone="013568434")
renter_manu.save()

 first_name = models.CharField(max_length=30),
  last_name = models.CharField(max_length=30),
  phone = models.CharField(max_length=15),
  vipt_num = models.IntegerField(default=0)
"""
