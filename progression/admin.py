from django.contrib import admin
from .models import Progress, CTRS


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Progress._meta.get_fields() if field.name != "getplan_name"]
    # list_display_links = ('CT_id',)
    # search_fields = [field.name for field in Progress._meta.get_fields() if field.name != "getplan_name"]
    search_fields = ('getplan_name',)
    exclude = ('inmedical_A1_YN_2','inmedical_A1_select_2','inmedical_A1_C_2','inmedical_A1_Text_2',
    'inmedical_A2_YN_2','inmedical_A2_select_2','inmedical_A2_C_2','inmedical_A2_Text_2',
    'inmedical_A3_YN_2','inmedical_A3_select_2','inmedical_A3_C_2','inmedical_A3_Text_2',
    'inmedical_A4_YN_2','inmedical_A4_select_2','inmedical_A4_C_2','inmedical_A4_Text_2') 
    list_per_page = 10


@admin.register(CTRS)
class CTRSAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CTRS._meta.get_fields() if field.name != "danger_name"]
    list_display = ('danger_name','가정영역')
    # list_display_links = ('CT_id',)

    def 가정영역(self, obj):
        return obj.survey1_1 + obj.survey1_2 + obj.survey1_3 + obj.survey1_4 + obj.survey1_5