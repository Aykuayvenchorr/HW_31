from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from user.validators import check_birth_date


class Location(models.Model):
    name = models.CharField(max_length=400)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('member', 'Пользователь'),
        ('moderator', 'Модератор')
    )

    role = models.CharField(choices=ROLES, default='member', max_length=20)
    age = models.PositiveSmallIntegerField(null=True, blank=True, editable=False)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(verbose_name="email address", blank=True,
                              validators=[RegexValidator(regex="@rambler.ru",
                                                         inverse_match=True,
                                                         message="Регистрация с домена rambler запрещена.")])

    def save(self, *args, **kwargs):
        self.age = relativedelta(date.today(), self.birth_date).years
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'