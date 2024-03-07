from django.db import models

class DataPoint(models.Model):
    x_value = models.IntegerField()
    y_value = models.IntegerField()
