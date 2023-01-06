from django.contrib import admin

from .models import Admissions, Course, Trainers

admin.site.register(Course)
admin.site.register(Trainers)


class AdmissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 's_name', 's_phone', 's_email',
                    'trainers_name', 'admission_date')


admin.site.register(Admissions, AdmissionsAdmin)
# Register your models here.
