from django import forms
from django.forms import ModelForm

from .models import Intake, Planning, Program
from info.models import Client


# class IntakeForm(forms.ModelForm):
#     class Meta:
#         model = Intake
#         fields = '__all__'

#     # Jumin = forms.CharField(label='주민번호',required=True)
#     # created_date = forms.DateTimeField(label='작성일')

#     # if Jumin:
#     #     Jumin = str(Jumin)
#     #     if Jumin[0] == '9':
#     #         Age = 2020 - int('19' + Jumin[0:2]) + 1
#     #     elif Jumin[0] == '0' or Jumin[0] =='1':
#     #         Age = 2020 - int('20' + Jumin[0:2]) + 1
#     #     elif type(Jumin) != int:
#     #         Jumin = 0


class IntakeForm(forms.Form):
    # 개인인적사항
    Name = forms.CharField(max_length=64, required=True)
    Jumin = forms.CharField(required=True)
    Reg = forms.DateField(required=True)
    coun_choices =[
    ('이성영', '이성영'),
    ('정현재', '정현재'),
    ('김현정', '김현정'),
    ('문보라', '문보라'),
    ('박지숙', '박지숙'),
    ('김수미', '김수미'),
    ('강주연', '강주연'),
    ('노미나', '노미나'),
    ('곽은영', '곽은영')]
    Coun = forms.ChoiceField(choices=coun_choices,required=False)

    gender_choices =[
    ('남자', '남자'),
    ('여자', '여자')]
    Res_choices = [
    ('자가', '자가'),
    ('전세', '전세'),
    ('원룸(월세)', '원룸(월세)'),
    ('고시텔(월세)','고시텔(월세)'),
    ('기타','기타')]
    Yn_choices = [
	('없음', '없음'),
    ('있음', '있음')]
    His_choices = [
    ('없음','없음'),
	('전화 및 SNS', '전화 및 SNS'),
    ('대면', '대면'),
    ('기타', '기타')] 
    Rou_choices = [
	('기관', '기관'),
    ('학교', '학교'),
    ('개인신청','개인신청'),
    ('수강명령','수강명령'),
    ('친구 및 지인소개','친구 및 지인소개')]
    Ss_choices = [
	('기초수급', '기초수급'),
    ('차상위', '차상위'),
    ('의료급여','의료급여'),
    ('기타','기타')]
    Fam_choices = [
	('조손가정', '조손가정'),
    ('한부모', '한부모'),
    ('부모','부모'),
    ('독립','독립'),
    ('동거','동거'),
    ('기타','기타')]
    Edu_choices = [
	('초등','초등'),
    ('중등','중등'),
    ('고등','고등'),
    ('기타','기타')]
    Gender = forms.ChoiceField(choices=gender_choices,required=False)
    Kakao = forms.CharField(required=False)
    Address1 = forms.CharField(required=False)
    Address2 = forms.CharField(required=False)
    Tel1 = forms.CharField(required=False)
    Tel2 = forms.CharField(required=False)
    Res = forms.ChoiceField(choices=Res_choices, required=False)
    Res_text = forms.CharField(required=False)
    Fam = forms.ChoiceField(choices=Fam_choices, required=False)
    Fam_text = forms.CharField(required=False)
    Ssgrade = forms.ChoiceField(choices=Ss_choices, required=False)
    Ssgrade_text = forms.CharField(required=False)
    His = forms.ChoiceField(choices=His_choices, required=False)
    Route = forms.ChoiceField(choices=Rou_choices, required=False)
    Route_text = forms.CharField(required=False)

    Eco1 = forms.IntegerField(required=False)
    Eco2 = forms.IntegerField(required=False)
    Eco3 = forms.IntegerField(required=False)
    Eco4 = forms.IntegerField(required=False)
    Edu = forms.ChoiceField(choices=Edu_choices, required=False)
    Edu_text = forms.CharField(required=False)
    Job = forms.ChoiceField(choices=Yn_choices, required=False)
    Job_text = forms.CharField(required=False)
    Disorder = forms.ChoiceField(choices=Yn_choices, required=False)
    Disorder_text = forms.CharField(required=False)
    Other = forms.CharField(required=False)

    Institute = forms.CharField(required=False)
    Incharge_name = forms.CharField(required=False)
    Incharge_tel = forms.CharField(required=False)


    def clean(self):
        cleaned_data = super().clean()
        # 개인인적사항
        Name = cleaned_data.get('Name')
        Reg = cleaned_data.get('Reg')
        Jumin = cleaned_data.get('Jumin')
        Coun = cleaned_data.get('Coun')
        Gender = cleaned_data.get('Gender')
        Kakao = cleaned_data.get('Kakao')
        Address1 = cleaned_data.get('Address1')
        Address2 = cleaned_data.get('Address2')
        Tel1 = cleaned_data.get('Tel1')
        Tel2 = cleaned_data.get('Tel2')
        Res = cleaned_data.get('Res')
        Res_text = cleaned_data.get('Res_text')
        Fam = cleaned_data.get('Fam')
        Fam_text = cleaned_data.get('Fam_text')
        Ssgrade = cleaned_data.get('Ssgrade')
        Ssgrade_text = cleaned_data.get('Ssgrade_text')
        His = cleaned_data.get('His')
        Route = cleaned_data.get('Route')
        Route_text = cleaned_data.get('Route_text')
        Eco1 = cleaned_data.get('Eco1')
        Eco2 = cleaned_data.get('Eco2')
        Eco3 = cleaned_data.get('Eco3')
        Eco4 = cleaned_data.get('Eco4')
        Edu = cleaned_data.get('Edu')
        Edu_text = cleaned_data.get('Edu_text')
        Job = cleaned_data.get('Job')
        Job_text = cleaned_data.get('Job_text')
        Disorder = cleaned_data.get('Disorder')
        Disorder_text = cleaned_data.get('Disorder_text')
        Other = cleaned_data.get('Other')
        Institute = cleaned_data.get('Institute')
        Incharge_name = cleaned_data.get('Incharge_name')
        Incharge_tel = cleaned_data.get('Incharge_tel')


        if Jumin:
            if Jumin[0] == '9':
                Age = 2020 - int('19' + Jumin[0:2]) + 1
            elif Jumin[0] == '0' or Jumin[0] =='1':
                Age = 2020 - int('20' + Jumin[0:2]) + 1
            elif type(Jumin) != int:
                Jumin = 0
        else:0

        # 개인인적사항 db
        intake = Intake(
            Name=Name,
            Reg=Reg,
            Jumin=Jumin,
            Age=Age,
            Coun=Coun,
            Gender=Gender,
            Kakao=Kakao,
            Address1=Address1,
            Address2=Address2,
            Tel1=Tel1,
            Tel2=Tel2,
            Res=Res,
            Res_text= Res_text,
            Fam=Fam,
            Fam_text=Fam_text,
            Ssgrade=Ssgrade,
            Ssgrade_text=Ssgrade_text,
            His=His,
            Route=Route,
            Route_text=Route_text,
            Eco1=Eco1,
            Eco2=Eco2,
            Eco3=Eco3,
            Eco4=Eco4,
            Edu=Edu,
            Edu_text=Edu_text,
            Job=Job,
            Job_text=Job_text,
            Disorder=Disorder,
            Disorder_text=Disorder_text,
            Other=Other,
            Institute= Institute,
            Incharge_name= Incharge_name,
            Incharge_tel= Incharge_tel

        )
        intake.save()

        client = Client(
            # id=id,
            name=Name,
            reg=Reg,
            coun=Coun,
            gender=Gender,
            age=Age
        )
        client.save()


