from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import Data,Credentials
# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        name=request.POST.get('nme')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        address=request.POST.get('address')
        bg=request.POST.get('bg')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        users=Data.objects.all()
        pnov=True
        emv=True
        for i in users:
            if pno==i.pno:
                pnov=False
            if email==i.email:
                emv=False
        if pnov==True:
            if emv==True:
                data=Data(name=name,pno=pno,email=email,address=address,bg=bg)
                data.save()
            else:
                messages.info(request,'Email Already Exist')
                return render(request,'register.html')
        else:
            messages.info(request,'Pno Already Exist')
            return render(request,'register.html')
        credentials=Credentials(username=email,Password=pw)
        credentials.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        data=Credentials.objects.all()
        usersdata=Data.objects.all()
        usv=False
        psv=False
        user='x'
        for i in data:
            if i.username==un:
                usv=True
                if i.Password==pw:
                    psv=True
                    
        for j in usersdata:
            if j.email==un:
                user=j
        if usv==True:
            if psv==True:
                messages.info(request,'Logged in Successfull')
                return render(request,'login.html',{'user':user})
            else:
                messages.info(request,'invalid Password')
                return render(request,'login.html')
        else:
            messages.info(request,'invalid Username')
            return render(request,'login.html')
    else:

        return render(request,'login.html')