from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


class Form1(models.Model):
    c_name = models.CharField("", max_length=255)
    c_email = models.EmailField("", max_length=150, blank=True)

    def __str__(self):
        return self.c_name + '/' + str(self.c_email)

    def get_absolute_url(self):
        return reverse('cover')


class Form2(models.Model):
    t_name = models.CharField(max_length=255)
    t_email = models.EmailField(max_length=150)
    pregex = RegexValidator(
        regex=r'^\+?1?\d{10,12}$', message="In the format 9999999999")
    t_contact = models.CharField(
        validators=[pregex], max_length=17, blank=True)
    t_subject = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.t_name + ' / ' + str(self.t_email) + ' / ' + self.t_contact + ' / ' + self.t_subject

    def get_absolute_url(self):
        return reverse('cover')