class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = '__all__'
        # fields = ['setplan_name', 'medical_A1_MF','medical_A1_TF','medical_A1_Text']


# class PlanningForm(forms.Form):
#     #의료지원
#     medical_start = forms.DateField()
#     medical_end = forms.DateField()
#     mental_start = forms.DateField()
#     mental_end = forms.DateField()
#     case_start = forms.DateField()
#     case_end = forms.DateField()
#     CT = forms.ChoiceField(widget=forms.HiddenInput)
#     ctname = forms.CharField(max_length=10, label='이름',required=False)
#     medical_A1_MF = forms.IntegerField(required=False, initial=0)
#     medical_A1_TF = forms.IntegerField(initial=0)
#     medical_A1_Text = forms.CharField(max_length=100, required=False)
#     medical_A2_MF = forms.IntegerField(required=False)
#     medical_A2_TF = forms.IntegerField()
#     medical_A2_Text = forms.CharField(max_length=100, required=False)
#     medical_A3_MF = forms.IntegerField()
#     medical_A3_TF = forms.IntegerField()
#     medical_A3_Text = forms.CharField(max_length=100, required=False)
#     medical_A4_MF = forms.IntegerField()
#     medical_A4_TF = forms.IntegerField()
#     medical_A4_Text = forms.CharField(max_length=100, required=False)
#     medical_B1_YN = forms.BooleanField(required=False)
#     medical_B1_Text = forms.CharField(max_length=100, required=False)
#     medical_B2_YN = forms.BooleanField(required=False)
#     medical_B2_Text = forms.CharField(max_length=100, required=False)
#     medical_B3_YN = forms.BooleanField(required=False)
#     medical_B3_Text = forms.CharField(max_length=100, required=False)
#     medical_B4_Name = forms.CharField(max_length=15, required=False)
#     medical_B4_YN = forms.BooleanField(required=False)
#     medical_B4_Text = forms.CharField(max_length=100, required=False)

