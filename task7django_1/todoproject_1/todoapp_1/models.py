from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class ToDo (models.Model):
    taskname=models.CharField(max_length=200)
    taskprio=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    taskalarm=models.BooleanField()
    tasktime=models.DateTimeField(blank=True, null=True)

