# Generated by Django 4.1.4 on 2023-01-08 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_blog_comment_related_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='BlogComment',
        ),
    ]
