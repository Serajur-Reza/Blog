# Generated by Django 2.2.5 on 2019-11-24 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20191124_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
    ]