#     medical_C1_MF = forms.IntegerField()
#     medical_C1_TF = forms.IntegerField()
#     medical_C1_Text = forms.CharField(max_length=100, required=False)
#     medical_C2_MF = forms.IntegerField()
#     medical_C2_TF = forms.IntegerField()
#     medical_C2_Text = forms.CharField(max_length=100, required=False)
#     medical_C3_MF = forms.IntegerField()
#     medical_C3_TF = forms.IntegerField()
#     medical_C3_Text = forms.CharField(max_length=100, required=False)
#     medical_C4_Name = forms.CharField(max_length=15, required=False)
#     medical_C4_MF = forms.IntegerField()
#     medical_C4_TF = forms.IntegerField()
#     medical_C4_Text = forms.CharField(max_length=10, required=False)
#     medical_C5_Name = forms.CharField(max_length=15, required=False)
#     medical_C5_MF = forms.IntegerField()
#     medical_C5_TF = forms.IntegerField()
#     medical_C5_Text = forms.CharField(max_length=100, required=False)

#     medical_D1_Num = forms.IntegerField()
#     medical_D1_Text = forms.CharField(max_length=100, required=False)
#     medical_D2_Num = forms.IntegerField()
#     medical_D2_Text = forms.CharField(max_length=100, required=False)
#     medical_D3_YN = forms.BooleanField(required=False)
#     medical_D3_Text = forms.CharField(max_length=100, required=False)
#     medical_D4_Name = forms.CharField(max_length=15, required=False)
#     medical_D4_TF = forms.IntegerField()
#     medical_D4_Text = forms.CharField(max_length=100, required=False)
#     medical_D5_Name = forms.CharField(max_length=15, required=False)
#     medical_D5_TF = forms.IntegerField()
#     medical_D5_Text = forms.CharField(max_length=100, required=False)
#     medical_D6_Name = forms.CharField(max_length=15, required=False)
#     medical_D6_TF = forms.IntegerField()
#     medical_D6_Text = forms.CharField(max_length=100, required=False)

#     medical_E1_MF = forms.IntegerField()
#     medical_E1_TF = forms.IntegerField()
#     medical_E1_Text = forms.CharField(max_length=100, required=False)
#     medical_E2_MF = forms.IntegerField()
#     medical_E2_TF = forms.IntegerField()
#     medical_E2_Text = forms.CharField(max_length=100, required=False)
#     medical_E3_Name = forms.CharField(max_length=15, required=False)
#     medical_E3_MF = forms.IntegerField()
#     medical_E3_TF = forms.IntegerField()
#     medical_E3_Text = forms.CharField(max_length=100, required=False)

#     medical_F1_MF = forms.IntegerField()
#     medical_F1_TF = forms.IntegerField()
#     medical_F1_Text = forms.CharField(max_length=100, required=False)
#     medical_F2_MF = forms.IntegerField()
#     medical_F2_TF = forms.IntegerField()
#     medical_F2_Text = forms.CharField(max_length=100, required=False)
#     medical_F3_MF = forms.IntegerField()
#     medical_F3_TF = forms.IntegerField()
#     medical_F3_Text = forms.CharField(max_length=100, required=False)
#     medical_F4_Name = forms.CharField(max_length=15, required=False)
#     medical_F4_MF = forms.IntegerField()
#     medical_F4_TF = forms.IntegerField()
#     medical_F4_Text = forms.CharField(max_length=100, required=False)

#     # 심리지원
#     # mental_A1_MF = forms.IntegerField()
#     # mental_A1_TF = forms.IntegerField()
#     # mental_A1_Text = forms.CharField(max_length=100, required=False)
#     # mental_A2_MF = forms.IntegerField()
#     # mental_A2_TF = forms.IntegerField()
#     # mental_A2_Text = forms.CharField(max_length=100, required=False)
#     # mental_B1_TF = forms.IntegerField()
#     # mental_B2_Name = forms.CharField(max_length=15, required=False)
#     # mental_B2_TF = forms.IntegerField()
#     # mental_C1_MF = forms.IntegerField()
#     # mental_C1_TF = forms.IntegerField()
#     # mental_C1_Text = forms.CharField(max_length=100, required=False)
#     # mental_C2_MF = forms.IntegerField()
#     # mental_C2_TF = forms.IntegerField()
#     # mental_C2_Text = forms.CharField(max_length=100, required=False)
#     # mental_C3_Name = forms.CharField(max_length=15, required=False)
#     # mental_C3_MF = forms.IntegerField()
#     # mental_C3_TF = forms.IntegerField()
#     # mental_C3_Text = forms.CharField(max_length=100, required=False)

