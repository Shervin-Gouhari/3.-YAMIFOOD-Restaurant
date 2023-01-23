from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=100)
    content = RichTextField(_("متن"))
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs")
    category = models.ForeignKey("Category", related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag", related_name="blogs", verbose_name=_("تگ ها"))
    
    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ بروزرسانی"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ بروزرسانی"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    
class BlogComment(models.Model):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        
    related_blog = models.ForeignKey("Blog", verbose_name=_("مقاله"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=50)
    email = models.EmailField(_("آدرس ایمیل"), max_length=100)
    comment = models.TextField(_("متن نظر"))
    created_at = models.DateTimeField(_("زمان انتشار"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.email