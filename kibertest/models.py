from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    group = models.IntegerField()
    answer = models.IntegerField()
    takeCardNumber = models.BooleanField()
    takeCardCVV = models.BooleanField()
    takeCardFIO = models.BooleanField()
    takeCardDATA = models.BooleanField()

    def __str__(self):
        return f"{self.name} - Группа {self.group}"