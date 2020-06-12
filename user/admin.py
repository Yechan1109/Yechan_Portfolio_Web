from django.contrib import admin

from user.models import Intake, Planning, Program


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'created_date', 'Coun', 'Gender', 'Jumin', 'Age')
    # list_display = [field.name for field in Intake._meta.get_fields() if field.name != "id"]
    # list_display_links = ('Name',)
    search_fields = [field.name for field in Intake._meta.get_fields()]
    # exclude = ('Coun',) 


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('setplan_name','setplan_date','last_date')
    # list_display = [field.name for field in Planning._meta.get_fields() if field.name != "id"]
    list_display_links = ('setplan_name',)
    # autocomplete_fields = ["setplan_name"]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Program._meta.get_fields()]
    list_display_links = ('id',)
