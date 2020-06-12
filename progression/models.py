from django.db import models
from user.models import Intake, Planning

from django.utils.functional import cached_property

den = (
    ('스케일링','스케일링'),
    ('보철','보철'),
    ('충치','충치'),
    ('기타','기타'))

# diagnosis = (
#     ('평일','평일'),
#     ('야간','야간'))

level = (
    ('1차','1차'),
    ('2차','2차'),
    ('3차','3차'))

sep = (
    ('상담','상담'),
    ('수강명령','수강명령'))
# True/False 값을 int 타입으로 convert
class CustomBooleanField(models.BooleanField):
    
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value)


class Progress(models.Model):
    
    id = models.AutoField(primary_key=True)
    CT = models.ForeignKey(Intake, on_delete=models.CASCADE, verbose_name='CT')
    getplan_name = models.CharField(verbose_name='내담자 이름', max_length=10)
    getplan_date = models.DateField(null=True, verbose_name='진행 날짜')
    last_date = models.DateTimeField('마지막 수정날짜', auto_now=True)

    # 의료지원
    # 평일진료
    # inmedical_A1_select = models.CharField(blank=True, default="",choices=diagnosis, max_length=2,verbose_name='치과 구분')
    inmedical_A1_YN_1 = CustomBooleanField(default=False, verbose_name='치과 여부')
    inmedical_A1_select_1 = models.CharField(blank=True, default="",choices=den, max_length=4,verbose_name='치과 진료명')
    inmedical_A1_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A1_Text_1 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    # inmedical_A2_select = models.CharField(choices=diagnosis, blank=True, max_length=2, default="", verbose_name='여성의학 구분')
    inmedical_A2_YN_1 = CustomBooleanField(default=False, verbose_name='여성의학 여부')
    inmedical_A2_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A2_Text_1 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    # inmedical_A3_select = models.CharField(choices=diagnosis, blank=True,max_length=2, default="", verbose_name='한방의학 구분')
    inmedical_A3_YN_1 = CustomBooleanField(default=False, verbose_name='한방의학 여부')
    inmedical_A3_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A3_Text_1 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    # inmedical_A4_select = models.CharField(choices=diagnosis, blank=True,max_length=2, default="", verbose_name='가정의학 구분')
    inmedical_A4_YN_1 = CustomBooleanField(default=False, verbose_name='가정의학 여부')
    inmedical_A4_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A4_Text_1 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    # 야간진료
    inmedical_A1_YN_2 = CustomBooleanField(default=False, verbose_name='치과(야간) 여부')
    inmedical_A1_select_2 = models.CharField(blank=True, default="",choices=den, max_length=4,verbose_name='치과 진료명')
    inmedical_A1_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A1_Text_2 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    inmedical_A2_YN_2 = CustomBooleanField(default=False, verbose_name='여성의학(야간) 여부')
    inmedical_A2_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A2_Text_2 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    inmedical_A3_YN_2 = CustomBooleanField(default=False, verbose_name='한방의학(야간) 여부')
    inmedical_A3_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A3_Text_2 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    inmedical_A4_YN_2 = CustomBooleanField(default=False, verbose_name='가정의학(야간) 여부')
    inmedical_A4_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_A4_Text_2 = models.CharField(blank=True, default="", max_length=200, verbose_name='내용')
    # 
    inmedical_B1_YN = CustomBooleanField(default=False, verbose_name='여성의학검사 여부')
    inmedical_B1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_B2_YN = CustomBooleanField(default=False, verbose_name='기초검사 여부')
    inmedical_B2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_B3_YN = CustomBooleanField(default=False, verbose_name='항체검사 여부')
    inmedical_B3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_B4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_B4_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    inmedical_B4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_B4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    inmedical_C1_YN = CustomBooleanField(default=False, verbose_name='치료제 여부')
    inmedical_C1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_C2_YN = CustomBooleanField(default=False, verbose_name='영양제 여부')
    inmedical_C2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_C3_YN = CustomBooleanField(default=False, verbose_name='임신테스트기 여부')
    inmedical_C3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C3_F = models.IntegerField(null=True, blank=True, default=0, verbose_name='수량')
    inmedical_C3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_C4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타1 이름')
    inmedical_C4_YN = CustomBooleanField(default=False, verbose_name='기타1 여부')
    inmedical_C4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_C5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타2 이름')
    inmedical_C5_YN = CustomBooleanField(default=False, verbose_name='기타2 여부')
    inmedical_C5_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_C5_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    inmedical_D1_YN = CustomBooleanField(default=False, verbose_name='간염 여부')
    inmedical_D1_Num = models.CharField(blank=True, default="",choices=level, max_length=3,verbose_name='간염 차수')
    inmedical_D1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_D2_YN = CustomBooleanField(default=False, verbose_name='자궁경부암 여부')
    inmedical_D2_Num = models.CharField(blank=True, default="",choices=level, max_length=3,verbose_name='자궁경부암 차수')
    inmedical_D2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_D3_YN = CustomBooleanField(default=False, verbose_name='독감예방 여부')
    inmedical_D3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_D4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D4_YN = CustomBooleanField(default=False, verbose_name='기타1 여부')
    inmedical_D4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_D5_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D5_YN = CustomBooleanField(default=False, verbose_name='기타2 여부')
    inmedical_D5_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D5_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_D6_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_D6_YN = CustomBooleanField(default=False, verbose_name='기타3 여부')
    inmedical_D6_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_D6_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    inmedical_E1_YN = CustomBooleanField(default=False, verbose_name='외부병원(치과) 여부')
    inmedical_E1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_E2_YN = CustomBooleanField(default=False, verbose_name='외부병원(여성) 여부')
    inmedical_E2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_E3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_E3_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    inmedical_E3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_E3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    inmedical_F1_YN = CustomBooleanField(default=False, verbose_name='잇솔질교육 여부')
    inmedical_F1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_F1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_F2_YN = CustomBooleanField(default=False, verbose_name='안경지원 여부')
    inmedical_F2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_F2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_F3_YN = CustomBooleanField(default=False, verbose_name='몸펴기운동 지원 여부')
    inmedical_F3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_F3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_F4_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmedical_F4_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    inmedical_F4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_F4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    inmedical_G1_YN = CustomBooleanField(default=False, verbose_name='의료상담(대면) 여부')
    inmedical_G1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_G1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_G2_YN = CustomBooleanField(default=False, verbose_name='의료상담(전화) 여부')
    inmedical_G2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_G2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmedical_G3_YN = CustomBooleanField(default=False, verbose_name='의료상담(SNS) 여부')
    inmedical_G3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmedical_G3_Text = models.CharField(blank=True,max_length=200, verbose_name='내용')
    # 심리지원
    inmental_A1_YN = CustomBooleanField(default=False, verbose_name='정신보건상담(대면) 여부')
    inmental_A1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_A1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmental_A2_YN = CustomBooleanField(default=False, verbose_name='정신보건상담(전화) 여부')
    inmental_A2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_A2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')

    inmental_B1_YN = CustomBooleanField(default=False, verbose_name='종합심리검사 여부')
    inmental_B1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_B1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmental_B2_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmental_B2_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    inmental_B2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_B2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    
    inmental_C1_YN = CustomBooleanField(default=False, verbose_name='원예치료 여부')
    inmental_C1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_C1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmental_C2_YN = CustomBooleanField(default=False, verbose_name='몸치유 여부')
    inmental_C2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_C2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    inmental_C3_name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    inmental_C3_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    inmental_C3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    inmental_C3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')

    
    # 사례관리
    # incase_A1_select_1 = models.CharField(blank=True, default="",choices=sep, max_length=5,verbose_name='대면 구분')
    incase_A1_YN_1 = CustomBooleanField(default=False, verbose_name='대면 여부')
    incase_A1_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A1_Text_1 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    # incase_A2_select_1 = models.CharField(blank=True, default="",choices=sep, max_length=5,verbose_name='심층 구분')
    incase_A2_YN_1 = CustomBooleanField(default=False, verbose_name='심층 여부')
    incase_A2_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A2_Text_1 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    # incase_A3_select_1 = models.CharField(blank=True, default="",choices=sep, max_length=5,verbose_name='전화 구분')
    incase_A3_YN_1 = CustomBooleanField(default=False, verbose_name='전화 여부')
    incase_A3_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A3_Text_1 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    # incase_A4_select_1 = models.CharField(blank=True, default="",choices=sep, max_length=5,verbose_name='SNS 구분')
    incase_A4_YN_1 = CustomBooleanField(default=False, verbose_name='SNS 여부')
    incase_A4_C_1 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A4_Text_1 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    # 수강명령
    incase_A1_YN_2 = CustomBooleanField(default=False, verbose_name='대면(수강명령) 여부')
    incase_A1_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A1_Text_2 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A2_YN_2 = CustomBooleanField(default=False, verbose_name='심층(수강명령) 여부')
    incase_A2_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A2_Text_2 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A3_YN_2 = CustomBooleanField(default=False, verbose_name='전화(수강명령) 여부')
    incase_A3_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A3_Text_2 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_A4_YN_2 = CustomBooleanField(default=False, verbose_name='SNS(수강명령) 여부')
    incase_A4_C_2 = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_A4_Text_2 = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    incase_B1_YN = CustomBooleanField(default=False, verbose_name='성건강 여부')
    incase_B1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_B1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_B2_YN = CustomBooleanField(default=False, verbose_name='관계 여부')
    incase_B2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_B2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_B3_Name = models.CharField(blank=True, default='', max_length=15, verbose_name='기타 이름')
    incase_B3_YN = CustomBooleanField(default=False, verbose_name='기타 여부')
    incase_B3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_B3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    #
    incase_C1_YN = CustomBooleanField(default=False, verbose_name='먹거리 여부')
    incase_C1_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_C1_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_C2_YN = CustomBooleanField(default=False, verbose_name='물품 여부')
    incase_C2_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_C2_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_C3_YN = CustomBooleanField(default=False, verbose_name='교통비 여부')
    incase_C3_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_C3_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_C4_YN = CustomBooleanField(default=False, verbose_name='자원연계 여부')
    incase_C4_C = models.IntegerField(null=True, blank=True, default=0, verbose_name='비용')
    incase_C4_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')
    incase_C5_TC = models.IntegerField(null=True, blank=True, default=0, verbose_name='총비용')
    incase_C5_Text = models.CharField(blank=True, default='', max_length=200, verbose_name='내용')

    getplan_comment = models.TextField(blank=True, default="", max_length=2000, verbose_name='comment')
    getplan_sentence = models.TextField(blank=True, default="", max_length=2000, verbose_name='sentence')

    inmedical_A_1_sum = models.IntegerField(null=True, blank=True, verbose_name='치과 SUM')
    inmedical_A_2_sum = models.IntegerField(null=True, blank=True, verbose_name='여성의학 SUM')
    inmedical_A_3_sum = models.IntegerField(null=True, blank=True, verbose_name='한방의학 SUM')
    inmedical_A_4_sum = models.IntegerField(null=True, blank=True, verbose_name='가정의학 SUM')
    inmedical_A_sum = models.IntegerField(null=True, blank=True, verbose_name='진료 SUM')
    inmedical_B_sum = models.IntegerField(null=True, blank=True, verbose_name='각종검사 SUM')
    inmedical_C_sum = models.IntegerField(null=True, blank=True, verbose_name='약지급 SUM')
    inmedical_D_sum = models.IntegerField(null=True, blank=True, verbose_name='예방접종 SUM')
    inmedical_E_sum = models.IntegerField(null=True, blank=True, verbose_name='외부병원 SUM')
    inmedical_F_sum = models.IntegerField(null=True, blank=True, verbose_name='예방의학 SUM')
    inmedical_G_sum = models.IntegerField(null=True, blank=True, verbose_name='의료상담 SUM')  # 차트에는 포함 x
    inmental_A_sum = models.IntegerField(null=True, blank=True, verbose_name='정신보건 SUM')
    inmental_B_sum = models.IntegerField(null=True, blank=True, verbose_name='심리검사 SUM')
    inmental_C_sum = models.IntegerField(null=True, blank=True, verbose_name='심리정서지원 SUM')
    incase_A_sum = models.IntegerField(null=True, blank=True, verbose_name='상담 SUM')
    incase_B_sum = models.IntegerField(null=True, blank=True, verbose_name='1:1교육 SUM')
    incase_C_sum = models.IntegerField(null=True, blank=True, verbose_name='기초생활지원 SUM')

    inmedical_A_1_cost = models.IntegerField(null=True, blank=True, verbose_name='치과 cost')
    inmedical_A_2_cost = models.IntegerField(null=True, blank=True, verbose_name='여성의학 cost')
    inmedical_A_3_cost = models.IntegerField(null=True, blank=True, verbose_name='한방의학 cost')
    inmedical_A_4_cost = models.IntegerField(null=True, blank=True, verbose_name='가정의학 cost')
    inmedical_A_cost = models.IntegerField(null=True, blank=True, verbose_name='진료 cost')
    inmedical_B_cost = models.IntegerField(null=True, blank=True, verbose_name='각종검사 cost')
    inmedical_C_cost = models.IntegerField(null=True, blank=True, verbose_name='약지급 cost')
    inmedical_D_cost = models.IntegerField(null=True, blank=True, verbose_name='예방접종 cost')
    inmedical_E_cost = models.IntegerField(null=True, blank=True, verbose_name='외부병원 cost')
    inmedical_F_cost = models.IntegerField(null=True, blank=True, verbose_name='예방의학 cost')
    inmedical_G_cost = models.IntegerField(null=True, blank=True, verbose_name='의료상담 cost')  # 차트에는 포함 x
    inmental_A_cost = models.IntegerField(null=True, blank=True, verbose_name='정신보건 cost')
    inmental_B_cost = models.IntegerField(null=True, blank=True, verbose_name='심리검사 cost')
    inmental_C_cost = models.IntegerField(null=True, blank=True, verbose_name='심리정서지원 cost')
    incase_A_cost = models.IntegerField(null=True, blank=True, verbose_name='상담 cost')
    incase_B_cost = models.IntegerField(null=True, blank=True, verbose_name='1:1교육 cost')
    incase_C_cost = models.IntegerField(null=True, blank=True, verbose_name='기초생활지원 cost')

    def save(self, *args, **kwargs):
        self.inmedical_A_1_sum = self.inmedical_A1_YN_1 + self.inmedical_A1_YN_2
        self.inmedical_A_2_sum = self.inmedical_A2_YN_1 + self.inmedical_A2_YN_2
        self.inmedical_A_3_sum = self.inmedical_A3_YN_1 + self.inmedical_A3_YN_2
        self.inmedical_A_4_sum = self.inmedical_A4_YN_1 + self.inmedical_A4_YN_2
        self.inmedical_A_sum = self.inmedical_A1_YN_1 + self.inmedical_A2_YN_1 + self.inmedical_A3_YN_1 + self.inmedical_A4_YN_1
        self.inmedical_B_sum = self.inmedical_B1_YN + self.inmedical_B2_YN + self.inmedical_B3_YN + self.inmedical_B4_YN
        self.inmedical_C_sum = self.inmedical_C1_YN + self.inmedical_C2_YN + self.inmedical_C3_YN + self.inmedical_C4_YN + self.inmedical_C5_YN
        self.inmedical_D_sum = self.inmedical_D1_YN + self.inmedical_D2_YN + self.inmedical_D3_YN + self.inmedical_D4_YN + self.inmedical_D5_YN + self.inmedical_D6_YN
        self.inmedical_E_sum = self.inmedical_E1_YN + self.inmedical_E2_YN + self.inmedical_E3_YN
        self.inmedical_F_sum = self.inmedical_F1_YN + self.inmedical_F2_YN + self.inmedical_F3_YN + self.inmedical_F4_YN
        self.inmedical_G_sum = self.inmedical_G1_YN + self.inmedical_G2_YN + self.inmedical_G3_YN
        self.inmental_A_sum = self.inmental_A1_YN + self.inmental_A2_YN
        self.inmental_B_sum = self.inmental_B1_YN + self.inmental_B2_YN
        self.inmental_C_sum = self.inmental_C1_YN + self.inmental_C2_YN + self.inmental_C3_YN
        self.incase_A_sum = self.incase_A1_YN_1 + self.incase_A2_YN_1 + self.incase_A3_YN_1 + self.incase_A4_YN_1
        self.incase_B_sum = self.incase_B1_YN + self.incase_B2_YN + self.incase_B3_YN
        self.incase_C_sum = self.incase_C1_YN + self.incase_C2_YN + self.incase_C3_YN + self.incase_C4_YN
        self.inmedical_A_1_cost = self.inmedical_A1_C_1 + self.inmedical_A1_C_2
        self.inmedical_A_2_cost = self.inmedical_A2_C_1 + self.inmedical_A2_C_2
        self.inmedical_A_3_cost = self.inmedical_A3_C_1 + self.inmedical_A3_C_2
        self.inmedical_A_4_cost = self.inmedical_A4_C_1 + self.inmedical_A4_C_2
        self.inmedical_A_cost = self.inmedical_A1_C_1 + self.inmedical_A2_C_1 + self.inmedical_A3_C_1 + self.inmedical_A4_C_1
        self.inmedical_B_cost = self.inmedical_B1_C + self.inmedical_B2_C + self.inmedical_B3_C + self.inmedical_B4_C
        self.inmedical_C_cost = self.inmedical_C1_C + self.inmedical_C2_C + self.inmedical_C3_C + self.inmedical_C4_C + self.inmedical_C5_C
        self.inmedical_D_cost = self.inmedical_D1_C + self.inmedical_D2_C + self.inmedical_D3_C + self.inmedical_D4_C + self.inmedical_D5_C + self.inmedical_D6_C
        self.inmedical_E_cost = self.inmedical_E1_C + self.inmedical_E2_C + self.inmedical_E3_C
        self.inmedical_F_cost = self.inmedical_F1_C + self.inmedical_F2_C + self.inmedical_F3_C + self.inmedical_F4_C
        self.inmedical_G_cost = self.inmedical_G1_C + self.inmedical_G2_C + self.inmedical_G3_C
        
        self.inmental_A_cost = self.inmental_A1_C + self.inmental_A2_C
        self.inmental_B_cost = self.inmental_B1_C + self.inmental_B2_C
        self.inmental_C_cost = self.inmental_C1_C + self.inmental_C2_C + self.inmental_C3_C
        self.incase_A_cost = self.incase_A1_C_1 + self.incase_A2_C_1 + self.incase_A3_C_1 + self.incase_A4_C_1
        self.incase_B_cost = self.incase_B1_C + self.incase_B2_C + self.incase_B3_C
        self.incase_C_cost = self.incase_C1_C + self.incase_C2_C + self.incase_C3_C + self.incase_C4_C
        super(Progress, self).save(*args, **kwargs)


    def __str__(self):
        return self.getplan_name

    class Meta:
        db_table = 'progress'
        verbose_name = '사례지원진행'
        verbose_name_plural = '사례지원진행'


