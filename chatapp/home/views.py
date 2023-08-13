from django.shortcuts import render,redirect
from .models import Userdetails

def home(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Userdetails.objects.filter(email=email,password=password).count():
            return render(request,'index.html')
        else:
            return render(request,'login.html')

    return render(request,'login.html')
def signup(request):
    data=Userdetails.objects.all()
    main_data={
    'data':data
    }
    print(main_data)
    if request.method=="POST":
        userdetail=Userdetails()
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        userdetail.name=name
        userdetail.email=email
        userdetail.password=password
        userdetail.save()
       
        return render(request,'index.html')
          
    return render(request,'signup.html')
def index(request):
    return render(request,'index.html')
# Create your views here.
