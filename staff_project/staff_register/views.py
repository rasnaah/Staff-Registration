from django.shortcuts import render, redirect
from .forms import StaffForm
from .models import Staff

# Create your views here.

def staff_list(request):
    context = {'staff_list' :Staff.objects.all()}
    return render(request,"staff_register/staff_list.html",context)

def staff_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = StaffForm()
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(instance=staff)
        return render(request,"staff_register/staff_form.html",{'form':form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(request.POST,instance = staff)
        if form.is_valid():
            form.save()
        return redirect('/staff/list')


def staff_delete(request,id):
    staff = Staff.objects.get(pk=id)
    staff.delete()
    return redirect('/staff/list')
