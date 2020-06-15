from django.contrib import admin

from user.models import Intake, Planning, Program


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'created_date', 'Coun', 'Gender', 'Age','Route','Institute')
    # list_display = [field.name for field in Intake._meta.get_fields() if field.name != "id"]
    # list_display_links = ('Name',)
    search_fields = ('Name',)
    list_per_page = 20

    # exclude = ('Coun',) 


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('id','CT','setplan_date','last_date','counselor')
    # list_display = [field.name for field in Planning._meta.get_fields() if field.name != "id"]
    list_display_links = ('CT',)
    search_fields = ('setplan_name',)
    list_per_page = 20

    # autocomplete_fields = ["setplan_name"]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','perfor_program','perfor_date','perfor_count','perfor_people')
    list_display_links = ('perfor_program',)
    search_fields = ('setplan_name',)
    list_per_page = 30

