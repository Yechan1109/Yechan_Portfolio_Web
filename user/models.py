from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

from django.db.models import Manager, Model
from django.db.models import F


class CustomBooleanField(models.BooleanField):
    
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value)


class Intake(models.Model):
    Coun_choices = (
        ('이성영', '이성영'),
        ('정현재', '정현재'),
        ('김현정', '김현정'),
        ('문보라', '문보라'),
        ('박지숙', '박지숙'),
        ('김수미', '김수미'),
        ('강주연', '강주연'),
        ('노미나', '노미나'),
        ('곽은영', '곽은영'))
    Gender_choices = (
        ('남자', '남자'),
        ('여자', '여자'))
    Res_choices = (
        ('자가', '자가'),
        ('전세', '전세'),
        ('원룸(월세)', '원룸(월세)'),
        ('고시텔(월세)','고시텔(월세)'),
        ('기타','기타'))
    Yn_choices = (
        ('없음', '없음'),
        ('있음', '있음'))
    His_choices = (
        ('없음','없음'),
        ('전화 및 SNS', '전화 및 SNS'),
        ('대면', '대면'),
        ('기타', '기타'))  
    Rou_choices = (
        ('기관', '기관'),
        ('학교', '학교'),
        ('개인신청','개인신청'),
        ('수강명령','수강명령'),
        ('친구 및 지인소개','친구 및 지인소개'))
    Ss_choices = (
        ('기초수급', '기초수급'),
        ('차상위', '차상위'),
        ('의료급여','의료급여'),
        ('기타','기타'))
    Fam_choices = (
        ('조손가정', '조손가정'),
        ('한부모', '한부모'),
        ('부모','부모'),
        ('독립','독립'),
        ('동거','동거'),
        ('기타','기타'))
    Edu_choices = (
        ('초등','초등'),
        ('중등','중등'),
        ('고등','고등'),
        ('기타','기타'))
    # counselor = models.ForeignKey('counselor.User', related_name='intake', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField('작성일', auto_now_add=True)
    last_date = models.DateTimeField('마지막 수정날짜', auto_now=True)
    Name = models.CharField(verbose_name='내담자 이름', max_length=10, unique=True)
    Reg = models.DateField(null=True, verbose_name='등록날짜')
    Coun = models.CharField(null=True,blank=True, default="", choices=Coun_choices, max_length=3, verbose_name='최초상담자')
    Gender = models.CharField(null=True, blank=True, default="", choices=Gender_choices, max_length=2, verbose_name='성별')
    Jumin = models.CharField(blank=True, default="", max_length=13,verbose_name='주민등록번호')
    Age = models.IntegerField(null=True, blank=True, default=0, verbose_name='연령')
    Kakao = models.CharField(blank=True, default="", max_length=20,verbose_name='카카오 아이디')
    Address1 = models.CharField(blank=True, default="", max_length=200,verbose_name='주소')
    Address2 = models.CharField(blank=True, default="", max_length=200,verbose_name='현주거지')
    Tel1 = models.CharField(blank=True, default="", max_length=15,verbose_name='전화번호')
    Tel2 = models.CharField(blank=True, default="", max_length=15,verbose_name='긴급연락처')
    
    Res = models.CharField(null=True,blank=True, default="", choices=Res_choices, max_length=10, verbose_name='주거형태')
    Res_text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타내용')
    Fam = models.CharField(null=True,blank=True, default="", choices=Fam_choices, max_length=15,verbose_name='가족형태')
    Fam_text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타내용')
    Ssgrade = models.CharField(null=True,blank=True, default="", choices=Ss_choices, max_length=10,verbose_name='보호구분')
    Ssgrade_text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타내용')
    His = models.CharField(null=True,blank=True, default="", choices=His_choices,max_length=15, verbose_name='상담이력')
    Route = models.CharField(null=True,blank=True, default="", choices=Rou_choices, max_length=10, verbose_name='의뢰경로')
    
    Eco1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(알바)')
    Eco2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(취업)')
    Eco3 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(부모지원)')
    Eco4 = models.IntegerField(null=True, blank=True, default=0, verbose_name='경제(기타)')
    Edu = models.CharField(choices=Edu_choices, blank=True,max_length=10,null=True,verbose_name='최종학력')
    Edu_text = models.CharField(null=True, blank=True,default="", max_length=30, verbose_name='최종학력(기타)')
    Job = models.CharField(choices=Yn_choices, blank=True,max_length=10,null=True,verbose_name='직업')
    Job_text = models.CharField(null=True, blank=True,default="", max_length=30, verbose_name='직업명')
    Disorder = models.CharField(choices=Yn_choices, blank=True,max_length=10,null=True,verbose_name='장애여부')
    Disorder_text = models.CharField(null=True, blank=True,default="", max_length=30, verbose_name='장애명')
    Other = models.CharField(null=True, blank=True, max_length=30, verbose_name='타기관 이용경험')

    Institute = models.CharField(null=True, blank=True,default="", max_length=200, verbose_name='의뢰기관')
    Incharge_name = models.CharField(null=True, blank=True,default="", max_length=30, verbose_name='의뢰인 이름')
    Incharge_tel = models.CharField(null=True, blank=True, max_length=30, verbose_name='의뢰인 연락처')


    
    
    def __str__(self):
        return self.Name

    # def save(self, **kwargs):
    #     if not self.id:
    #         max = Intake.objects.aggregate(id_max=models.Max('id'))['id_max']
    #     if max is not None:
    #         max += 1
    #     else:
    #         max = 1
    #     self.id = "{}{:04d}".format("A", max)  # id from 100 to start
    #     super().save()


    # if Age:
    #     Jumin = str(Jumin)
    #     # print(Jumin)
    #     if Jumin[0] == '9':
    #         Age = 2020 - int('19' + Jumin[0:2]) + 1
    #     elif Jumin[0] == '0' or Jumin[0] =='1':
    #         Age = 2020 - int('20' + Jumin[0:2]) + 1
    # else:0

    # Jumin = str(Jumin)
    # if Jumin[0] == '9':
    #     Age = 2020 - int('19' + Jumin[0:2]) + 1
    # elif Jumin[0] == '0' or Jumin[0] =='1':
    #     Age = 2020 - int('20' + Jumin[0:2]) + 1

    class Meta:
        db_table = 'intake'
        verbose_name = '기본인적사항'
        verbose_name_plural = '기본인적사항'

    # def age_form(self, Jumin):
    #     Age = 2020 - int('19' + Jumin[0:2]) + 1
    #     return Age

    # def age_form2(self, Jumin):
    #     Age = 2020 - int('20' + Jumin[0:2]) + 1
    #     return Age

    # # def age_form3(self, Jumin):
    # #     return 

    # def get_age(self, Jumin):
    #     if Jumin:
    #         if Jumin[0] == '9':
    #             return self.age_form(Jumin)
    #         elif Jumin[0] == '0' or Jumin[0] == '1':
    #             return self.age_form2(Jumin)




