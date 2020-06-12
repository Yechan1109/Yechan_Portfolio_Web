# Generated by Django 2.1.7 on 2020-06-06 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('progression', '0002_auto_20200606_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctrs',
            name='CT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Intake', verbose_name='CT'),
            preserve_default=False,
        ),
    ]
