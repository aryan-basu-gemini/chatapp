from django.shortcuts import render,redirect
from .models import Userdetails,Chat
import datetime
import pandas as pd
name_from=''
def home(request):
    print(datetime.datetime.now()) 
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
    
    message_data1=[]
    message_data2=[]
    time_data1=[]
    time_data2=[]
    if message1:
        message_data1=message1[0].message
        time_data1=message1[0].timestamp
    if message2:
        message_data2=message2[0].message
        time_data2=message2[0].timestamp



    if request.method=="POST":
        message=Chat.objects.filter(from_message=email_from,to_message=email_to)
        
        
        if not message:
            temp=[]
            temp_time=[]
            temp_message=request.POST.get('message')
            temp.append(temp_message)
            chat=Chat()
            chat.from_message=email_from
            chat.message=temp
            chat.to_message=email_to
            temp_time.append(datetime.datetime.now())
            chat.timestamp=temp_time 
            chat.save()
        else:
            temp=message[0].message
            temp_time=message[0].timestamp
            temp_message=request.POST.get('message')
            temp_time.append(datetime.datetime.now())
            temp.append(temp_message)
            message.update(message=temp,timestamp=temp_time)
            
    cols=[]
    df = pd.DataFrame(columns = cols)
    flag_data=[]
    for i in range(len(message_data1)):      
      flag_data.append(1)
    for i in range(len(message_data2)):
        flag_data.append(2)
    message_data=message_data1+message_data2
    time_data=time_data1+time_data2
    data={
        'Message':message_data,
        'Time':time_data,
        'Flag':flag_data
    }
    
    df=pd.DataFrame(data)
    
    df.sort_values('Time', inplace=True)
    df.reset_index(inplace = True, drop = True) # Resets the index, makes factor a column
   
    arr=[]
    for ind in df.index:
        x={'Message':df['Message'][ind],'Time':df['Time'][ind],'Flag':df['Flag'][ind]}
        arr.append(x)

    ##print(arr)
    return render(request,'message.html',{'data':arr})

