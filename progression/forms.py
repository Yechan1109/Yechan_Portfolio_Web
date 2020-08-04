from django import forms
from django.forms import ModelForm
from .models import Progress, CTRS

class CTRSForm(forms.ModelForm):

    class Meta:
        model = CTRS
        fields = '__all__'


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = '__all__'
        # fields = ['getplan_name', 'getplan_date','inmedical_A1_C','inmedical_A1_select','inmedical_A1_select2','inmedical_A1_Text']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = '__all__'





































# class ProgressForm(forms.Form):
    
#     den = [
#         ('스케일링', '스케일링'),
#         ('보철', '보철'),
#         ('충치','충치'),
#         ('기타','기타')]
    
#     diagnosis = [
#         ('평일','평일'),
#         ('야간','야간')]

#     # for_name = forms.CharField(required=False, widget=forms.HiddenInput)
#     getplan_name = forms.CharField(required=False)
#     getplan_date = forms.DateField(required=False)
#     # 의료지원
#     inmedical_A1_select = forms.ChoiceField(choices=diagnosis,required=False)
#     inmedical_A1_select_2 = forms.ChoiceField(choices=den,required=False)
#     inmedical_A1_C = forms.IntegerField(required=False, initial=0)
#     inmedical_A1_Text = forms.CharField(max_length=200, required=False)
#     # inmedical_A2_select = forms.ChoiceField(choices=diagnosis, required=False)
#     # inmedical_A2_C = forms.IntegerField(required=False, initial=0)
#     # inmedical_A2_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_A3_select = forms.ChoiceField(choices=diagnosis, required=False)
#     # inmedical_A3_C = forms.IntegerField(required=False, initial=0)
#     # inmedical_A3_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_A4_select = forms.ChoiceField(choices=diagnosis, required=False)
#     # inmedical_A4_C = forms.IntegerField(required=False, initial=0)
#     # inmedical_A4_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_B1_YN = forms.BooleanField(required=False, initial='0')
#     # inmedical_B1_C = forms.IntegerField(required=False, initial='0')
#     # inmedical_B1_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_B2_YN = forms.BooleanField(required=False, initial='0')
#     # inmedical_B2_C = forms.IntegerField(required=False, initial='0')
#     # inmedical_B2_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_B3_YN = forms.BooleanField(required=False, initial='0')
#     # inmedical_B3_C = forms.IntegerField(required=False, initial='0')
#     # inmedical_B3_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_B4_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_B4_YN = forms.BooleanField(required=False, initial='0')
#     # inmedical_B4_C = forms.IntegerField(required=False, initial='0')
#     # inmedical_B4_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_C1_YN = forms.BooleanField(required=False)
#     # inmedical_C1_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_C2_YN = forms.BooleanField(required=False)
#     # inmedical_C2_C = forms.IntegerField(required=False)
#     # inmedical_C2_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_C3_YN = forms.BooleanField(required=False)
#     # inmedical_C3_F = forms.IntegerField(required=False, initial='0')
#     # inmedical_C3_C = forms.IntegerField(required=False)
#     # inmedical_C3_Text = forms.CharField(max_length=70, required=False)
    
#     # inmedical_C4_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_C4_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_C4_YN = forms.BooleanField(required=False)
#     # inmedical_C5_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_C5_YN = forms.BooleanField(required=False)
#     # inmedical_C5_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_D1_Num = forms.IntegerField()
#     # inmedical_D1_C = forms.IntegerField(required=False)
#     # inmedical_D1_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_D2_Num = forms.IntegerField()
#     # inmedical_D2_C = forms.IntegerField(required=False)
#     # inmedical_D2_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_D3_YN = forms.BooleanField(required=False)
#     # inmedical_D3_C = forms.IntegerField(required=False)
#     # inmedical_D3_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_D4_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_D4_YN = forms.BooleanField(required=False)
#     # inmedical_D4_C = forms.IntegerField(required=False)
#     # inmedical_D4_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_D5_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_D5_YN = forms.BooleanField(required=False)
#     # inmedical_D5_C = forms.IntegerField(required=False)
#     # inmedical_D5_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_D6_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_D6_YN = forms.BooleanField(required=False)
#     # inmedical_D6_C = forms.IntegerField(required=False)
#     # inmedical_D6_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_E1_YN = forms.BooleanField(required=False)
#     # inmedical_E1_C = forms.IntegerField(required=False)
#     # inmedical_E1_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_E2_YN = forms.BooleanField(required=False)
#     # inmedical_E2_C = forms.IntegerField(required=False)
#     # inmedical_E2_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_E3_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_E3_YN = forms.BooleanField(required=False)
#     # inmedical_E3_C = forms.IntegerField(required=False)
#     # inmedical_E3_Text = forms.CharField(max_length=70, required=False)

