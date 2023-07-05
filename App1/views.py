from django.shortcuts import render,redirect
from App1.models import Camera_show,Contact_form,Signup_Form ,Suggestions_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.
def Homepage(request):
    return render(request,'index.html')

    

def show(request):
    csf=Camera_show.objects.all()
    return render(request,'show.html',{'csf':csf})


def contact_formF(request):
    if request.method =='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Masg=request.POST['message']
       
        User(Name=Name,Email=Email,Subject=Subject,Masg=Masg)
        return redirect('Homepage')
    
    else:
        return render(request,'contactform.html')




def about_us(request):
    return render(request,'aboutform.html')

            # signup

def signup_page(request):
    if request.method =='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Password=request.POST['Password']
        rp=request.POST['rp']
        if Password == rp:
            if User.objects.filter(username=Name).exists():
                messages.error(request,'Username allready exists..')
            elif User.objects.filter(email=Email).exists():
                messages.error(request,'Email allready exists..')
                return redirect('signup_page')
            else:
                User(username=Name,email=Email,password=Password).save()
                return redirect('Homepage')
        else:
         messages.error(request,'Password not match')
         return render(request,'signup.html')
         

    return render(request,'signup.html')
            
        


def suggestion(request):
    if request.method =='POST':
        Name=request.POST['Name']
        Phone=request.POST['Phone']
        Email=request.POST['Email']
        Misg=request.POST['Misg']
        Topic=request.POST['Topic']
        # breakpoint()
        # print(Name)
        Suggestions_form(Name=Name,Phone=Phone, Email=Email, Topic=Topic,Misg=Misg).save()
        # s="Thanks for Your Suggestions...Get in Touch"
        return render(request,'show.html')
    else:
     return redirect('signup_page')





def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        Password=request.POST['Password']
        # print('heelo')
        user = authenticate(username=username,password=Password)
        if user is not None:
            auth.login(request,user)    
            # return redirect('show')
            messages.success(request,'Login succesfull ')
            return redirect('show')

        else:
            messages.error(request,'Invalid Password/Username')
            return redirect('login')
            
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("login")
       






           



   
   