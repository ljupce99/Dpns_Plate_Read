from django.db import models

# Create your models here.
from django.db import models

class Plate(models.Model):
    plate_number = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.plate_number}"
class Evidencija(models.Model):
    pleat=models.ForeignKey(Plate,on_delete=models.CASCADE)
    time=models.TimeField()
    date=models.DateField()