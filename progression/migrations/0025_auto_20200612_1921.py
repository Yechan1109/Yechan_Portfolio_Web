# Generated by Django 2.1.7 on 2020-06-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progression', '0024_auto_20200612_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctrs',
            name='survey1_1',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='개인1'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey1_2',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='개인2'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey1_3',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='개인3'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey1_4',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='개인4'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey1_5',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='개인5'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey2_1',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='가정1'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey2_2',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='가정2'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey2_3',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='가정3'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey2_4',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='가정4'),
        ),
        migrations.AlterField(
            model_name='ctrs',
            name='survey2_5',
            field=models.IntegerField(choices=[(0, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True, verbose_name='가정5'),
        ),
    ]