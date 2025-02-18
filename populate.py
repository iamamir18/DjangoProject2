import os
import django
from numpy import roll
#Run administrative tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakerProject.settings')
#set environment to current project settings
django.setup() #load the module
from faker import Faker
from MyApp.models import Student
f=Faker()
def generate_data(n):
    for i in range(n):#n specifies no of records
        fname=f.name()
        froll=f.random_int(min=1,max=100)
        fmarks=f.random_int(min=1,max=100)
        fdob=f.date_of_birth()
        femail=f.email
 
        s=Student.objects.get_or_create(name=fname,roll=froll,marks=fmarks,dob=fdob,email=femail)
generate_data(20)