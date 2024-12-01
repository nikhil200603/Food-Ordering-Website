from .models import Student
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
def exec():
    print("Function Started")
    # time.sleep(5)
    print("Function Executed")

def send_email_to_clients():
    subject="This is the mail from Django server"
    message="This is a test message"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["nikhilkasaundhan@gmail.com","nikhilkasaundhan1@gmail.com"]
    try:
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
    except Exception as e:
        print(e)

def send_email_with_attachment(subject,message,recipient_list,file_path):
    mail=EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
    




  