#     # # 사례지원
#     # case_A1_MF = forms.IntegerField()
#     # case_A1_TF = forms.IntegerField()
#     # case_A1_Text = forms.CharField(max_length=300, required=False)
#     # case_A2_MF = forms.IntegerField()
#     # case_A2_TF = forms.IntegerField()
#     # case_A2_Text = forms.CharField(max_length=300, required=False)
#     # case_A3_MF = forms.IntegerField()
#     # case_A3_TF = forms.IntegerField()
#     # case_A3_Text = forms.CharField(max_length=300, required=False)
#     # case_A4_MF = forms.IntegerField()
#     # case_A4_TF = forms.IntegerField()
#     # case_A4_Text = forms.CharField(max_length=300, required=False)
#     # case_B1_MF = forms.IntegerField()
#     # case_B1_TF = forms.IntegerField()
#     # case_B1_Text = forms.CharField(max_length=100, required=False)
#     # case_B2_MF = forms.IntegerField()
#     # case_B2_TF = forms.IntegerField()
#     # case_B2_Text = forms.CharField(max_length=100, required=False)
#     # case_B3_Name = forms.CharField(max_length=15, required=False)
#     # case_B3_MF = forms.IntegerField()
#     # case_B3_TF = forms.IntegerField()
#     # case_B3_Text = forms.CharField(max_length=100, required=False)
#     # case_C1_MF = forms.IntegerField()
#     # case_C1_TF = forms.IntegerField()
#     # case_C1_Text = forms.CharField(max_length=100, required=False)
#     # case_C2_MF = forms.IntegerField()
#     # case_C2_TF = forms.IntegerField()
#     # case_C2_Text = forms.CharField(max_length=100, required=False)
#     # case_C3_MF = forms.IntegerField()
#     # case_C3_TF = forms.IntegerField()
#     # case_C3_Text = forms.CharField(max_length=100, required=False)
#     # case_C4_MF = forms.IntegerField()
#     # case_C4_TF = forms.IntegerField()
#     # case_C4_Text = forms.CharField(max_length=100, required=False)

#     # setplan_comment = forms.CharField(widget=forms.Textarea)
#     # setplan_sentence = forms.CharField(widget=forms.Textarea)

    
    

#     def clean(self):
#         cleaned_data = super().clean()
#         medical_start = cleaned_data.get('medical_start')
#         medical_end = cleaned_data.get('medical_end')
#         CT = cleaned_data.get('CT')
#         # 의료지원
#         ctname = cleaned_data.get('ctname')
#         medical_A1_MF = cleaned_data.get('medical_A1_MF')
#         medical_A1_TF = cleaned_data.get('medical_A1_TF')
#         medical_A1_Text = cleaned_data.get('medical_A1_Text')
#         medical_A2_MF = cleaned_data.get('medical_A2_MF')
#         medical_A2_TF = cleaned_data.get('medical_A2_TF')
#         medical_A2_Text = cleaned_data.get('medical_A2_Text')
#         medical_A3_MF = cleaned_data.get('medical_A3_MF')
#         medical_A3_TF = cleaned_data.get('medical_A3_TF')
#         medical_A3_Text = cleaned_data.get('medical_A3_Text')
#         medical_A4_MF = cleaned_data.get('medical_A4_MF')
#         medical_A4_TF = cleaned_data.get('medical_A4_TF')
#         medical_A4_Text = cleaned_data.get('medical_A4_Text')
#         medical_B1_YN = cleaned_data.get('medical_B1_YN')
#         medical_B1_Text = cleaned_data.get('medical_B1_Text')
#         medical_B2_YN = cleaned_data.get('medical_B2_YN')
#         medical_B2_Text = cleaned_data.get('medical_B2_Text')
#         medical_B3_YN = cleaned_data.get('medical_B3_YN')
#         medical_B3_Text = cleaned_data.get('medical_B3_Text')
#         medical_B4_YN = cleaned_data.get('medical_B4_YN')
#         medical_B4_Name = cleaned_data.get('medical_B4_Name')
#         medical_B4_Text = cleaned_data.get('medical_B4_Text')

#         medical_C1_MF = cleaned_data.get('medical_C1_MF')
#         medical_C1_TF = cleaned_data.get('medical_C1_TF')
#         medical_C1_Text = cleaned_data.get('medical_C1_Text')
#         medical_C2_MF = cleaned_data.get('medical_C2_MF')
#         medical_C2_TF = cleaned_data.get('medical_C2_TF')
#         medical_C2_Text = cleaned_data.get('medical_C2_Text')
#         medical_C3_MF = cleaned_data.get('medical_C3_MF')
#         medical_C3_TF = cleaned_data.get('medical_C3_TF')
#         medical_C3_Text = cleaned_data.get('medical_C3_Text')
#         medical_C4_Name = cleaned_data.get('medical_C4_Name')
#         medical_C4_MF = cleaned_data.get('medical_C4_MF')
#         medical_C4_TF = cleaned_data.get('medical_C4_TF')
#         medical_C4_Text = cleaned_data.get('medical_C4_Text')
#         medical_C5_Name = cleaned_data.get('medical_C5_Name')
#         medical_C5_MF = cleaned_data.get('medical_C5_MF')
#         medical_C5_TF = cleaned_data.get('medical_C5_TF')
#         medical_C5_Text = cleaned_data.get('medical_C5_Text')

#         medical_D1_Num = cleaned_data.get('medical_D1_Num')
#         medical_D1_Text = cleaned_data.get('medical_D1_Text')
#         medical_D2_Num = cleaned_data.get('medical_D2_Num')
#         medical_D2_Text = cleaned_data.get('medical_D2_Text')
#         medical_D3_YN = cleaned_data.get('medical_D3_YN')
#         medical_D3_Text = cleaned_data.get('medical_D3_Text')
#         medical_D4_Name = cleaned_data.get('medical_D4_Name')
#         medical_D4_TF = cleaned_data.get('medical_D4_TF')
#         medical_D4_Text = cleaned_data.get('medical_D4_Text')
#         medical_D5_Name = cleaned_data.get('medical_D5_Name')
#         medical_D5_TF = cleaned_data.get('medical_D5_TF')
#         medical_D5_Text = cleaned_data.get('medical_D5_Text')
#         medical_D6_Name = cleaned_data.get('medical_D6_Name')
#         medical_D6_TF = cleaned_data.get('medical_D6_TF')
#         medical_D6_Text = cleaned_data.get('medical_D6_Text')

