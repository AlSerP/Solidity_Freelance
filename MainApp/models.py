from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.CharField(max_length=1000, unique=True)


class Task(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=255, default=None)
    cost = models.FloatField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Submitted_tasks(models.Model):
    sumbit_user_id = models.IntegerField()
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