#     # inmedical_F1_YN = forms.BooleanField(required=False)
#     # inmedical_F1_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_F2_YN = forms.BooleanField(required=False)
#     # inmedical_F2_C = forms.IntegerField(required=False)
#     # inmedical_F2_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_F3_YN = forms.BooleanField(required=False)
#     # inmedical_F3_Text = forms.CharField(max_length=70, required=False)
#     # inmedical_F4_Name = forms.CharField(max_length=15, required=False)
#     # inmedical_F4_YN = forms.BooleanField(required=False)
#     # inmedical_F4_Text = forms.CharField(max_length=70, required=False)

#     # medical =[
#     # ('대면', '대면'),
#     # ('전화', '전화'),
#     # ('SNS', 'SNS')]
#     # inmedical_G1 = forms.ChoiceField(choices=medical, label='의료상담',required=False)
#     # inmedical_G1_Text = forms.CharField(widget=forms.Textarea)


#     # # 심리지원
#     # inmental_A1_YN = forms.BooleanField(required=False)
#     # inmental_A1_C = forms.IntegerField(required=False)
#     # inmental_A1_Text = forms.CharField(max_length=70, required=False)
#     # inmental_A2_YN = forms.BooleanField(required=False)
#     # inmental_A2_C = forms.IntegerField(required=False)
#     # inmental_A2_Text = forms.CharField(max_length=70, required=False)

#     # inmental_B1_YN = forms.BooleanField(required=False)
#     # inmental_B1_C = forms.IntegerField(required=False)
#     # inmental_B1_Text = forms.CharField(max_length=70, required=False)
#     # inmental_B2_Name = forms.CharField(max_length=15, required=False)
#     # inmental_B2_YN = forms.BooleanField(required=False)
#     # inmental_B2_C = forms.IntegerField(required=False)
#     # inmental_B2_Text = forms.CharField(max_length=70, required=False)
    
#     # inmental_C1_YN = forms.BooleanField(required=False)
#     # inmental_C1_Text = forms.CharField(max_length=70, required=False)
#     # inmental_C2_YN = forms.BooleanField(required=False)
#     # inmental_C2_Text = forms.CharField(max_length=70, required=False)
#     # inmental_C3_name = forms.CharField(max_length=15, required=False)
#     # inmental_C3_YN = forms.BooleanField(required=False)
#     # inmental_C3_Text = forms.CharField(max_length=70, required=False)

#     # # 사례관리
#     # incase_A1_YN = forms.BooleanField(required=False)
#     # incase_A1_YN2 = forms.BooleanField(required=False)
#     # incase_A1_Text = forms.CharField(max_length=200, required=False)
#     # incase_A2_YN = forms.BooleanField(required=False)
#     # incase_A2_YN2 = forms.BooleanField(required=False)
#     # incase_A2_Text = forms.CharField(max_length=200, required=False)
#     # incase_A3_YN = forms.BooleanField(required=False)
#     # incase_A3_YN2 = forms.BooleanField(required=False)
#     # incase_A3_Text = forms.CharField(max_length=200, required=False)
#     # incase_A4_YN = forms.BooleanField(required=False)
#     # incase_A4_YN2 = forms.BooleanField(required=False)
#     # incase_A4_Text = forms.CharField(max_length=200, required=False)

#     # incase_B1_YN = forms.BooleanField(required=False)
#     # incase_B1_Text = forms.CharField(max_length=70, required=False)
#     # incase_B2_YN = forms.BooleanField(required=False)
#     # incase_B2_Text = forms.CharField(max_length=70, required=False)
#     # incase_B3_Name = forms.CharField(max_length=15, required=False)
#     # incase_B3_YN = forms.BooleanField(required=False)
#     # incase_B3_Text = forms.CharField(max_length=70, required=False)

