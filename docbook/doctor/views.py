from django.shortcuts import render,redirect
from .models import *
def DocRegisterView(request):
    return render(request,"doctor-register.html")

def DocRegisterView1(request):
    return render(request,"step1.html")

def profile_submit(request):
    if request.method=="POST":
        profile_image=request.POST['profile_image']    
        gender=request.POST['gender']  
        reg_clinic_address=request.POST['address']  
        pincode=request.POST['zipcode']  
        age=request.POST['age']  
        bio = request.POST['bio']  
        qualification =request.POST['qualification']  
        mobile =request.POST['mobile']  
        profile_data=DocProfile.objects.create(profile_image=profile_image,gender=gender,reg_clinic_address=reg_clinic_address,pincode=pincode,age=age,bio=bio,qualification=qualification,mobile=mobile)
        profile_data.save()
        return redirect('/')
    else:
        return render(request,'step1.html')    


    

    
