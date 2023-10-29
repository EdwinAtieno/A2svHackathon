from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Profiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user


class Income(models.Model):
    income = models.CharField(max_length=100)
    profile = models.ForeignKey(Profiles, on_delete=models.PROTECT, default=list)
    source = models.CharField(max_length=100)
    amount = models.IntegerField()
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.income


class Expense(models.Model):
    expense = models.CharField(max_length=100)
    profile = models.ForeignKey(Profiles, on_delete=models.PROTECT, default=list)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.expense


class Savings(models.Model):
    savings = models.CharField(max_length=100)
    profile = models.ForeignKey(Profiles, on_delete=models.PROTECT, default=list)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.saving


class Goals(models.Model):
    goals = models.CharField(max_length=100)
    profile = models.ForeignKey(Profiles, on_delete=models.PROTECT, default=list)
    description = models.CharField(max_length=10000)
    target = models.IntegerField()

    def __str__(self):
        return self.goal