#     # incase_C1_YN = forms.BooleanField(required=False)
#     # incase_C1_Text = forms.CharField(max_length=100, required=False)
#     # incase_C2_YN = forms.BooleanField(required=False)
#     # incase_C2_Text = forms.CharField(max_length=100, required=False)
#     # incase_C3_YN = forms.BooleanField(required=False)
#     # incase_C3_Text = forms.CharField(max_length=100, required=False)
#     # incase_C4_YN = forms.BooleanField(required=False)
#     # incase_C4_Text = forms.CharField(max_length=100, required=False)
#     # incase_C5_TC = forms.IntegerField(required=False)

#     # getplan_comment = forms.CharField(widget=forms.Textarea)
#     # getplan_sentence = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         cleaned_data = super().clean()
#         getplan_name = cleaned_data.get('getplan_name')
#         getplan_date = cleaned_data.get('getplan_date')
#         inmedical_A1_select = cleaned_data.get('inmedical_A1_select')
#         inmedical_A1_select_2 = cleaned_data.get('inmedical_A1_select_2')
#         inmedical_A1_C = cleaned_data.get('inmedical_A1_C')
#         inmedical_A1_Text = cleaned_data.get('inmedical_A1_Text')

#         # inmedical_A2_YN = cleaned_data.get('inmedical_A2_YN')
#         # inmedical_A2_YN2 = cleaned_data.get('inmedical_A2_YN2')
#         # inmedical_A2_Text = cleaned_data.get('inmedical_A2_Text')
#         # inmedical_A3_YN = cleaned_data.get('inmedical_A3_YN')
#         # inmedical_A3_YN2 = cleaned_data.get('inmedical_A3_YN2')
#         # inmedical_A3_Text = cleaned_data.get('inmedical_A3_Text')
#         # inmedical_A4_YN = cleaned_data.get('inmedical_A4_YN')
#         # inmedical_A4_YN2 = cleaned_data.get('inmedical_A4_YN2')
#         # inmedical_A4_Text = cleaned_data.get('inmedical_A4_Text')

#         # inmedical_B1_YN = cleaned_data.get('inmedical_B1_YN')
#         # inmedical_B1_C = cleaned_data.get('inmedical_B1_C')
#         # inmedical_B1_Text = cleaned_data.get('inmedical_B1_Text')
#         # inmedical_B2_YN = cleaned_data.get('inmedical_B2_YN')
#         # inmedical_B2_C = cleaned_data.get('inmedical_B2_C')
#         # inmedical_B2_Text = cleaned_data.get('inmedical_B2_Text')
#         # inmedical_B3_YN = cleaned_data.get('inmedical_B3_YN')
#         # inmedical_B3_C = cleaned_data.get('inmedical_B3_C')
#         # inmedical_B3_Text = cleaned_data.get('inmedical_B3_Text')
#         # inmedical_B4_Name = cleaned_data.get('inmedical_B4_Name')
#         # inmedical_B4_YN = cleaned_data.get('inmedical_B4_YN')
#         # inmedical_B4_C = cleaned_data.get('inmedical_B4_C')
#         # inmedical_B4_Text = cleaned_data.get('inmedical_B4_Text')

#         # inmedical_C1_YN = cleaned_data.get('inmedical_C1_YN')
#         # inmedical_C1_Text = cleaned_data.get('inmedical_C1_Text')
#         # inmedical_C2_YN = cleaned_data.get('inmedical_C2_YN')
#         # inmedical_C2_C = cleaned_data.get('inmedical_C2_C')
#         # inmedical_C2_Text = cleaned_data.get('inmedical_C2_Text')
#         # inmedical_C3_YN = cleaned_data.get('inmedical_C3_YN')
#         # inmedical_C3_F = cleaned_data.get('inmedical_C3_F')
#         # inmedical_C3_C = cleaned_data.get('inmedical_C3_C')
#         # inmedical_C3_Text = cleaned_data.get('inmedical_C3_Text')
#         # inmedical_C4_Name = cleaned_data.get('inmedical_C4_Name')
#         # inmedical_C4_Text = cleaned_data.get('inmedical_C4_Text')
#         # inmedical_C4_YN = cleaned_data.get('inmedical_C4_YN')
#         # inmedical_C5_Name = cleaned_data.get('inmedical_C5_Name')
#         # inmedical_C5_YN = cleaned_data.get('inmedical_C5_YN')
#         # inmedical_C5_Text = cleaned_data.get('inmedical_C5_Text')

