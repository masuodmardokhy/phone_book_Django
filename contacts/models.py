from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'مشخصات '
        verbose_name_plural = 'مشخصات کاربران'



# class ContactModel(models.Model):
#     name = models.CharField(max_length=20, verbose_name='نام')
#     family = models.CharField(max_length=20, verbose_name='فامیلی')
#     phone = models.CharField(max_length=20, verbose_name='تلفن')
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = 'مشخصات '
#         verbose_name_plural = 'مشخصات کاربران'



