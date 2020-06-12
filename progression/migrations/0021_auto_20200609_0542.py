# Generated by Django 2.1.7 on 2020-06-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progression', '0020_auto_20200609_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctrs',
            name='sum_10',
            field=models.IntegerField(blank=True, null=True, verbose_name='폭력가해 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_11',
            field=models.IntegerField(blank=True, null=True, verbose_name='정신건강 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_2',
            field=models.IntegerField(blank=True, null=True, verbose_name='가정 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_3',
            field=models.IntegerField(blank=True, null=True, verbose_name='또래 및 학교 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_4',
            field=models.IntegerField(blank=True, null=True, verbose_name='지지체계 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_5',
            field=models.IntegerField(blank=True, null=True, verbose_name='성건강_공통 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_6',
            field=models.IntegerField(blank=True, null=True, verbose_name='성건강_성관계 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_7',
            field=models.IntegerField(blank=True, null=True, verbose_name='성폭력 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='sum_9',
            field=models.IntegerField(blank=True, null=True, verbose_name='폭력피해 Sum'),
        ),
        migrations.AddField(
            model_name='ctrs',
            name='total',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='sum_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='개인 Sum'),
        ),
    ]
