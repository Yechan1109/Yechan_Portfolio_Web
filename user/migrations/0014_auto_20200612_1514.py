# Generated by Django 2.1.7 on 2020-06-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20200609_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intake',
            name='Route_text',
        ),
        migrations.AlterField(
            model_name='intake',
            name='Route',
            field=models.CharField(blank=True, choices=[('기관', '기관'), ('학교', '학교'), ('개인신청', '개인신청'), ('수강명령', '수강명령'), ('친구 및 지인소개', '친구 및 지인소개')], default='', max_length=10, null=True, verbose_name='의뢰경로'),
        ),
    ]