class CTRS(models.Model):
    choices = (
        (0, "9"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"))
    reverse_choices = (
        (5, "1"),
        (4, "2"),
        (3, "3"),
        (2, "4"),
        (1, "5"),
        (0, "9"))
    label = (
        ('1차','1차'),
        ('2차','2차'),
        ('3차','3차'))

    id = models.AutoField(primary_key=True)
    CT = models.ForeignKey(Intake, on_delete=models.CASCADE, verbose_name='CT')
    danger_name = models.CharField(verbose_name='내담자 이름', max_length=10)
    danger_date = models.DateField(null=True, verbose_name='진행 날짜')
    last_date = models.DateTimeField('마지막 수정날짜', auto_now=True)
    danger_label = models.CharField(blank=True, default="",choices=label, max_length=3,verbose_name='차수')

    survey1_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='개인1')
    survey1_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='개인2')
    survey1_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='개인3')
    survey1_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='개인4')
    survey1_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='개인5')
    survey2_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='가정1')
    survey2_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='가정2')
    survey2_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='가정3')
    survey2_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='가정4')
    survey2_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='가정5')

    survey3_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='또래 및 학교1')
    survey3_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='또래 및 학교2')
    survey3_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='또래 및 학교3')
    survey3_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='또래 및 학교4')
    survey3_5 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='또래 및 학교5')
    survey4_1 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='지지체계1')
    survey4_2 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='지지체계2')
    survey4_3 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='지지체계3')
    survey4_4 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='지지체계4')

    survey5_1 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='성건강_공통1')
    survey5_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성건강_공통2')
    survey5_3 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='성건강_공통3')
    survey5_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성건강_공통4')
    survey5_5 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='성건강_공통5')

    survey6_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성건강_성관계1')
    survey6_2 = models.IntegerField(choices=reverse_choices,null=True, blank=True, verbose_name='성건강_성관계2')
    survey6_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성건강_성관계3')
    survey7_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성폭력1')
    survey7_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성폭력2')
    survey7_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='성폭력3')
    survey9_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력피해1')
    survey9_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력피해2')
    survey9_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력피해3')

    survey10_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력가해1')
    survey10_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력가해2')
    survey10_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='폭력가해3')
    survey11_1 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='정신건강1')
    survey11_2 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='정신건강2')
    survey11_3 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='정신건강3')
    survey11_4 = models.IntegerField(choices=choices,null=True, blank=True, verbose_name='정신건강4')

    ctrs_comment = models.TextField(blank=True, default="", max_length=2000, verbose_name='Commnet')
    ctrs_sentence = models.TextField(blank=True, default="", max_length=2000, verbose_name='오늘의 한줄')

    # Sum Code
    sum_1 = models.IntegerField(null=True, blank=True, verbose_name='개인 Sum')
    sum_2 = models.IntegerField(null=True, blank=True, verbose_name='가정 Sum')
    sum_3 = models.IntegerField(null=True, blank=True, verbose_name='또래 및 학교 Sum')
    sum_4 = models.IntegerField(null=True, blank=True, verbose_name='지지체계 Sum')
    sum_5 = models.IntegerField(null=True, blank=True, verbose_name='성건강_공통 Sum')
    sum_6 = models.IntegerField(null=True, blank=True, verbose_name='성건강_성관계 Sum')
    sum_7 = models.IntegerField(null=True, blank=True, verbose_name='성폭력 Sum')
    sum_9 = models.IntegerField(null=True, blank=True, verbose_name='폭력피해 Sum')
    sum_10 = models.IntegerField(null=True, blank=True, verbose_name='폭력가해 Sum')
    sum_11 = models.IntegerField(null=True, blank=True, verbose_name='정신건강 Sum')
    total = models.IntegerField(null=True, blank=True, verbose_name='Total')


    def save(self, field, *args, **kwargs):
        if type(self.field) != int:
            self.field = 0
        self.sum_1 = self.survey1_1 + self.survey1_2 + self.survey1_3 + self.survey1_4 + self.survey1_5 
        self.sum_2 = self.survey2_1 + self.survey2_2 + self.survey2_3 + self.survey2_4 + self.survey2_5
        self.sum_3 = self.survey3_1 + self.survey3_2 + self.survey3_3 + self.survey3_4 + self.survey3_5
        self.sum_4 = self.survey4_1 + self.survey4_2 + self.survey4_3 + self.survey4_4
        self.sum_5 = self.survey5_1 + self.survey5_2 + self.survey5_3 + self.survey5_4 + self.survey5_5
        self.sum_6 = self.survey6_1 + self.survey6_2 + self.survey6_3
        self.sum_7 = self.survey7_1 + self.survey7_2 + self.survey7_3
        self.sum_9 = self.survey9_1 + self.survey9_2 + self.survey9_3
        self.sum_10 = self.survey10_1 + self.survey10_2 + self.survey10_3
        self.sum_11 = self.survey11_1 + self.survey11_2 + self.survey11_3 + self.survey11_4
        self.total = self.sum_1 + self.sum_2 + self.sum_3 + self.sum_4 + self.sum_5 + self.sum_6 + self.sum_7 + self.sum_9 + self.sum_10 + self.sum_11
        super(CTRS, self).save(*args, **kwargs)

    # def sum_1(self, obj):
    #     return obj.survey1_1 + obj.survey1_2 + obj.survey1_3 + obj.survey1_4 + obj.survey1_5

    # def _get_full_name(self):
    #     # return '%s, %s %s' % (self.lastname, self.firstname, self.middlename)
    #     return self.survey1_1 + self.survey1_2 + self.survey1_3 + self.survey1_4 + self.survey1_5
    # sum_1 = property(_get_full_name)


    def __str__(self):
        return self.danger_name

    class Meta:
        db_table = 'ctrs'
        verbose_name = '위기분류척도'
        verbose_name_plural = '위기분류척도'