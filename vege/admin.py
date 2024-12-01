from django.contrib import admin
from django.db.models import Sum

from .models import *
# Register your models here.

admin.site.register(Receipe)
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Department)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(Subject)


class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_generation']
    ordering=['student_rank']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        marks=subject_marks.aggregate(marks=Sum('marks')) 
        return marks['marks']

admin.site.register(ReportCard,ReportCardAdmin)