class Planning(models.Model):
    
    # setplan_name = models.OneToOneField(Intake, on_delete=models.CASCADE)
    CT = models.OneToOneField(Intake, on_delete=models.CASCADE, verbose_name='CT')
    setplan_name = models.CharField(verbose_name='내담자 이름', max_length=10, unique=True)
    setplan_date = models.DateTimeField(auto_now_add=True, verbose_name='계획 작성일')
    last_date = models.DateTimeField('마지막 수정날짜', auto_now=True)
    counselor = models.ForeignKey('counselor.User', on_delete=models.CASCADE, verbose_name='상담자')


    medical_start = models.DateField(null=True, blank=True, verbose_name='의료지원 시작일')
    medical_end = models.DateField(null=True, blank=True, verbose_name='의료지원 종료일')
    mental_start = models.DateField(null=True, blank=True, verbose_name='심리지원 시작일')
    mental_end = models.DateField(null=True, blank=True, verbose_name='심리지원 종료일')
    case_start = models.DateField(null=True, blank=True, verbose_name='사례관리 시작일')
    case_end = models.DateField(null=True, blank=True, verbose_name='사례관리 종료일')
    # 의료지원
    medical_A1_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 월빈도')
    medical_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치과 총빈도')
    medical_A1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='치과 내용')
    medical_A2_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 월빈도')
    medical_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='여성의학 총빈도')
    medical_A2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='여성의학 내용')
    medical_A3_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 월빈도')
    medical_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='한방의학 총빈도')
    medical_A3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='한방의학 내용')
    medical_A4_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 월빈도')
    medical_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='가정의학 총빈도')
    medical_A4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='가정의학 내용')
    # medical_A_sum = models.IntegerField(null=True, blank=True, default=0, verbose_name='진료 총 합계')

    medical_B1_YN = CustomBooleanField(default=False, verbose_name='여성의학 검사 여부')
    medical_B1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='여성의학 검사 내용')
    medical_B2_YN = CustomBooleanField(default=False, verbose_name='기초검사 여부')
    medical_B2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기초검사 내용')
    medical_B3_YN = CustomBooleanField(default=False, verbose_name='항체검사 여부')
    medical_B3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='항체검사 내용')
    medical_B4_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타검사명')
    medical_B4_YN = CustomBooleanField(default=False, verbose_name='기타검사 여부') # 추가됨
    medical_B4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타검사 내용')

    medical_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='치료제 월빈도')
    medical_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='치료제 총빈도')
    medical_C1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='치료제 내용')
    medical_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='영양제 월빈도')
    medical_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='영양제 총빈도')
    medical_C2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='영양제 내용')
    medical_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='임신테스트기 월빈도')
    medical_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='임신테스트기 총빈도')
    medical_C3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='임신테스트기 내용')
    medical_C4_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타1 이름')
    medical_C4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타1 월빈도')
    medical_C4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타1 총빈도')
    medical_C4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타1 내용')
    medical_C5_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타2 이름')
    medical_C5_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타2 월빈도')
    medical_C5_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타2 총빈도')
    medical_C5_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타2 내용')

    medical_D1_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='간염예방접종 차수')
    medical_D1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='간염예방접종 내용')
    medical_D2_Num = models.IntegerField(null=True, blank=True, default=0, verbose_name='자궁경부암접종 차수')
    medical_D2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='자궁경부암접종 내용')
    medical_D3_YN = models.IntegerField(null=True, blank=True, default=0, verbose_name='독갑예방접종 총빈도')
    medical_D3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='독감예방접종 내용')
    medical_D4_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타1 접종 이름')
    medical_D4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타1 접종 총빈도')
    medical_D4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타1 접종 내용')
    medical_D5_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타2 접종 이름')
    medical_D5_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타2 접종 총빈도')
    medical_D5_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타2 접종 내용')
    medical_D6_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타3 접종 이름')
    medical_D6_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타3 접종 총빈도')
    medical_D6_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타3 접종 내용')

    medical_E1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(치과) 월빈도')
    medical_E1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(치과) 총빈도')
    medical_E1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='외부(치과) 내용')
    medical_E2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(여성) 월빈도')
    medical_E2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(여성) 총빈도')
    medical_E2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='외부(여성) 내용')
    medical_E3_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='외부(기타) 이름')
    medical_E3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='외부(기타) 월빈도')
    medical_E3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='외부(기타) 총빈도')
    medical_E3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='외부(기타) 내용')

    medical_F1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='잇솔질 월빈도')
    medical_F1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='잇솔질 총빈도')
    medical_F1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='잇솔질 내용')
    medical_F2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='안경지원 월빈도')
    medical_F2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='안경지원 총빈도')
    medical_F2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='안경지원 내용')
    medical_F3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='몸펴기 월빈도')
    medical_F3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='몸펴기 총빈도')
    medical_F3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='몸펴기 내용')
    medical_F4_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='예방(기타) 이름')
    medical_F4_MF = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방(기타) 월빈도')
    medical_F4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='예방(기타) 총빈도')
    medical_F4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='예방(기타) 내용')
    
    # 심리지원
    mental_A1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='정신(대면) 월빈도')
    mental_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신(대면) 총빈도')
    mental_A1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='정신(대면) 내용')
    mental_A2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='정신(전화) 월빈도')
    mental_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='정신(전화) 총빈도')
    mental_A2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='정신(전화) 내용')
    mental_B1_TF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='종합심리검사 총빈도')
    mental_B1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    mental_B2_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타 이름')
    mental_B2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    mental_B2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='정신(전화) 내용')
    mental_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='원예 월빈도')
    mental_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='원예 총빈도')
    mental_C1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='원예 내용')
    mental_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='몸치유 월빈도')
    mental_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='몸치유 총빈도')
    mental_C2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='몸치유 내용')
    mental_C3_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타 이름')
    mental_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타 월빈도')
    mental_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    mental_C3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타 내용')

    # # 사례관리
    case_A1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(대면) 월빈도')
    case_A1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(대면) 총빈도')
    case_A1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='사례(대면) 내용')
    case_A2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(심층) 월빈도')
    case_A2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(심층) 총빈도')
    case_A2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='사례(심층) 내용')
    case_A3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(전화) 월빈도')
    case_A3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(전화) 총빈도')
    case_A3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='사례(전화) 내용')
    case_A4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='사례(SNS) 월빈도')
    case_A4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='사례(SNS) 총빈도')
    case_A4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='사례(SNS) 내용')
    case_B1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='성건강 월빈도')
    case_B1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='성건강 총빈도')
    case_B1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='성건강 내용')
    case_B2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='관계 월빈도')
    case_B2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='관계 총빈도')
    case_B2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='관계 내용')
    case_B3_Name = models.CharField(blank=True, default="", max_length=15, verbose_name='기타 이름')
    case_B3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='기타 월빈도')
    case_B3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='기타 총빈도')
    case_B3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타 내용')
    case_C1_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='먹거리 월빈도')
    case_C1_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='먹거리 총빈도')
    case_C1_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='기타 내용')
    case_C2_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='물품 월빈도')
    case_C2_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='물품 총빈도')
    case_C2_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='물품 내용')
    case_C3_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='교통비 월빈도')
    case_C3_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='교통비 총빈도')
    case_C3_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='교통비 내용')
    case_C4_MF = models.IntegerField(null=True, blank=True, default=0,  verbose_name='자원연계 월빈도')
    case_C4_TF = models.IntegerField(null=True, blank=True, default=0, verbose_name='자원연계 총빈도')
    case_C4_Text = models.CharField(blank=True, default="", max_length=200, verbose_name='자원연계 내용')

    setplan_comment = models.TextField(blank=True, default="", max_length=2000, verbose_name='comment')
    setplan_sentence = models.TextField(blank=True, default="", max_length=2000, verbose_name='sentence')



    # sum_medical_A = models.IntegerField(null=True, blank=True, verbose_name='진료 total')
    # sum_medical_B = models.IntegerField(null=True, blank=True, verbose_name='각종검사 total')
    # sum_medical_C = models.IntegerField(null=True, blank=True, verbose_name='약지급 total')
    # sum_medical_D = models.IntegerField(null=True, blank=True, verbose_name='예방접종 total')
    # sum_medical_E = models.IntegerField(null=True, blank=True, verbose_name='외부병원 total')
    # sum_medical_F = models.IntegerField(null=True, blank=True, verbose_name='예방의학 total')
    # sum_mental_A  = models.IntegerField(null=True, blank=True, verbose_name='정신보건상담 total')
    # sum_mental_B = models.IntegerField(null=True, blank=True, verbose_name='심리검사 total')
    # sum_mental_C = models.IntegerField(null=True, blank=True, verbose_name='심리정서지원프로그램 total')
    # sum_case_A = models.IntegerField(null=True, blank=True, verbose_name='상담 total')
    # sum_case_B = models.IntegerField(null=True, blank=True, verbose_name='1:1교육 total')
    # sum_case_C = models.IntegerField(null=True, blank=True, verbose_name='기초생활지원 total')


    def __str__(self):
        return self.setplan_name
    
    # if medical_A1_TF or medical_A2_TF or medical_A3_TF or medical_A4_TF:
    #     medical_A_sum = medical_A1_TF+medical_A2_TF

    # @property
    # def sum(self):
    #     medical_A_sum = self.medical_A1_TF + self.medical_A2_TF + self.medical_A3_TF + self.medical_A4_TF
    #     return self.medical_A_sum

    @property
    def A_sum(self):
        if type(self.medical_A4_TF) != int:
            self.medical_A4_TF = 0
        return self.medical_A1_TF + self.medical_A2_TF + self.medical_A3_TF + self.medical_A4_TF

    def B_sum(self):
        return self.medical_B1_YN + self.medical_B2_YN + self.medical_B3_YN + self.medical_B4_YN
    
    def C_sum(self):
        if type(self.medical_C1_TF) != int:
            self.medical_C1_TF = 0
        if type(self.medical_C2_TF) != int:
            self.medical_C2_TF = 0
        if type(self.medical_C3_TF) != int:
            self.medical_C3_TF = 0
        if type(self.medical_C4_TF) != int:
            self.medical_C4_TF = 0
        if type(self.medical_C5_TF) != int:
            self.medical_C5_TF = 0
        return self.medical_C1_TF + self.medical_C2_TF + self.medical_C3_TF + self.medical_C4_TF + self.medical_C5_TF
    
    def D_sum(self):
        if type(self.medical_D1_Num) != int:
            self.medical_D1_Num = 0
        if type(self.medical_D2_Num) != int:
            self.medical_D2_Num = 0
        if type(self.medical_D3_YN) != int:
            self.medical_D3_YN = 0
        if type(self.medical_D4_TF) != int:
            self.medical_D4_TF = 0
        if type(self.medical_D5_TF) != int:
            self.medical_D5_TF = 0
        if type(self.medical_D6_TF) != int:
            self.medical_D6_TF = 0
        return self.medical_D1_Num + self.medical_D2_Num + self.medical_D3_YN + self.medical_D4_TF + self.medical_D5_TF + self.medical_D6_TF
        
    def E_sum(self):
        if type(self.medical_E1_TF) != int:
            self.medical_E1_TF = 0
        if type(self.medical_E2_TF) != int:
            self.medical_E2_TF = 0
        if type(self.medical_E3_TF) != int:
            self.medical_E3_TF = 0
        return self.medical_E1_TF + self.medical_E2_TF + self.medical_E3_TF

    def F_sum(self):
        if type(self.medical_F1_TF) != int:
            self.medical_F1_TF = 0
        if type(self.medical_F2_TF) != int:
            self.medical_F2_TF = 0
        if type(self.medical_F3_TF) != int:
            self.medical_F3_TF = 0
        if type(self.medical_F4_TF) != int:
            self.medical_F4_TF = 0
        return self.medical_F1_TF + self.medical_F2_TF + self.medical_F3_TF + self.medical_F4_TF

    def mental_A_sum(self):
        if type(self.mental_A1_TF) != int:
            self.mental_A1_TF = 0
        if type(self.mental_A2_TF) != int:
            self.mental_A2_TF = 0
        return self.mental_A1_TF + self.mental_A2_TF

    def mental_B_sum(self):
        if type(self.mental_B1_TF) != int:
            self.mental_B1_TF = 0
        if type(self.mental_B2_TF) != int:
            self.mental_B2_TF = 0
        return self.mental_B1_TF + self.mental_B2_TF

    def mental_C_sum(self):
        if type(self.mental_C1_TF) != int:
            self.mental_C1_TF = 0
        if type(self.mental_C2_TF) != int:
            self.mental_C2_TF = 0
        if type(self.mental_C3_TF) != int:
            self.mental_C3_TF = 0
        return self.mental_C1_TF + self.mental_C2_TF + self.mental_C3_TF

    def case_A_sum(self):
        if type(self.case_A1_TF) != int:
            self.case_A1_TF = 0
        if type(self.case_A2_TF) != int:
            self.case_A2_TF = 0
        if type(self.case_A3_TF) != int:
            self.case_A3_TF = 0
        if type(self.case_A4_TF) != int:
            self.case_A4_TF = 0
        return self.case_A1_TF + self.case_A2_TF + self.case_A3_TF + self.case_A4_TF

    def case_B_sum(self):
        if type(self.case_B1_TF) != int:
            self.case_B1_TF = 0
        if type(self.case_B2_TF) != int:
            self.case_B2_TF = 0
        if type(self.case_B3_TF) != int:
            self.case_B3_TF = 0
        return self.case_B1_TF + self.case_B2_TF + self.case_B3_TF

    def case_C_sum(self):
        if type(self.case_C1_TF) != int:
            self.case_C1_TF = 0
        if type(self.case_C2_TF) != int:
            self.case_C2_TF = 0
        if type(self.case_C3_TF) != int:
            self.case_C3_TF = 0
        if type(self.case_C4_TF) != int:
            self.case_C4_TF = 0
        return self.case_C1_TF + self.case_C2_TF + self.case_C3_TF + self.case_C4_TF   


    class Meta:
        db_table = 'planning'
        verbose_name = '사례지원계획'
        verbose_name_plural = '사례지원계획'