#         # inmedical_D1_Num = cleaned_data.get('inmedical_D1_Num')
#         # inmedical_D1_C = cleaned_data.get('inmedical_D1_C')
#         # inmedical_D1_Text = cleaned_data.get('inmedical_D1_Text')
#         # inmedical_D2_Num = cleaned_data.get('inmedical_D2_Num')
#         # inmedical_D2_C = cleaned_data.get('inmedical_D2_C')
#         # inmedical_D2_Text = cleaned_data.get('inmedical_D2_Text')
#         # inmedical_D3_YN = cleaned_data.get('inmedical_D3_YN')
#         # inmedical_D3_C = cleaned_data.get('inmedical_D3_C')
#         # inmedical_D3_Text = cleaned_data.get('inmedical_D3_Text')
#         # inmedical_D4_Name = cleaned_data.get('inmedical_D4_Name')
#         # inmedical_D4_YN = cleaned_data.get('inmedical_D4_YN')
#         # inmedical_D4_C = cleaned_data.get('inmedical_D4_C')
#         # inmedical_D4_Text = cleaned_data.get('inmedical_D4_Text')
#         # inmedical_D5_Name = cleaned_data.get('inmedical_D5_Name')
#         # inmedical_D5_YN = cleaned_data.get('inmedical_D5_YN')
#         # inmedical_D5_C = cleaned_data.get('inmedical_D5_C')
#         # inmedical_D5_Text = cleaned_data.get('inmedical_D5_Text')
#         # inmedical_D6_Name = cleaned_data.get('inmedical_D6_Name')
#         # inmedical_D6_YN = cleaned_data.get('inmedical_D6_YN')
#         # inmedical_D6_C = cleaned_data.get('inmedical_D6_C')
#         # inmedical_D6_Text = cleaned_data.get('inmedical_D6_Text')

#         # inmedical_E1_YN = cleaned_data.get('inmedical_E1_YN')
#         # inmedical_E1_C = cleaned_data.get('inmedical_E1_C')
#         # inmedical_E1_Text = cleaned_data.get('inmedical_E1_Text')
#         # inmedical_E2_YN = cleaned_data.get('inmedical_E2_YN')
#         # inmedical_E2_C = cleaned_data.get('inmedical_E2_C')
#         # inmedical_E2_Text = cleaned_data.get('inmedical_E2_Text')
#         # inmedical_E3_Name = cleaned_data.get('inmedical_E3_Name')
#         # inmedical_E3_YN = cleaned_data.get('inmedical_E3_YN')
#         # inmedical_E3_C = cleaned_data.get('inmedical_E3_C')
#         # inmedical_E3_Text = cleaned_data.get('inmedical_E3_Text')

#         # inmedical_F1_YN = cleaned_data.get('inmedical_F1_YN')
#         # inmedical_F1_Text = cleaned_data.get('inmedical_F1_Text')
#         # inmedical_F2_YN = cleaned_data.get('inmedical_F2_YN')
#         # inmedical_F2_C = cleaned_data.get('inmedical_F2_C')
#         # inmedical_F2_Text = cleaned_data.get('inmedical_F2_Text')
#         # inmedical_F3_YN = cleaned_data.get('inmedical_F3_YN')
#         # inmedical_F3_Text = cleaned_data.get('inmedical_F3_Text')
#         # inmedical_F4_Name = cleaned_data.get('inmedical_F4_Name')
#         # inmedical_F4_YN = cleaned_data.get('inmedical_F4_YN')
#         # inmedical_F4_Text = cleaned_data.get('inmedical_F4_Text')

#         # inmedical_G1 = cleaned_data.get('inmedical_G1')
#         # inmedical_G1_Text = cleaned_data.get('inmedical_G1_Text')

