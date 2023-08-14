from django.shortcuts import render,redirect
from .models import Userdetails,Chat

name_from=''
def home(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        x=Userdetails.objects.filter(email=email,password=password).values()
        
        
        if Userdetails.objects.filter(email=email,password=password).count():
            data=Userdetails.objects.exclude(email=email,password=password)
            
            global email_from
            email_from=x[0]['email']
            return render(request,'index.html',{'data':data})
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
        global email_from
        email_from=email
        return render(request,'index.html')
          
    return render(request,'signup.html')
def index(request):
    return render(request,'index.html')
def message(request,id):
    
    clicked_data=Userdetails.objects.filter(id=id).values()
    email_to=clicked_data[0]['email']
    message1=Chat.objects.filter(from_message=email_from,to_message=email_to)
    message2=Chat.objects.filter(from_message=email_to,to_message=email_from)
    data1=[]
    data2=[]
    if message1:
        data1=message1[0].message
    if message2:
        data2=message2[0].message



    if request.method=="POST":
        message=Chat.objects.filter(from_message=email_from,to_message=email_to)
        
        
        if not message:
            temp=[]
            temp_message=request.POST.get('message')
            temp.append(temp_message)
            chat=Chat()
            chat.from_message=email_from
            chat.message=temp
            chat.to_message=email_to
            chat.save()
        else:
            temp=message[0].message
            temp_message=request.POST.get('message')
            temp.append(temp_message)
            message.update(message=temp)
        
    return render(request,'message.html',{'data1':data1,'data2':data2})
# Create your views here.
