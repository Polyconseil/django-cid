from django.db import models


class Item(models.Model):
    number = models.IntegerField()
