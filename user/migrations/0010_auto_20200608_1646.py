# Generated by Django 2.1.7 on 2020-06-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200608_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='case_end',
            field=models.DateField(null=True, verbose_name='사례관리 종료일'),
        ),
        migrations.AddField(
            model_name='planning',
            name='case_start',
            field=models.DateField(null=True, verbose_name='사례관리 시작일'),
        ),
        migrations.AddField(
            model_name='planning',
            name='mental_end',
            field=models.DateField(null=True, verbose_name='심리지원 종료일'),
        ),
        migrations.AddField(
            model_name='planning',
            name='mental_start',
            field=models.DateField(null=True, verbose_name='심리지원 시작일'),
        ),
    ]