# Generated by Django 4.1.4 on 2023-01-08 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_rename_comment_foodcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodcomment',
            old_name='related_blog',
            new_name='related_food',
        ),
    ]
