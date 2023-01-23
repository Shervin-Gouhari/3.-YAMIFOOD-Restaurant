from django.db import models
from django.utils.translation import gettext as _

class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "صبحانه"),
        ("lunch", "ناهار"),
        ("dinner", "شام"),
        ("drinks", "نوشیدنی"),
    ]
    name = models.CharField(_("نام"), max_length=200)
    description = models.CharField(_("توضیحات"), max_length=200)
    rate = models.PositiveIntegerField(_("امتیاز"), default=0)
    price = models.PositiveIntegerField(_("قیمت"), default=0)
    time = models.PositiveIntegerField(_("زمان لازم"), default=0)
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(_("عکس"), upload_to='foods')
    food_type = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="drinks")
    
    def __str__(self):
        return self.name
    
    
class FoodComment(models.Model):
    related_food = models.ForeignKey("Food", verbose_name=_("غذا"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=50)
    email = models.EmailField(_("آدرس ایمیل"), max_length=100)
    comment = models.TextField(_("متن نظر"))
    created_at = models.DateTimeField(_("زمان انتشار"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.email