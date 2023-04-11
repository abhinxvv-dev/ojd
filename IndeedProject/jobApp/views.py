from django.shortcuts import render
from jobApp.models import *
from . import forms
# Create your views here.
def index(request):
    return render(request,'index.html')

def hydJobs(request):
    jobs_list=hydjobs.objects.order_by('id')
    my_dict={'jobs_list':jobs_list}
    return render(request,'hydJobs.html',context=my_dict)

def lkoJobs(request):
    jobs_list=lkojobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'lkoJobs.html',context=my_dict)

def registration(request):
    form=forms.jobForm()
    if request.method=='POST':
        id1=request.POST['id']
        company1=request.POST['company']
        address1=request.POST['address']
        email1=request.POST['email']
        phone1=request.POST['phone']
        date1=request.POST['date']
        data=lkojobs.objects.create(id=id1,company=company1,address=address1,email=email1,phone=phone1,date=date1)
        print("DATA ENTERD SUCCESSFULLY")


    return render(request,'registration.html',{'form':form})