#         # # 심리지원
#         # inmental_A1_YN = cleaned_data.get('inmental_A1_YN')
#         # inmental_A1_C = cleaned_data.get('inmental_A1_C')
#         # inmental_A1_Text = cleaned_data.get('inmental_A1_Text')
#         # inmental_A2_YN = cleaned_data.get('inmental_A2_YN')
#         # inmental_A2_C = cleaned_data.get('inmental_A2_C')
#         # inmental_A2_Text = cleaned_data.get('inmental_A2_Text')

#         # inmental_B1_YN = cleaned_data.get('inmental_B1_YN')
#         # inmental_B1_C = cleaned_data.get('inmental_B1_C')
#         # inmental_B1_Text = cleaned_data.get('inmental_B1_Text')
#         # inmental_B2_Name = cleaned_data.get('inmental_B2_Name')
#         # inmental_B2_YN = cleaned_data.get('inmental_B2_YN')
#         # inmental_B2_C = cleaned_data.get('inmental_B2_C')
#         # inmental_B2_Text = cleaned_data.get('inmental_B2_Text')
        
#         # inmental_C1_YN = cleaned_data.get('inmental_C1_YN')
#         # inmental_C1_Text = cleaned_data.get('inmental_C1_Text')
#         # inmental_C2_YN = cleaned_data.get('inmental_C2_YN')
#         # inmental_C2_Text = cleaned_data.get('inmental_C2_Text')
#         # inmental_C3_name = cleaned_data.get('inmental_C3_name')
#         # inmental_C3_YN = cleaned_data.get('inmental_C3_YN')
#         # inmental_C3_Text = cleaned_data.get('inmental_C3_Text')

#         # # 사례관리
#         # incase_A1_YN = cleaned_data.get('incase_A1_YN')
#         # incase_A1_YN2 = cleaned_data.get('incase_A1_YN2')
#         # incase_A1_Text = cleaned_data.get('incase_A1_Text')
#         # incase_A2_YN = cleaned_data.get('incase_A2_YN')
#         # incase_A2_YN2 = cleaned_data.get('incase_A2_YN2')
#         # incase_A2_Text = cleaned_data.get('incase_A2_Text')
#         # incase_A3_YN = cleaned_data.get('incase_A3_YN')
#         # incase_A3_YN2 = cleaned_data.get('incase_A3_YN2')
#         # incase_A3_Text = cleaned_data.get('incase_A3_Text')
#         # incase_A4_YN = cleaned_data.get('incase_A4_YN')
#         # incase_A4_YN2 = cleaned_data.get('incase_A4_YN2')
#         # incase_A4_Text = cleaned_data.get('incase_A4_Text')

#         # incase_B1_YN = cleaned_data.get('incase_B1_YN')
#         # incase_B1_Text = cleaned_data.get('incase_B1_Text')
#         # incase_B2_YN = cleaned_data.get('incase_B2_YN')
#         # incase_B2_Text = cleaned_data.get('incase_B2_Text')
#         # incase_B3_Name = cleaned_data.get('incase_B3_Name')
#         # incase_B3_YN = cleaned_data.get('incase_B3_YN')
#         # incase_B3_Text = cleaned_data.get('incase_B3_Text')

#         # incase_C1_YN = cleaned_data.get('incase_C1_YN')
#         # incase_C1_Text = cleaned_data.get('incase_C1_Text')
#         # incase_C2_YN = cleaned_data.get('incase_C2_YN')
#         # incase_C2_Text = cleaned_data.get('incase_C2_Text')
#         # incase_C3_YN = cleaned_data.get('incase_C3_YN')
#         # incase_C3_Text = cleaned_data.get('incase_C3_Text')
#         # incase_C4_YN = cleaned_data.get('incase_C4_YN')
#         # incase_C4_Text = cleaned_data.get('incase_C4_Text')
#         # incase_C5_TC = cleaned_data.get('incase_C5_TC')
#         # getplan_comment = cleaned_data.get('getplan_comment')
#         # getplan_sentence = cleaned_data.get('getplan_sentence')

