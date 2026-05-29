from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Фамилия")
    year = models.IntegerField(verbose_name="Курс")

    answer = models.IntegerField(verbose_name="Результат теста", blank=True, null=True)
    wentToLink = models.BooleanField(verbose_name="Перешел по ссылке", blank=True, null=True)
    takeCardNumber = models.BooleanField(verbose_name="Передал номер карты", blank=True, null=True)
    takeCardCVV = models.BooleanField(verbose_name="Передал cvv код", blank=True, null=True)
    takeCardFIO = models.BooleanField(verbose_name="Передал фио из карты", blank=True, null=True)
    takeCardDATE = models.BooleanField(verbose_name="Передал срок действия карты", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - Группа {self.year}"

    class Meta:
        ordering = ("id",)
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"


class Card(models.Model):
    number = models.CharField(max_length=8,verbose_name="Номер карты")
    nameBank = models.CharField(max_length=100, verbose_name="Название банка")
    system = models.CharField(max_length=100,verbose_name="Система")

    def __str__(self):
        return f"{self.nameBank}"

    class Meta:
        ordering = ("id",)
        verbose_name = "<Банк>"
        verbose_name_plural = "Банки"