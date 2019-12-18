from django.shortcuts import render
from testapp.models import Employee
# Create your views here.

def login(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'register.html')

def savedetails(request):
    #id=request.GET.get('id')
    username=request.POST.get('username')
    password=request.POST.get('password')
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    # eaddr=request.POST.get('eaddr')
    e=Employee(username=username,password=password,name=name,salary=salary)
    e.save()
    return render(request,'index.html')

def logincheck(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    id= Employee.objects.only('id').get(username=username).id
    emp=Employee.objects.filter(username=username,password=password)
    if emp:
        res=Employee.objects.get(id=id)
        return render(request,'welcome.html',{'msg':res})
    else:
        return render(request,'index.html')

def viewprofile(request):
    id=request.GET.get('id')
    res=Employee.objects.get(id=id)
    return render(request,'welcome.html',{'profile':res,'msg':res})

def updateprofile(request):
    id=request.GET.get('id')
    res=Employee.objects.get(id=id)
    return render(request,'welcome.html',{'update':res,'msg':res})

def updatedetails(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    name=request.POST.get('name')
    salary=request.POST.get('salary')
    id=request.GET.get('id')
    # eaddr=request.POST.get('eaddr')
    e=Employee(username=username,id=id,password=password,name=name,salary=salary)
    e.save()
    return render(request,'welcome.html',{'profile':e,'msg':e})

def deleteprofile(request):
    id=request.GET.get('id')
    res=Employee.objects.get(id=id)
    return render(request,'welcome.html',{'delete':res,'msg':res})

def delete(request):
    option=request.POST.get('yes')
    id=request.POST.get('id')
    if option=='Yes':
        Employee.objects.filter(id=id).delete()
        return render(request,'index.html')

