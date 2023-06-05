from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Department, Role
from django.db. models import Q

# Create your views here.

def index(request):
    return render(request, "index.html")


def all_emp(request):
    emps = Employee.objects.all()
    return render(request, "show_all_emp.html", context={"emps": emps})

def add_emp(request):
    if request.method == "GET":
        return render(request,   "add_emp.html")
    elif request.method == "POST":
        print(request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dept = request.POST.get("dept")
        salary = request.POST.get("salary")
        role = request.POST.get("role")
        bonus = request.POST.get("bonus")
        phone = request.POST.get("phone")
        hire_date = request.POST.get("hire_date")
        emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, role_id=role, bonus=bonus, phone=phone, hire_date=hire_date)
        emp.save()
        return redirect("all_emp")

def remove_emp(request, id=0):
    if id:
        try:
            emp = Employee.objects.get(id=id)
            emp.delete()
            return HttpResponse(f"Employee with id {id} removed successfully.")
        except Employee.DoesNotExist:
            return HttpResponse("Enter valid Employee ID") 
    emps = Employee.objects.all()
    print(emps)
    return render(request, "remove_emp.html", context={"emps": emps})
        
def filter_emp(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        dept = request.POST.get("dept")
        role = request.POST.get("role")
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
        return render(request, "show_all_emp.html", context={"emps": emps})
    elif request.method == "GET":
        return render(request, "filter_emp.html")
    else:
        return HttpResponse('An Exception Occurred')
    
def update_emp(request):
    if request.method == "POST":
        id = request.POST.get("id")
        if id:
            try:
                emp = Employee.objects.get(id=id)                  
            except Employee.DoesNotExist:
                return HttpResponse("Enter valid Employee ID") 
        emp.first_name = request.POST.get("first_name")
        emp.last_name = request.POST.get("last_name")
        emp.dept_id = request.POST.get("dept")
        emp.salary = request.POST.get("salary")
        emp.role_id= request.POST.get("role")
        emp.bonus = request.POST.get("bonus")
        emp.phone = request.POST.get("phone")
        emp.hire_date = request.POST.get("hire_date")
        
        emp.save()
        return HttpResponse(f"Employee with id {id} updated successfully.")
    else:
        return render(request, "update_emp.html")
