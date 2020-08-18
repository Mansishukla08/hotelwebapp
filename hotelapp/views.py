from django.shortcuts import render
from.models import Staff,Login,Category,Room,Customer,Booking,Service,CustomerService
from.forms import Customerform,ServiceForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"staff.html")


def addstaff(request):
    s1=Staff()
    l1=Login()
    s1.name=request.POST['name']
    s1.email=request.POST['email']
    s1.phone=request.POST['phone']
    s1.address=request.POST['address']
    s1.gender=request.POST['gender']
    s1.salary=request.POST['salary']
    s1.designation=request.POST['designation']
    
    l1.username=s1.email
   
    l1.password=request.POST['psw']
    l1.save()
    s1.login=l1
    s1.save()
    return render(request,'index.html')

def login(request):
    l1=Login()
    l1.username=request.POST['uname']
    l1.password=request.POST['psw']
    l1.save()
    return render(request,"home.html")


def direct(request):
    return render(request,"index.html")

def send(request):
    return render(request,"staff.html")

def manage(request):
    return render(request,"index.html")


def sendy(request):
    return render(request,"form.html")

def addcustomer(request):
     if request.method == 'POST':
         cus_form=Customerform(request.POST,request.FILES)
         if cus_form.is_valid():
            c=Customer()
            c_room=cus_form.cleaned_data["room"]
            c.name=cus_form.cleaned_data["name"]
            c.phone=cus_form.cleaned_data["phone"]
            c.email=cus_form.cleaned_data["email"]
            c.address=cus_form.cleaned_data["address"]
            c.adhaar=cus_form.cleaned_data["adhaar"]
            c.save()
            b=Booking()

            b.checkin_date=request.POST["indate"]
            b.checkout_date=request.POST["outdate"]
            b.people=request.POST["people"]
            b.customers=c
            print(c_room)
            for course in c_room:
                   print('hello')
                   jim=str(course)
                   list1=jim.split()
            z=list1[0]
            print("hii",z)
            booking_list=Booking.objects.all()
            for items in booking_list:
                print(items.rooms.room_no)
                if items.rooms.room_no in z:
                    return render(request,"service.html",{'error':"room addition operation  failed try adding different room"})
                else:
                    b.rooms=Room.objects.get(room_no=z)
                    return render(request,"service.html",{'error':'customer_added'})
            b.rooms=Room.objects.get(room_no=z)
            b.save()
            return render(request,"service.html",{'error':'customer_added'})
        
    
     else:
         pf=Customerform()
         return render(request,"form.html",{'form':pf})
     
def confirm(request):
    b1=Booking()
    val=Room.objects.get(id=id)
    print(val)
    b1.rooms=val
    b1.save()
    
        
        
def show_category(request):
    return render(request,"category.html")
    
def insert_category(request):
    c1=Category()
    c1.cname=request.POST["name1"]
    c1.description=request.POST["desc"]
    c1.save()
    return render(request,"home.html")



def show_room(request):
    room=Category.objects.all()
    return render(request,"room.html",{'list1':room})

def add_room(request):
    r1=Room()
    r1.room_no=request.POST["rno"]
    r1.description=request.POST["desc"]
    k=request.POST.getlist('room')
    for items in k:
        b=Category.objects.get(id=items)
        r1.categories=b
    r1.save()
    return render(request,"room.html",{'error':'rooms already added'})

def services(request):
    return render(request,'service.html')

def add_service(request):
    s=Service()
    s.name=request.POST["sname"]
    s.tariff=request.POST["scharge"]
    s.description=request.POST["sdesc"]
    s.save()
    return render(request,"home.html",{'error':'service_added'})

def customer_service(request):
    pf=ServiceForm()
    return render(request,"cservice.html",{'form':pf})

def addservice_cust(request):
    service_form = ServiceForm(request.POST)
    if service_form.is_valid():
        p=CustomerService()
        name=service_form.cleaned_data["cust"]
        service=service_form.cleaned_data["service_display"]
        for i in name:
            t=str(i)
            s=t.split()
        n1=s[0]
        
        for s in service:
            t2=str(s)
            s2=t2.split()
        n2=s2[0]
        
        p.Customers=Customer.objects.get(name=n1)
        p.Services=Service.objects.get(name=n2)
        p.save()
        return render(request,"home.html",{'error':'service_added'})
    
def customerview(request):
    m=Customer.objects.all()
    return render(request,"customerview.html",{'list1':m})

def bill(request,id):
    c=CustomerService.objects.all()
    list2=list()
    for items in c:
        if id==items.Customers.id:
            list2.append(items.Services)
    sum=0
    for items in list2:
        sum=sum+items.tariff
    list2.append(sum)
    return render(request,"bill.html",{'list3':list2})

def delete(request,id):
    c=Customer.objects.get(id=id)
    c.delete()
    m=Customer.objects.all()
    return render(request,"customerview.html",{'list1':m})
    
    
    