class Program(models.Model):
    program_name = (
        ('의료지원사업', (
            ('의료 아웃리치', '의료 아웃리치'),
            ('소녀돌봄약국지원', '소녀돌봄약국지원')
        )),
        ('교육지원사업', (
            ('성교육장이용', '성교육장이용'),
            ('찾아가는 성매매예방교육연극', '찾아가는 성매매예방교육연극'),
            ('종사자교육', '종사자교육'),
        )),
        ('성건강지원사업', (
            ('성건강수첩', '성건강수첩'),
            ('찾아가는 초등성건강교육', '찾아가는 초등성건강교육'),
            ('소그룹 성건강교육', '소그룹 성건강교육'),
            ('생리대 배분', '생리대 배분'),
            ('생리대 후원 확보', '생리대 후원 확보'),
        )),
        ('네트워크', (
            ('거리, 방문홍보', '온라인 홍보'),
            ('우편홍보', '우편홍보'),
            ('내외부 직원교육', '내외부 직원교육'),
            ('네트워크 및 사업협력','네트워크 및 사업협력'),
            ('대학생 타기관 교육, 네트워킹','대학생 타기관 교육, 네트워킹'),
            ('연합사례회의, 지원협력','연합사례회의, 지원협력'),
            ('후원처 자원발굴, 관리','후원처 자원발굴, 관리'),
            ('이용자 만족도조사, 질적인터뷰 등','이용자 만족도조사, 질적인터뷰 등'),
            ('자원봉사활동','자원봉사활동'),
        )),
    )
    perfor_date = models.DateField(verbose_name='진행 날짜')
    perfor_people = models.IntegerField(verbose_name='인원')
    perfor_count = models.IntegerField(verbose_name='건수')
    perfor_program = models.CharField(choices=program_name, max_length=30, verbose_name='프로그램')

    # 기타사업등록에는 왜 안되지??????? 
    # counselor = models.ForeignKey('counselor.User', on_delete=models.CASCADE, verbose_name='상담자')


    def __str__(self):
        return self.perfor_program
    
    class Meta:
        db_table = 'program'
        verbose_name = '실적등록'
        verbose_name_plural = '실적등록'