# Generated by Django 2.2.6 on 2019-11-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20191123_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Name',
            field=models.CharField(default='', max_length=250, verbose_name='Name'),
        ),
    ]