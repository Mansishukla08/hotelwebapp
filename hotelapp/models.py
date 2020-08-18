from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    class Meta:
        db_table='login'

class Category(models.Model):
    cname=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    
    class Meta:
        db_table='category'

class Room(models.Model):
    room_no=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    
    categories=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.room_no+" "+self.description
    class Meta:
        db_table='room'
        
class Staff(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    salary=models.FloatField()
    designation=models.CharField(max_length=100)
    login=models.OneToOneField(Login,on_delete=models.CASCADE)
    def __str__(self):
        return self.name+" "+self.email+" "+self.phone+" "+self.address+" "+self.salary+" "+self.designation
    class Meta:
        db_table='staff'
    
class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.FloatField()
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    adhaar=models.ImageField(upload_to='pictures')
    
    def __str__(self):
        return self.name+" "+str(self.phone)+" "+(self.email)+" "+(self.address)   
    class Meta:
        db_table='customer'
    

class Booking(models.Model):
    customers=models.ForeignKey(Customer,on_delete=models.CASCADE)
    rooms=models.ForeignKey(Room,on_delete=models.CASCADE)
    checkin_date=models.DateField()
    checkout_date=models.DateField()
    people=models.IntegerField()
    
    def __str__(self):
        return self.customers+" "+self.rooms+" "+self.checkin_date+" "+self.checkout_date+" "+self.people
    class Meta:
        db_table='booking'
        
class Service(models.Model):
    name=models.CharField(max_length=20)
    tariff=models.FloatField()
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.name+" "+str(self.tariff)+" "+self.description
    class Meta:
        db_table='service'
        
class CustomerService(models.Model):
    Customers=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Services=models.ForeignKey(Service,on_delete=models.CASCADE)
    class Meta:
        db_table='custservice'
    def __str__(self):
        return self.name+" "+str(self.tariff)      
          
    