#         # if type(inmedical_A1_C) != int:
#         #     inmedical_A1_C = 0
#         # if type(inmedical_B1_C) != int:
#         #     inmedical_B1_C = 0
#         # if type(inmedical_B2_C) != int:
#         #     inmedical_B2_C = 0
#         # if type(inmedical_B3_C) != int:
#         #     inmedical_B3_C = 0
#         # if type(inmedical_B4_C) != int:
#         #     inmedical_B4_C = 0
#         # if type(inmedical_C2_C) != int:
#         #     inmedical_C2_C = 0
#         # if type(inmedical_C3_C) != int:
#         #     inmedical_C3_C = 0
#         # if type(inmedical_D1_C) != int:
#         #     inmedical_D1_C = 0
#         # if type(inmedical_D2_C) != int:
#         #     inmedical_D2_C = 0
#         # if type(inmedical_D3_C) != int:
#         #     inmedical_D3_C = 0
#         # if type(inmedical_D4_C) != int:
#         #     inmedical_D4_C = 0
#         # if type(inmedical_D5_C) != int:
#         #     inmedical_D5_C = 0
#         # if type(inmedical_D6_C) != int:
#         #     inmedical_D6_C = 0
#         # if type(inmedical_E1_C) != int:
#         #     inmedical_E1_C = 0
#         # if type(inmedical_E2_C) != int:
#         #     inmedical_E2_C = 0
#         # if type(inmedical_E3_C) != int:
#         #     inmedical_E3_C = 0
#         # if type(inmedical_F2_C) != int:
#         #     inmedical_F2_C = 0    

#         # if type(inmental_A1_C) != int:
#         #     inmental_A1_C = 0
#         # if type(inmental_A2_C) != int:
#         #     inmental_A2_C = 0
#         # if type(inmental_B1_C) != int:
#         #     inmental_B1_C = 0
#         # if type(inmental_B2_C) != int:
#         #     inmental_B2_C = 0
#         # if type(incase_C5_TC) != int:
#         #     incase_C5_TC = 0

#         # if type(inmedical_D1_Num) != int:
#         #     inmedical_D1_Num = 0
#         # if type(inmedical_D2_Num) != int:
#         #     inmedical_D2_Num = 0

#         progress = Progress(
#             # sum_inmedical_A=inmedical_A1_YN+inmedical_A2_YN+inmedical_A3_YN+inmedical_A4_YN,
#             # sum_inmedical_A2=inmedical_A1_YN2+inmedical_A2_YN2+inmedical_A3_YN2+inmedical_A4_YN2,
#             # sum_inmedical_B=inmedical_B1_YN+inmedical_B2_YN+inmedical_B3_YN+inmedical_B4_YN,
#             # sum_inmedical_C=inmedical_C1_YN+inmedical_C2_YN+inmedical_C3_YN+inmedical_C4_YN,
#             # sum_inmedical_D=inmedical_D1_Num+inmedical_D2_Num+inmedical_D3_YN+inmedical_D4_YN+inmedical_D5_YN+inmedical_D6_YN,
#             # sum_inmedical_E=inmedical_E1_YN+inmedical_E2_YN+inmedical_E3_YN,
#             # sum_inmedical_F=inmedical_F1_YN+inmedical_F2_YN+inmedical_F3_YN+inmedical_F4_YN,
#             # sum_inmental_A=inmental_A1_YN+inmental_A2_YN,
#             # sum_inmental_B=inmental_B1_YN+inmental_B2_YN,
#             # sum_inmental_C=inmental_C1_YN+inmental_C2_YN+inmental_C3_YN,
#             # sum_incase_A=incase_A1_YN+incase_A2_YN+incase_A3_YN+incase_A4_YN,
#             # sum_incase_A2=incase_A1_YN2+incase_A2_YN2+incase_A3_YN2+incase_A4_YN2,
#             # sum_incase_B=incase_B1_YN+incase_B2_YN+incase_B3_YN,
#             # sum_incase_C=incase_C1_YN+incase_C2_YN+incase_C3_YN+incase_C4_YN,
#             # sum_cost = inmedical_A1_C+inmedical_B1_C+inmedical_B2_C+inmedical_B3_C+inmedical_B4_C+inmedical_C2_C+inmedical_C3_C+inmedical_D1_C+inmedical_D2_C+inmedical_D3_C+inmedical_D4_C+inmedical_D5_C+inmedical_D6_C+inmedical_E1_C+inmedical_E2_C+inmedical_E3_C+inmedical_F2_C+inmental_A1_C+inmental_A2_C+inmental_B1_C+inmental_B2_C+incase_C5_TC,