#         medical_E1_MF = cleaned_data.get('medical_E1_MF')
#         medical_E1_TF = cleaned_data.get('medical_E1_TF')
#         medical_E1_Text = cleaned_data.get('medical_E1_Text')
#         medical_E2_MF = cleaned_data.get('medical_E2_MF')
#         medical_E2_TF = cleaned_data.get('medical_E2_TF')
#         medical_E2_Text = cleaned_data.get('medical_E2_Text')
#         medical_E3_Name = cleaned_data.get('medical_E3_Name')
#         medical_E3_MF = cleaned_data.get('medical_E3_MF')
#         medical_E3_TF = cleaned_data.get('medical_E3_TF')
#         medical_E3_Text = cleaned_data.get('medical_E3_Text')

#         medical_F1_MF = cleaned_data.get('medical_F1_MF')
#         medical_F1_TF = cleaned_data.get('medical_F1_TF')
#         medical_F1_Text = cleaned_data.get('medical_F1_Text')
#         medical_F2_MF = cleaned_data.get('medical_F2_MF')
#         medical_F2_TF = cleaned_data.get('medical_F2_TF')
#         medical_F2_Text = cleaned_data.get('medical_F2_Text')
#         medical_F3_MF = cleaned_data.get('medical_F3_MF')
#         medical_F3_TF = cleaned_data.get('medical_F3_TF')
#         medical_F3_Text = cleaned_data.get('medical_F3_Text')
#         medical_F4_Name = cleaned_data.get('medical_F4_Name')
#         medical_F4_MF = cleaned_data.get('medical_F4_MF')
#         medical_F4_TF = cleaned_data.get('medical_F4_TF')
#         medical_F4_Text = cleaned_data.get('medical_F4_Text')

#         # 심리지원
#         # mental_start = cleaned_data.get('mental_start')
#         # mental_end = cleaned_data.get('mental_end')
        
#         # mental_A1_MF = cleaned_data.get('mental_A1_MF')
#         # mental_A1_TF = cleaned_data.get('mental_A1_TF')
#         # mental_A1_Text = cleaned_data.get('mental_A1_Text')
#         # mental_A2_MF = cleaned_data.get('mental_A2_MF')
#         # mental_A2_TF = cleaned_data.get('mental_A2_TF')
#         # mental_A2_Text = cleaned_data.get('mental_A2_Text')
#         # mental_B1_TF = cleaned_data.get('mental_B1_TF')
#         # mental_B2_Name = cleaned_data.get('mental_B2_Name')
#         # mental_B2_TF = cleaned_data.get('mental_B2_TF')
#         # mental_C1_MF = cleaned_data.get('mental_C1_MF')
#         # mental_C1_TF = cleaned_data.get('mental_C1_TF')
#         # mental_C1_Text = cleaned_data.get('mental_C1_Text')
#         # mental_C2_MF = cleaned_data.get('mental_C2_MF')
#         # mental_C2_TF = cleaned_data.get('mental_C2_TF')
#         # mental_C2_Text = cleaned_data.get('mental_C2_Text')
#         # mental_C3_Name = cleaned_data.get('mental_C3_Name')
#         # mental_C3_MF = cleaned_data.get('mental_C3_MF')
#         # mental_C3_TF = cleaned_data.get('mental_C3_TF')
#         # mental_C3_Text = cleaned_data.get('mental_C3_Text')

#         # # 사례지원
#         # case_start = cleaned_data.get('case_start')
#         # case_end = cleaned_data.get('case_end')

