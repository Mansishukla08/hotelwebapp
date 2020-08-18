from django import forms
from.models import Customer,Booking,Room,Service



room_name = [
    ('G101','G101'),
    ('G102','G102'),
    ('G103','G103'),
    ('G104','G104'),
    
]


class Customerform(forms.Form):
    name=forms.CharField(max_length=200)
    phone=forms.FloatField()
    email=forms.CharField(max_length=200)
    address=forms.CharField(max_length=200)
    room=forms.ModelMultipleChoiceField(queryset=Room.objects.all())
    adhaar=forms.ImageField()
 
class ServiceForm(forms.Form):
    cust=forms.ModelMultipleChoiceField(queryset=Customer.objects.all())
    service_display=forms.ModelMultipleChoiceField(queryset=Service.objects.all())