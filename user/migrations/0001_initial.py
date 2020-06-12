# Generated by Django 2.1.7 on 2020-06-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('Name', models.CharField(max_length=10, unique=True, verbose_name='내담자 이름')),
                ('Reg', models.DateField(null=True, verbose_name='등록날짜')),
                ('Coun', models.CharField(blank=True, choices=[('이성영', '이성영'), ('정현재', '정현재'), ('김현정', '김현정'), ('문보라', '문보라'), ('박지숙', '박지숙'), ('김수미', '김수미'), ('강주연', '강주연'), ('노미나', '노미나'), ('곽은영', '곽은영')], default='', max_length=3, null=True, verbose_name='최초상담자')),
                ('Gender', models.CharField(blank=True, choices=[('남자', '남자'), ('여자', '여자')], default='', max_length=2, null=True, verbose_name='성별')),
                ('Jumin', models.CharField(blank=True, default='', max_length=13, verbose_name='주민등록번호')),
                ('Age', models.IntegerField(blank=True, default=0, null=True, verbose_name='연령')),
                ('Kakao', models.CharField(blank=True, default='', max_length=20, verbose_name='카카오 아이디')),
                ('Address1', models.CharField(blank=True, default='', max_length=50, verbose_name='주소')),
                ('Address2', models.CharField(blank=True, default='', max_length=50, verbose_name='현주거지')),
                ('Tel1', models.CharField(blank=True, default='', max_length=15, verbose_name='전화번호')),
                ('Tel2', models.CharField(blank=True, default='', max_length=15, verbose_name='긴급연락처')),
                ('Res', models.CharField(blank=True, choices=[('자가', '자가'), ('전세', '전세'), ('원룸(월세)', '원룸(월세)'), ('고시텔(월세)', '고시텔(월세)'), ('기타', '기타')], default='', max_length=10, null=True, verbose_name='주거형태')),
                ('Res_text', models.CharField(blank=True, default='', max_length=50, verbose_name='기타내용')),
                ('Fam', models.CharField(blank=True, choices=[('조손가정', '조손가정'), ('한부모', '한부모'), ('부모', '부모'), ('독립', '독립'), ('동거', '동거'), ('기타', '기타')], default='', max_length=15, null=True, verbose_name='가족형태')),
                ('Fam_text', models.CharField(blank=True, default='', max_length=50, verbose_name='기타내용')),
                ('Ssgrade', models.CharField(blank=True, choices=[('기초수급', '기초수급'), ('차상위', '차상위'), ('의료급여', '의료급여'), ('기타', '기타')], default='', max_length=10, null=True, verbose_name='보호구분')),
                ('Ssgrade_text', models.CharField(blank=True, default='', max_length=50, verbose_name='기타내용')),
                ('His', models.CharField(blank=True, choices=[('없음', '없음'), ('전화 및 SNS', '전화 및 SNS'), ('대면', '대면'), ('기타', '기타')], default='', max_length=15, null=True, verbose_name='상담이력')),
                ('Route', models.CharField(blank=True, choices=[('선생님', '선생님'), ('기관소개', '기관소개'), ('기타', '기타')], default='', max_length=10, null=True, verbose_name='의뢰경로')),
                ('Route_text', models.CharField(blank=True, default='', max_length=50, verbose_name='기타내용')),
                ('Eco1', models.IntegerField(blank=True, default=0, null=True, verbose_name='경제(알바)')),
                ('Eco2', models.IntegerField(blank=True, default=0, null=True, verbose_name='경제(취업)')),
                ('Eco3', models.IntegerField(blank=True, default=0, null=True, verbose_name='경제(부모지원)')),
                ('Eco4', models.IntegerField(blank=True, default=0, null=True, verbose_name='경제(기타)')),
                ('Edu', models.CharField(blank=True, choices=[('초등', '초등'), ('중등', '중등'), ('고등', '고등'), ('기타', '기타')], max_length=10, null=True, verbose_name='최종학력')),
                ('Edu_text', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='최종학력(기타)')),
                ('Job', models.CharField(blank=True, choices=[('없음', '없음'), ('있음', '있음')], max_length=10, null=True, verbose_name='직업')),
                ('Job_text', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='직업명')),
                ('Disorder', models.CharField(blank=True, choices=[('없음', '없음'), ('있음', '있음')], max_length=10, null=True, verbose_name='장애여부')),
                ('Disorder_text', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='장애명')),
                ('Other', models.CharField(blank=True, max_length=30, null=True, verbose_name='타기관 이용경험')),
                ('Institute', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='의뢰기관')),
                ('Incharge_name', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='의뢰인 이름')),
                ('Incharge_tel', models.CharField(blank=True, max_length=30, null=True, verbose_name='의뢰인 연락처')),
            ],
            options={
                'verbose_name': '기본인적사항',
                'verbose_name_plural': '기본인적사항',
                'db_table': 'intake',
            },
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setplan_name', models.CharField(max_length=10, unique=True, verbose_name='내담자 이름')),
                ('medical_start', models.DateField(blank=True, null=True, verbose_name='의료지원 시작일')),
                ('medical_end', models.DateField(blank=True, null=True, verbose_name='의료지원 종료일')),
                ('setplan_date', models.DateTimeField(auto_now_add=True, verbose_name='계획 작성일')),
                ('medical_A1_MF', models.IntegerField(blank=True, default=0, null=True, verbose_name='치과 월빈도')),
                ('medical_A1_TF', models.IntegerField(blank=True, default=0, null=True, verbose_name='치과 총빈도')),
                ('medical_A1_Text', models.CharField(blank=True, default='', max_length=100, verbose_name='치과 내용')),
                ('medical_A2_MF', models.IntegerField(blank=True, default=0, null=True, verbose_name='여성의학 월빈도')),
                ('medical_A2_TF', models.IntegerField(blank=True, default=0, null=True, verbose_name='여성의학 총빈도')),
                ('medical_A2_Text', models.CharField(blank=True, default='', max_length=100, verbose_name='여성의학 내용')),
                ('medical_A3_MF', models.IntegerField(blank=True, default=0, null=True, verbose_name='한방의학 월빈도')),
                ('medical_A3_TF', models.IntegerField(blank=True, default=0, null=True, verbose_name='한방의학 총빈도')),
                ('medical_A3_Text', models.CharField(blank=True, default='', max_length=100, verbose_name='한방의학 내용')),
                ('medical_A4_MF', models.IntegerField(blank=True, default=0, null=True, verbose_name='가정의학 월빈도')),
                ('medical_A4_TF', models.IntegerField(blank=True, default=0, null=True, verbose_name='가정의학 총빈도')),
                ('medical_A4_Text', models.CharField(blank=True, default='', max_length=100, verbose_name='가정의학 내용')),
                ('CT', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Intake', verbose_name='CT')),
            ],
            options={
                'verbose_name': '사례지원계획',
                'verbose_name_plural': '사례지원계획',
                'db_table': 'planning',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfor_date', models.DateField(verbose_name='진행 날짜')),
                ('perfor_people', models.IntegerField(verbose_name='인원')),
                ('perfor_count', models.IntegerField(verbose_name='건수')),
                ('perfor_program', models.CharField(choices=[('의료지원사업', (('의료 아웃리치', '의료 아웃리치'), ('소녀돌봄약국지원', '소녀돌봄약국지원'))), ('교육지원사업', (('성교육장이용', '성교육장이용'), ('찾아가는 성매매예방교육연극', '찾아가는 성매매예방교육연극'), ('종사자교육', '종사자교육'))), ('성건강지원사업', (('성건강수첩', '성건강수첩'), ('찾아가는 초등성건강교육', '찾아가는 초등성건강교육'), ('소그룹 성건강교육', '소그룹 성건강교육'), ('생리대 배분', '생리대 배분'), ('생리대 후원 확보', '생리대 후원 확보'))), ('네트워크', (('거리, 방문홍보', '온라인 홍보'), ('우편홍보', '우편홍보'), ('내외부 직원교육', '내외부 직원교육'), ('네트워크 및 사업협력', '네트워크 및 사업협력'), ('대학생 타기관 교육, 네트워킹', '대학생 타기관 교육, 네트워킹'), ('연합사례회의, 지원협력', '연합사례회의, 지원협력'), ('후원처 자원발굴, 관리', '후원처 자원발굴, 관리'), ('이용자 만족도조사, 질적인터뷰 등', '이용자 만족도조사, 질적인터뷰 등'), ('자원봉사활동', '자원봉사활동')))], max_length=30, verbose_name='프로그램')),
            ],
            options={
                'verbose_name': '실적등록',
                'verbose_name_plural': '실적등록',
                'db_table': 'program',
            },
        ),
    ]