#             getplan_name=getplan_name,
#             getplan_date=getplan_date,
#             inmedical_A1_select=inmedical_A1_select,
#             # inmedical_A1_select2=inmedical_A1_select_2,
#             inmedical_A1_C=inmedical_A1_C,
#             inmedical_A1_Text=inmedical_A1_Text,
#             # inmedical_A2_YN=inmedical_A2_YN,
#             # inmedical_A2_YN2=inmedical_A2_YN2,
#             # inmedical_A2_Text=inmedical_A2_Text,
#             # inmedical_A3_YN=inmedical_A3_YN,
#             # inmedical_A3_YN2=inmedical_A3_YN2,
#             # inmedical_A3_Text=inmedical_A3_Text,
#             # inmedical_A4_YN=inmedical_A4_YN,
#             # inmedical_A4_YN2=inmedical_A4_YN2,
#             # inmedical_A4_Text=inmedical_A4_Text,

#             # inmedical_B1_YN=inmedical_B1_YN,
#             # inmedical_B1_C=inmedical_B1_C,
#             # inmedical_B1_Text=inmedical_B1_Text,
#             # inmedical_B2_YN=inmedical_B2_YN,
#             # inmedical_B2_C=inmedical_B2_C,
#             # inmedical_B2_Text=inmedical_B2_Text,
#             # inmedical_B3_YN=inmedical_B3_YN,
#             # inmedical_B3_C=inmedical_B3_C,
#             # inmedical_B3_Text=inmedical_B3_Text,
#             # inmedical_B4_Name=inmedical_B4_Name,
#             # inmedical_B4_YN=inmedical_B4_YN,
#             # inmedical_B4_C=inmedical_B4_C,
#             # inmedical_B4_Text=inmedical_B4_Text,

#             # inmedical_C1_YN=inmedical_C1_YN,
#             # inmedical_C1_Text=inmedical_C1_Text,
#             # inmedical_C2_YN=inmedical_C2_YN,
#             # inmedical_C2_C=inmedical_C2_C,
#             # inmedical_C2_Text=inmedical_C2_Text,
#             # inmedical_C3_YN=inmedical_C3_YN,
#             # inmedical_C3_F=inmedical_C3_F,
#             # inmedical_C3_C=inmedical_C3_C,
#             # inmedical_C3_Text=inmedical_C3_Text,
#             # inmedical_C4_Name=inmedical_C4_Name,
#             # inmedical_C4_Text=inmedical_C4_Text,
#             # inmedical_C4_YN=inmedical_C4_YN,
#             # inmedical_C5_Name=inmedical_C5_Name,
#             # inmedical_C5_YN=inmedical_C5_YN,
#             # inmedical_C5_Text=inmedical_C5_Text,

#             # inmedical_D1_Num=inmedical_D1_Num,
#             # inmedical_D1_C=inmedical_D1_C,
#             # inmedical_D1_Text=inmedical_D1_Text,
#             # inmedical_D2_Num=inmedical_D2_Num,
#             # inmedical_D2_C=inmedical_D2_C,
#             # inmedical_D2_Text=inmedical_D2_Text,
#             # inmedical_D3_YN=inmedical_D3_YN,
#             # inmedical_D3_C=inmedical_D3_C,
#             # inmedical_D3_Text=inmedical_D3_Text,
#             # inmedical_D4_Name=inmedical_D4_Name,
#             # inmedical_D4_YN=inmedical_D4_YN,
#             # inmedical_D4_C=inmedical_D4_C,
#             # inmedical_D4_Text=inmedical_D4_Text,
#             # inmedical_D5_Name=inmedical_D5_Name,
#             # inmedical_D5_YN=inmedical_D5_YN,
#             # inmedical_D5_C=inmedical_D5_C,
#             # inmedical_D5_Text=inmedical_D5_Text,
#             # inmedical_D6_Name=inmedical_D6_Name,
#             # inmedical_D6_YN=inmedical_D6_YN,
#             # inmedical_D6_C=inmedical_D6_C,
#             # inmedical_D6_Text=inmedical_D6_Text,

