from django.urls import path

from.import views

urlpatterns=[
    path('',views.index),
    path('signin',views.addstaff),
    path('log',views.direct),
    path('login',views.login),
    path('home',views.manage),
    path('staff',views.send),
    path('customer',views.addcustomer),
    path('savedata',views.addcustomer),
    path('category',views.show_category),
    path('cat',views.insert_category),
    path('BookRoom',views.show_room),
    path('addroom',views.add_room),
    path('aservice',views.services),
    path('service',views.add_service),
    path('addcustservice',views.customer_service),
    path('addservice_cust',views.addservice_cust),
    path('customerview',views.customerview),
    path('bill/<int:id>',views.bill),
    path('delete/<int:id>',views.delete)
    
    
    
    
]
    