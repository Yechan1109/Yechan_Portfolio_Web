# Generated by Django 2.1.7 on 2020-06-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='medical_A_sum',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='진료 총 합계'),
        ),
    ]