#         # case_A1_MF = cleaned_data.get('case_A1_MF')
#         # case_A1_TF = cleaned_data.get('case_A1_TF = cleaned_data')
#         # case_A1_Text = cleaned_data.get('case_A1_Text')
#         # case_A2_MF = cleaned_data.get('case_A2_MF')
#         # case_A2_TF = cleaned_data.get('case_A2_TF')
#         # case_A2_Text = cleaned_data.get('case_A2_Text')
#         # case_A3_MF = cleaned_data.get('case_A3_MF')
#         # case_A3_TF = cleaned_data.get('case_A3_TF')
#         # case_A3_Text = cleaned_data.get('case_A3_Text')
#         # case_A4_MF = cleaned_data.get('case_A4_MF')
#         # case_A4_TF = cleaned_data.get('case_A4_TF')
#         # case_A4_Text = cleaned_data.get('case_A4_Text')
#         # case_B1_MF = cleaned_data.get('case_B1_MF')
#         # case_B1_TF = cleaned_data.get('case_B1_TF')
#         # case_B1_Text = cleaned_data.get('case_B1_Text')
#         # case_B2_MF = cleaned_data.get('case_B2_MF')
#         # case_B2_TF = cleaned_data.get('case_B2_TF')
#         # case_B2_Text = cleaned_data.get('case_B2_Text')
#         # case_B3_Name = cleaned_data.get('case_B3_Name')
#         # case_B3_MF = cleaned_data.get('case_B3_MF')
#         # case_B3_TF = cleaned_data.get('case_B3_TF')
#         # case_B3_Text = cleaned_data.get('case_B3_Text')
#         # case_C1_MF = cleaned_data.get('case_C1_MF')
#         # case_C1_TF = cleaned_data.get('case_C1_TF')
#         # case_C1_Text = cleaned_data.get('case_C1_Text')
#         # case_C2_MF = cleaned_data.get('case_C2_MF')
#         # case_C2_TF = cleaned_data.get('case_C2_TF')
#         # case_C2_Text = cleaned_data.get('case_C2_Text')
#         # case_C3_MF = cleaned_data.get('case_C3_MF')
#         # case_C3_TF = cleaned_data.get('case_C3_TF')
#         # case_C3_Text = cleaned_data.get('case_C3_Text')
#         # case_C4_MF = cleaned_data.get('case_C4_MF')
#         # case_C4_TF = cleaned_data.get('case_C4_TF')
#         # case_C4_Text = cleaned_data.get('case_C4_Text')
#         # setplan_comment = cleaned_data.get('setplan_comment')
#         # setplan_sentence = cleaned_data.get('setplan_sentence')

#         # if type(medical_A1_TF) != int:
#         #     medical_A1_TF = 0
#         # if type(medical_A2_TF) != int:
#         #     medical_A2_TF = 0
#         # if type(medical_A3_TF) != int:
#         #     medical_A3_TF = 0
#         # if type(medical_A4_TF) != int:
#         #     medical_A4_TF = 0

#         # if type(medical_C1_TF) != int:
#         #     medical_C1_TF = 0
#         # if type(medical_C2_TF) != int:
#         #     medical_C2_TF = 0
#         # if type(medical_C3_TF) != int:
#         #     medical_C3_TF = 0
#         # if type(medical_C4_TF) != int:
#         #     medical_C4_TF = 0
#         # if type(medical_C5_TF) != int:
#         #     medical_C5_TF = 0

#         # if type(medical_D1_Num) != int:
#         #     medical_D1_Num = 0
#         # if type(medical_D2_Num) != int:
#         #     medical_D2_Num = 0
#         # if type(medical_D4_TF) != int:
#         #     medical_D4_TF = 0
#         # if type(medical_D5_TF) != int:
#         #     medical_D5_TF = 0
#         # if type(medical_D6_TF) != int:
#         #     medical_D6_TF = 0

#         # if type(medical_E1_TF) != int:
#         #     medical_E1_TF = 0
#         # if type(medical_E2_TF) != int:
#         #     medical_E2_TF = 0
#         # if type(medical_E3_TF) != int:
#         #     medical_E3_TF = 0

#         # if type(medical_F1_TF) != int:
#         #     medical_F1_TF = 0
#         # if type(medical_F2_TF) != int:
#         #     medical_F2_TF = 0
#         # if type(medical_F3_TF) != int:
#         #     medical_F3_TF = 0
#         # if type(medical_F4_TF) != int:
#         #     medical_F4_TF = 0

#         # if type(mental_A1_TF) != int:
#         #     mental_A1_TF = 0
#         # if type(mental_A2_TF) != int:
#         #     mental_A2_TF = 0

#         # if type(mental_B1_TF) != int:
#         #     mental_B1_TF = 0
#         # if type(mental_B2_TF) != int:
#         #     mental_B2_TF = 0

#         # if type(mental_C1_TF) != int:
#         #     mental_C1_TF = 0
#         # if type(mental_C2_TF) != int:
#         #     mental_C2_TF = 0
#         # if type(mental_C3_TF) != int:
#         #     mental_C3_TF = 0

#         # if type(case_A1_TF) != int:
#         #     case_A1_TF = 0
#         # if type(case_A2_TF) != int:
#         #     case_A2_TF = 0
#         # if type(case_A3_TF) != int:
#         #     case_A3_TF = 0
#         # if type(case_A4_TF) != int:
#         #     case_A4_TF = 0
        
#         # if type(case_B1_TF) != int:
#         #     case_B1_TF = 0
#         # if type(case_B2_TF) != int:
#         #     case_B2_TF = 0
#         # if type(case_B3_TF) != int:
#         #     case_B3_TF = 0

#         # if type(case_C1_TF) != int:
#         #     case_C1_TF = 0
#         # if type(case_C2_TF) != int:
#         #     case_C2_TF = 0
#         # if type(case_C3_TF) != int:
#         #     case_C3_TF = 0
#         # if type(case_C4_TF) != int:
#         #     case_C4_TF = 0
        



