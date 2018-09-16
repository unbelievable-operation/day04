from django.contrib import admin

# Register your models here.
from app.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 'id', 's_sex', 's_age']
    list_filter = ['id']
    search_fields = ['s_name']
    list_per_page = 5


admin.site.register(Student, StudentAdmin)

