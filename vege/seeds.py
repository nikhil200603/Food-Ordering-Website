from faker import Faker
fake=Faker()
import random

from .models import *
from django.db.models import Sum




def create_subject_marks(n)->None:
    try:
        student_list=Student.objects.all()
        for s in student_list:
            subject_list=Subject.objects.all()
            for subj in subject_list:
                marks=random.randint(0,100)
                SubjectMarks.objects.create(
                    student=s,
                    subject=subj,
                    marks=marks
                )
    except Exception  as e:
        print(e)


def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            # print("heloo")
            department_objs=Department.objects.all()
            department=department_objs[random.randint(0,len(department_objs)-1)]
            student_id=f'STU-{random.randint(100,1000)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            student_address=fake.address()
            student=StudentID.objects.create(student_id=student_id)
            

            s_obj=Student.objects.create(
                student_id=student,
                deparment=department,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )

            s_obj.save()
    except Exception as e: 
        print(e)

def generate_report_card():

    current_rank=1
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    for rank in ranks:
        ReportCard.objects.create(student=rank,student_rank=current_rank)
        current_rank+=1



