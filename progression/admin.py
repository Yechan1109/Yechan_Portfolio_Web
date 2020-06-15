from django.contrib import admin
from .models import Progress, CTRS


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Progress._meta.get_fields() if field.name != "getplan_name"]
    list_display = ('id','CT','getplan_date','last_date','counselor','inmedical_A_1_sum','inmedical_A_2_sum','inmedical_A_3_sum',
'inmedical_A_4_sum','inmedical_A_sum','inmedical_B_sum','inmedical_C_sum',
'inmedical_D_sum','inmedical_E_sum','inmedical_F_sum','inmedical_G_sum',
'inmental_A_sum','inmental_B_sum','inmental_C_sum','incase_A_sum',
'incase_B_sum','incase_C_sum')
    list_display_links = ('CT',)
    # search_fields = [field.name for field in Progress._meta.get_fields() if field.name != "getplan_name"]
    search_fields = ('getplan_name',)
    exclude = ('inmedical_A1_YN_2','inmedical_A1_select_2','inmedical_A1_C_2','inmedical_A1_Text_2',
    'inmedical_A2_YN_2','inmedical_A2_select_2','inmedical_A2_C_2','inmedical_A2_Text_2',
    'inmedical_A3_YN_2','inmedical_A3_select_2','inmedical_A3_C_2','inmedical_A3_Text_2',
    'inmedical_A4_YN_2','inmedical_A4_select_2','inmedical_A4_C_2','inmedical_A4_Text_2') 
    list_per_page = 20


@admin.register(CTRS)
class CTRSAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CTRS._meta.get_fields()]
    list_display = ('id','CT','danger_date','last_date','danger_label','counselor','sum_1','sum_2','sum_3','sum_4',
    'sum_5','sum_6','sum_7','sum_9','sum_10','sum_11','total')
    list_display_links = ('CT',)
    search_fields = ('danger_name',)
    list_per_page = 20


    def 가정영역(self, obj):
        return obj.survey1_1 + obj.survey1_2 + obj.survey1_3 + obj.survey1_4 + obj.survey1_5