#             # inmedical_E1_YN=inmedical_E1_YN,
#             # inmedical_E1_C=inmedical_E1_C,
#             # inmedical_E1_Text=inmedical_E1_Text,
#             # inmedical_E2_YN=inmedical_E2_YN,
#             # inmedical_E2_C=inmedical_E2_C,
#             # inmedical_E2_Text=inmedical_E2_Text,
#             # inmedical_E3_Name=inmedical_E3_Name,
#             # inmedical_E3_YN=inmedical_E3_YN,
#             # inmedical_E3_C=inmedical_E3_C,
#             # inmedical_E3_Text=inmedical_E3_Text,

#             # inmedical_F1_YN=inmedical_F1_YN,
#             # inmedical_F1_Text=inmedical_F1_Text,
#             # inmedical_F2_YN=inmedical_F2_YN,
#             # inmedical_F2_C=inmedical_F2_C,
#             # inmedical_F2_Text=inmedical_F2_Text,
#             # inmedical_F3_YN=inmedical_F3_YN,
#             # inmedical_F3_Text=inmedical_F3_Text,
#             # inmedical_F4_Name=inmedical_F4_Name,
#             # inmedical_F4_YN=inmedical_F4_YN,
#             # inmedical_F4_Text=inmedical_F4_Text,
#             # inmedical_G1=inmedical_G1,
#             # inmedical_G1_Text=inmedical_G1_Text,

#             # # 심리지원
#             # inmental_A1_YN=inmental_A1_YN,
#             # inmental_A1_C=inmental_A1_C,
#             # inmental_A1_Text=inmental_A1_Text,
#             # inmental_A2_YN=inmental_A2_YN,
#             # inmental_A2_C=inmental_A2_C,
#             # inmental_A2_Text=inmental_A2_Text,

#             # inmental_B1_YN=inmental_B1_YN,
#             # inmental_B1_C=inmental_B1_C,
#             # inmental_B1_Text=inmental_B1_Text,
#             # inmental_B2_Name=inmental_B2_Name,
#             # inmental_B2_YN=inmental_B2_YN,
#             # inmental_B2_C=inmental_B2_C,
#             # inmental_B2_Text=inmental_B2_Text,
            
#             # inmental_C1_YN=inmental_C1_YN,
#             # inmental_C1_Text=inmental_C1_Text,
#             # inmental_C2_YN=inmental_C2_YN,
#             # inmental_C2_Text=inmental_C2_Text,
#             # inmental_C3_name=inmental_C3_name,
#             # inmental_C3_YN=inmental_C3_YN,
#             # inmental_C3_Text=inmental_C3_Text,

#             # # 사례관리
#             # incase_A1_YN=incase_A1_YN,
#             # incase_A1_YN2=incase_A1_YN2,
#             # incase_A1_Text=incase_A1_Text,
#             # incase_A2_YN=incase_A2_YN,
#             # incase_A2_YN2=incase_A2_YN2,
#             # incase_A2_Text=incase_A2_Text,
#             # incase_A3_YN=incase_A3_YN,
#             # incase_A3_YN2=incase_A3_YN2,
#             # incase_A3_Text=incase_A3_Text,
#             # incase_A4_YN=incase_A4_YN,
#             # incase_A4_YN2=incase_A4_YN2,
#             # incase_A4_Text=incase_A4_Text,

#             # incase_B1_YN=incase_B1_YN,
#             # incase_B1_Text=incase_B1_Text,
#             # incase_B2_YN=incase_B2_YN,
#             # incase_B2_Text=incase_B2_Text,
#             # incase_B3_Name=incase_B3_Name,
#             # incase_B3_YN=incase_B3_YN,
#             # incase_B3_Text=incase_B3_Text,

#             # incase_C1_YN=incase_C1_YN,
#             # incase_C1_Text=incase_C1_Text,
#             # incase_C2_YN=incase_C2_YN,
#             # incase_C2_Text=incase_C2_Text,
#             # incase_C3_YN=incase_C3_YN,
#             # incase_C3_Text=incase_C3_Text,
#             # incase_C4_YN=incase_C4_YN,
#             # incase_C4_Text=incase_C4_Text,
#             # incase_C5_TC=incase_C5_TC,
#             # getplan_comment=getplan_comment,
#             # getplan_sentence=getplan_sentence
                
#         )

#         progress.save()