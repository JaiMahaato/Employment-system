from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Emp123,Testimonial
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def emp(request):
    emps=Emp.objects.all()
    
    return render(request,"index.html",{
        'emps':emps
    })

def add(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working == None:
            e.working=False
        else:
            e.working=True


        e.save() 
        
        return redirect('/jai/home/')
   
    return render(request,'add.html',{})    
   




def delete(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()

    return redirect('/jai/home/')




def update(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,'update.html',{
        'emp':emp
    })


def doupdate(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        

        e.save()     

    return redirect('/jai/home/')



def feedback(request):
    if request.method=="POST":


        
        email=request.POST.get('email')
        name=request.POST.get('name')
        feedback=request.POST.get('feedback')
        e=Emp123()
        e.email=email
        e.name=name
        e.feedback=feedback
        e.save()
        
        print("data save")
        return redirect('/jai/home/')
            
        
    return render(request,'feedback.html',{})


def jai(request):
    return render(request,'jai.html',{})



def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,'testimonials.html',{
        'testi':testi
    })

