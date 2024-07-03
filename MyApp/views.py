from django.shortcuts import render
from MyApp.models import Student
# Create your views here.
def fakerView(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'MyApp/output.html',d)