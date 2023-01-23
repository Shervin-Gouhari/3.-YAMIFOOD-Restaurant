from django.db import models
from django.utils.translation import gettext as _

class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=30)
    email = models.EmailField(_("آدرس ایمیل"), max_length=100)
    phone = models.IntegerField(_("شماره تلفن شخصی"))
    number = models.IntegerField(_("تعداد"), default=0)
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email