#         # 사례지원계획 db
#         planning = Planning(
#             CT=CT,
#             setplan_name=ctname,
#             medical_start=medical_start,
#             medical_end=medical_end,
#             # mental_start=mental_start,
#             # mental_end=mental_end,
#             # case_start=case_start,
#             # case_end=case_end,
#             # set_A = set_A,
#             medical_A1_MF=medical_A1_MF,
#             medical_A1_TF=medical_A1_TF,
#             medical_A1_Text=medical_A1_Text,
#             medical_A2_MF=medical_A2_MF,
#             medical_A2_TF=medical_A2_TF,
#             medical_A2_Text=medical_A2_Text,
#             medical_A3_MF=medical_A3_MF,
#             medical_A3_TF=medical_A3_TF,
#             medical_A3_Text=medical_A3_Text,
#             medical_A4_MF=medical_A4_MF,
#             medical_A4_TF=medical_A4_TF,
#             medical_A4_Text=medical_A4_Text,
#             medical_B1_YN=medical_B1_YN,
#             medical_B1_Text=medical_B1_Text,
#             medical_B2_YN=medical_B2_YN,
#             medical_B2_Text=medical_B2_Text,
#             medical_B3_YN=medical_B3_YN,
#             medical_B3_Text=medical_B3_Text,
#             medical_B4_Name=medical_B4_Name,
#             medical_B4_YN=medical_B4_YN,
#             medical_B4_Text=medical_B4_Text, 

#             medical_C1_MF=medical_C1_MF,
#             medical_C1_TF=medical_C1_TF,
#             medical_C1_Text=medical_C1_Text,
#             medical_C2_MF=medical_C2_MF,
#             medical_C2_TF=medical_C2_TF,
#             medical_C2_Text=medical_C2_Text,
#             medical_C3_MF=medical_C3_MF,
#             medical_C3_TF=medical_C3_TF,
#             medical_C3_Text=medical_C3_Text,
#             medical_C4_Name=medical_C4_Name,
#             medical_C4_MF=medical_C4_MF,
#             medical_C4_TF=medical_C4_TF,
#             medical_C4_Text=medical_C4_Text,
#             medical_C5_Name=medical_C5_Name,
#             medical_C5_MF=medical_C5_MF,
#             medical_C5_TF=medical_C5_TF,
#             medical_C5_Text=medical_C5_Text,

#             medical_D1_Num=medical_D1_Num,
#             medical_D1_Text=medical_D1_Text,
#             medical_D2_Num=medical_D2_Num,
#             medical_D2_Text=medical_D2_Text,
#             medical_D3_YN=medical_D3_YN,
#             medical_D3_Text=medical_D3_Text,
#             medical_D4_Name=medical_D4_Name,
#             medical_D4_TF=medical_D4_TF,
#             medical_D4_Text=medical_D4_Text,
#             medical_D5_Name=medical_D5_Name,
#             medical_D5_TF=medical_D5_TF,
#             medical_D5_Text=medical_D5_Text,
#             medical_D6_Name=medical_D6_Name,
#             medical_D6_TF=medical_D6_TF,
#             medical_D6_Text=medical_D6_Text,

#             medical_E1_MF=medical_E1_MF,
#             medical_E1_TF=medical_E1_TF,
#             medical_E1_Text=medical_E1_Text,
#             medical_E2_MF=medical_E2_MF,
#             medical_E2_TF=medical_E2_TF,
#             medical_E2_Text=medical_E2_Text,
#             medical_E3_Name=medical_E3_Name,
#             medical_E3_MF=medical_E3_MF,
#             medical_E3_TF=medical_E3_TF,
#             medical_E3_Text=medical_E3_Text,

#             medical_F1_MF=medical_F1_MF,
#             medical_F1_TF=medical_F1_TF,
#             medical_F1_Text=medical_F1_Text,
#             medical_F2_MF=medical_F2_MF,
#             medical_F2_TF=medical_F2_TF,
#             medical_F2_Text=medical_F2_Text,
#             medical_F3_MF=medical_F3_MF,
#             medical_F3_TF=medical_F3_TF,
#             medical_F3_Text=medical_F3_Text,
#             medical_F4_Name=medical_F4_Name,
#             medical_F4_MF=medical_F4_MF,
#             medical_F4_TF=medical_F4_TF,
#             medical_F4_Text=medical_F4_Text,
            
#             # 심리지원
#             # mental_A1_MF=mental_A1_MF,
#             # mental_A1_TF=mental_A1_TF,
#             # mental_A1_Text=mental_A1_Text,
#             # mental_A2_MF=mental_A2_MF,
#             # mental_A2_TF=mental_A2_TF,
#             # mental_A2_Text=mental_A2_Text,
#             # mental_B1_TF=mental_B1_TF,
#             # mental_B2_Name=mental_B2_Name,
#             # mental_B2_TF=mental_B2_TF,
#             # mental_C1_MF=mental_C1_MF,
#             # mental_C1_TF=mental_C1_TF,
#             # mental_C1_Text=mental_C1_Text,
#             # mental_C2_MF=mental_C2_MF,
#             # mental_C2_TF=mental_C2_TF,
#             # mental_C2_Text=mental_C2_Text,
#             # mental_C3_Name=mental_C3_Name,
#             # mental_C3_MF=mental_C3_MF,
#             # mental_C3_TF=mental_C3_TF,
#             # mental_C3_Text=mental_C3_Text,

