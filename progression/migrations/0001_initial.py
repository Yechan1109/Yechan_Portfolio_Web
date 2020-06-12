# Generated by Django 2.1.7 on 2020-06-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTRS',
            fields=[
                ('CTRS_id', models.AutoField(primary_key=True, serialize=False)),
                ('danger_name', models.CharField(max_length=10, verbose_name='내담자 이름')),
                ('danger_date', models.DateField(null=True, verbose_name='진행 날짜')),
                ('danger_label', models.CharField(blank=True, choices=[('1차', '1차'), ('2차', '2차'), ('3차', '3차')], default='', max_length=3, verbose_name='차수')),
                ('survey1_1', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='개인1')),
                ('survey1_2', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='개인2')),
                ('survey1_3', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='개인3')),
                ('survey1_4', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='개인4')),
                ('survey1_5', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='개인5')),
                ('survey2_1', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='가정1')),
                ('survey2_2', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='가정2')),
                ('survey2_3', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='가정3')),
                ('survey2_4', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='가정4')),
                ('survey2_5', models.IntegerField(blank=True, choices=[(9, '9'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, verbose_name='가정5')),
                ('sum_1', models.IntegerField(blank=True, null=True, verbose_name='개인영역 Sum')),
            ],
            options={
                'verbose_name': '위기분류척도',
                'verbose_name_plural': '위기분류척도',
                'db_table': 'ctrs',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('Progress_id', models.AutoField(primary_key=True, serialize=False)),
                ('getplan_name', models.CharField(max_length=10, verbose_name='내담자 이름')),
                ('getplan_date', models.DateField(null=True, verbose_name='진행 날짜')),
                ('inmedical_A1_select', models.CharField(blank=True, choices=[('평일', '평일'), ('야간', '야간')], default='', max_length=2, verbose_name='치과 구분')),
                ('inmedical_A1_select2', models.CharField(blank=True, choices=[('스케일링', '스케일링'), ('보철', '보철'), ('충치', '충치'), ('기타', '기타')], default='', max_length=4, verbose_name='치과 진료명')),
                ('inmedical_A1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_A1_Text', models.CharField(blank=True, default='없음', max_length=200, verbose_name='내용')),
                ('inmedical_A2_select', models.CharField(blank=True, choices=[('평일', '평일'), ('야간', '야간')], default='', max_length=2, verbose_name='여성의학 구분')),
                ('inmedical_A2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_A2_Text', models.CharField(blank=True, default='없음', max_length=200, verbose_name='내용')),
                ('inmedical_A3_select', models.CharField(blank=True, choices=[('평일', '평일'), ('야간', '야간')], default='', max_length=2, verbose_name='한방의학 구분')),
                ('inmedical_A3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_A3_Text', models.CharField(blank=True, default='없음', max_length=200, verbose_name='내용')),
                ('inmedical_A4_select', models.CharField(blank=True, choices=[('평일', '평일'), ('야간', '야간')], default='', max_length=2, verbose_name='가정의학 구분')),
                ('inmedical_A4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_A4_Text', models.CharField(blank=True, default='없음', max_length=200, verbose_name='내용')),
                ('inmedical_B1_YN', models.BooleanField(default=False, verbose_name='여성의학검사 여부')),
                ('inmedical_B1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_B1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_B2_YN', models.BooleanField(default=False, verbose_name='기초검사 여부')),
                ('inmedical_B2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_B2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_B3_YN', models.BooleanField(default=False, verbose_name='항체검사 여부')),
                ('inmedical_B3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_B3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_B4_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_B4_YN', models.BooleanField(default=False, verbose_name='기타 여부')),
                ('inmedical_B4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_B4_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_C1_YN', models.BooleanField(default=False, verbose_name='치료제 여부')),
                ('inmedical_C1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_C1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_C2_YN', models.BooleanField(default=False, verbose_name='영양제 여부')),
                ('inmedical_C2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_C2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_C3_YN', models.BooleanField(default=False, verbose_name='임신테스트기 여부')),
                ('inmedical_C3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_C3_F', models.IntegerField(blank=True, default=0, null=True, verbose_name='수량')),
                ('inmedical_C3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_C4_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 이름')),
                ('inmedical_C4_YN', models.BooleanField(default=False, verbose_name='기타1 여부')),
                ('inmedical_C4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_C4_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_C5_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타2 이름')),
                ('inmedical_C5_YN', models.BooleanField(default=False, verbose_name='기타2 여부')),
                ('inmedical_C5_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_C5_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D1_YN', models.BooleanField(default=False, verbose_name='간염 여부')),
                ('inmedical_D1_Num', models.CharField(blank=True, choices=[('1차', '1차'), ('2차', '2차'), ('3차', '3차')], default='', max_length=3, verbose_name='간염 차수')),
                ('inmedical_D1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D2_YN', models.BooleanField(default=False, verbose_name='자궁경부암 여부')),
                ('inmedical_D2_Num', models.CharField(blank=True, choices=[('1차', '1차'), ('2차', '2차'), ('3차', '3차')], default='', max_length=3, verbose_name='자궁경부암 차수')),
                ('inmedical_D2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D3_YN', models.BooleanField(default=False, verbose_name='독감예방 여부')),
                ('inmedical_D3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D4_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_D4_YN', models.BooleanField(default=False, verbose_name='기타1 여부')),
                ('inmedical_D4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D4_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D5_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_D5_YN', models.BooleanField(default=False, verbose_name='기타2 여부')),
                ('inmedical_D5_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D5_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_D6_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_D6_YN', models.BooleanField(default=False, verbose_name='기타3 여부')),
                ('inmedical_D6_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_D6_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_E1_YN', models.BooleanField(default=False, verbose_name='외부병원(치과) 여부')),
                ('inmedical_E1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_E1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_E2_YN', models.BooleanField(default=False, verbose_name='외부병원(여성) 여부')),
                ('inmedical_E2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_E2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_E3_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_E3_YN', models.BooleanField(default=False, verbose_name='기타 여부')),
                ('inmedical_E3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_E3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_F1_YN', models.BooleanField(default=False, verbose_name='잇솔질교육 여부')),
                ('inmedical_F1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_F1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_F2_YN', models.BooleanField(default=False, verbose_name='안경지원 여부')),
                ('inmedical_F2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_F2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_F3_YN', models.BooleanField(default=False, verbose_name='몸펴기운동 지원 여부')),
                ('inmedical_F3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_F3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_F4_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmedical_F4_YN', models.BooleanField(default=False, verbose_name='기타 여부')),
                ('inmedical_F4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_F4_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_G1_YN', models.BooleanField(default=False, verbose_name='의료상담(대면) 여부')),
                ('inmedical_G1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_G1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_G2_YN', models.BooleanField(default=False, verbose_name='의료상담(전화) 여부')),
                ('inmedical_G2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_G2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmedical_G3_YN', models.BooleanField(default=False, verbose_name='의료상담(SNS) 여부')),
                ('inmedical_G3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmedical_G3_Text', models.CharField(blank=True, max_length=200, verbose_name='내용')),
                ('inmental_A1_YN', models.BooleanField(default=False, verbose_name='정신보건상담(대면) 여부')),
                ('inmental_A1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_A1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_A2_YN', models.BooleanField(default=False, verbose_name='정신보건상담(전화) 여부')),
                ('inmental_A2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_A2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_B1_YN', models.BooleanField(default=False, verbose_name='종합심리검사 여부')),
                ('inmental_B1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_B1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_B2_Name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmental_B2_YN', models.BooleanField(default=False, verbose_name='기타 여부')),
                ('inmental_B2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_B2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_C1_YN', models.BooleanField(default=False, verbose_name='원예치료 여부')),
                ('inmental_C1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_C1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_C2_YN', models.BooleanField(default=False, verbose_name='몸치유 여부')),
                ('inmental_C2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_C2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('inmental_C3_name', models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')),
                ('inmental_C3_YN', models.BooleanField(default=False, verbose_name='기타 여부')),
                ('inmental_C3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('inmental_C3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('incase_A1_select', models.CharField(blank=True, choices=[('상담', '상담'), ('수강명령', '수강명령')], default='', max_length=5, verbose_name='대면 구분')),
                ('incase_A1_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('incase_A1_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('incase_A2_select', models.CharField(blank=True, choices=[('상담', '상담'), ('수강명령', '수강명령')], default='', max_length=5, verbose_name='심층 구분')),
                ('incase_A2_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('incase_A2_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('incase_A3_select', models.CharField(blank=True, choices=[('상담', '상담'), ('수강명령', '수강명령')], default='', max_length=5, verbose_name='전화 구분')),
                ('incase_A3_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('incase_A3_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('incase_A4_select', models.CharField(blank=True, choices=[('상담', '상담'), ('수강명령', '수강명령')], default='', max_length=5, verbose_name='SNS 구분')),
                ('incase_A4_C', models.IntegerField(blank=True, default=0, null=True, verbose_name='비용')),
                ('incase_A4_Text', models.CharField(blank=True, default='', max_length=200, verbose_name='내용')),
                ('CT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Intake', verbose_name='CT')),
            ],
            options={
                'verbose_name': '사례지원진행',
                'verbose_name_plural': '사례지원진행',
                'db_table': 'progress',
            },
        ),
    ]
