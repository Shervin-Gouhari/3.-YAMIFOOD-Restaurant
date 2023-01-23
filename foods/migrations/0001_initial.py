# Generated by Django 4.1.4 on 2023-01-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, verbose_name='توضیحات')),
                ('rate', models.PositiveIntegerField(verbose_name='امتیاز')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('time', models.PositiveIntegerField(verbose_name='زمان لازم')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('photo', models.ImageField(upload_to='foods')),
            ],
        ),
    ]
