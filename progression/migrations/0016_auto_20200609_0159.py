# Generated by Django 2.1.7 on 2020-06-08 16:59

from django.db import migrations
import progression.models


class Migration(migrations.Migration):

    dependencies = [
        ('progression', '0015_auto_20200608_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='incase_B1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='성건강 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_B2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='관계 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_B3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_C1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='먹거리 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_C2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='물품 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_C3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='교통비 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='incase_C4_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='자원연계 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A1_YN_2',
            field=progression.models.CustomBooleanField(default=False, verbose_name='치과(야간) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A2_YN_1',
            field=progression.models.CustomBooleanField(default=False, verbose_name='여성의학 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A2_YN_2',
            field=progression.models.CustomBooleanField(default=False, verbose_name='여성의학(야간) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A3_YN_1',
            field=progression.models.CustomBooleanField(default=False, verbose_name='한방의학 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A3_YN_2',
            field=progression.models.CustomBooleanField(default=False, verbose_name='한방의학(야간) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A4_YN_1',
            field=progression.models.CustomBooleanField(default=False, verbose_name='가정의학 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_A4_YN_2',
            field=progression.models.CustomBooleanField(default=False, verbose_name='가정의학(야간) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_B1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='여성의학검사 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_B2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기초검사 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_B3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='항체검사 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_B4_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_C1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='치료제 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_C2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='영양제 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_C3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='임신테스트기 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_C4_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타1 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_C5_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타2 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='간염 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='자궁경부암 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='독감예방 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D4_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타1 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D5_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타2 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_D6_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타3 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_E1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='외부병원(치과) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_E2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='외부병원(여성) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_E3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_F1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='잇솔질교육 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_F2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='안경지원 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_F3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='몸펴기운동 지원 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_F4_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_G1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='의료상담(대면) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_G2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='의료상담(전화) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmedical_G3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='의료상담(SNS) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_A1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='정신보건상담(대면) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_A2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='정신보건상담(전화) 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_B1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='종합심리검사 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_B2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_C1_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='원예치료 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_C2_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='몸치유 여부'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='inmental_C3_YN',
            field=progression.models.CustomBooleanField(default=False, verbose_name='기타 여부'),
        ),
    ]