#             # # 사례지원
#             # case_A1_MF=case_A1_MF,
#             # case_A1_TF=case_A1_TF,
#             # case_A1_Text=case_A1_Text,
#             # case_A2_MF=case_A2_MF,
#             # case_A2_TF=case_A2_TF,
#             # case_A2_Text=case_A2_Text,
#             # case_A3_MF=case_A3_MF,
#             # case_A3_TF=case_A3_TF,
#             # case_A3_Text=case_A3_Text,
#             # case_A4_MF=case_A4_MF,
#             # case_A4_TF=case_A4_TF,
#             # case_A4_Text=case_A4_Text,
#             # case_B1_MF=case_B1_MF,
#             # case_B1_TF=case_B1_TF,
#             # case_B1_Text=case_B1_Text,
#             # case_B2_MF=case_B2_MF,
#             # case_B2_TF=case_B2_TF,
#             # case_B2_Text=case_B2_Text,
#             # case_B3_Name=case_B3_Name,
#             # case_B3_MF=case_B3_MF,
#             # case_B3_TF=case_B3_TF,
#             # case_B3_Text=case_B3_Text,
#             # case_C1_MF=case_C1_MF,
#             # case_C1_TF=case_C1_TF,
#             # case_C1_Text=case_C1_Text,
#             # case_C2_MF=case_C2_MF,
#             # case_C2_TF=case_C2_TF,
#             # case_C2_Text=case_C2_Text,
#             # case_C3_MF=case_C3_MF,
#             # case_C3_TF=case_C3_TF,
#             # case_C3_Text=case_C3_Text,
#             # case_C4_MF=case_C4_MF,
#             # case_C4_TF=case_C4_TF,
#             # case_C4_Text=case_C4_Text,
#             # setplan_comment=setplan_comment,
#             # setplan_sentence=setplan_sentence,

#             # medical_A1_TF=medical_A1_TF,
#             # medical_A2_TF=medical_A2_TF,
#             # medical_A3_TF=medical_A3_TF,
#             # medical_A4_TF=medical_A4_TF,
#             # sum_medical_A=medical_A1_TF+medical_A2_TF+medical_A3_TF+medical_A4_TF,
#             # sum_medical_B=medical_B1_YN+medical_B2_YN+medical_B3_YN+medical_B4_YN,
#             # sum_medical_C=medical_C1_TF+medical_C2_TF+medical_C3_TF+medical_C4_TF+medical_C5_TF,
#             # sum_medical_D=medical_D1_Num+medical_D2_Num+medical_D3_YN+medical_D4_TF+medical_D5_TF+medical_D6_TF,
#             # sum_medical_E=medical_E1_TF+medical_E2_TF+medical_E3_TF,
#             # sum_medical_F=medical_F1_TF+medical_F2_TF+medical_F3_TF+medical_F4_TF,
#             # sum_mental_A=mental_A1_TF+mental_A2_TF,
#             # sum_mental_B=mental_B1_TF+mental_B2_TF,
#             # sum_mental_C=mental_C1_TF+mental_C2_TF+mental_C3_TF,
#             # sum_case_A=case_A1_TF+case_A2_TF+case_A3_TF+case_A4_TF,
#             # sum_case_B=case_B1_TF+case_B2_TF+case_B3_TF,
#             # sum_case_C=case_C1_TF+case_C2_TF+case_C3_TF+case_C4_TF

           
#         )
        
#         planning.save()


class ProgramForm(forms.Form):
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
    perfor_program = forms.ChoiceField(
        error_messages={
            'required':'프로그램명을 입력해주세요.'
        },
        widget=forms.Select, choices=program_name, label='프로그램명',required=True)
    perfor_date = forms.CharField(
        error_messages={
            'required':'날짜를 입력해주세요.'
        },
        widget=forms.DateInput(attrs={'type':'date'}), label='진행 날짜', required=True)
    # perfor_date = forms.DateField(
    #     error_messages={
    #         'required':'날짜를 입력해주세요.'
    #     },
    #     label='진행 날짜', required=True)
    perfor_people = forms.IntegerField(
        error_messages={
            'required':'인원(건)을 입력해주세요.'
        },
        label='인원(건)',required=True)

    perfor_count = forms.IntegerField(
        error_messages={
            'required':'인원(건)을 입력해주세요.'
        },
        label='인원(건)',required=True)


    def clean(self):
        cleaned_data = super().clean()

        perfor_date = cleaned_data.get('perfor_date')
        perfor_people = cleaned_data.get('perfor_people')
        perfor_program = cleaned_data.get('perfor_program')
        perfor_count = cleaned_data.get('perfor_count')

        program = Program(

            perfor_program=perfor_program,
            perfor_date=perfor_date,
            perfor_people=perfor_people,
            perfor_count=perfor_count

        )

        program.save()