from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
import uuid
from .utilities import Send_Verification_Email, Send_Password_Reset_Email






# Create your views here.
def Test(request):
    
    return render(request, "resetpassword.html")

def Login_Attempt(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        # Check If Email is Existing or not
        email_is_valid = User.objects.filter(email=email).first()
        if email_is_valid:
            
            if email_is_valid.is_active:
                # Check The Email and Password Both Are Correct
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    # If User Object Authenticate Success Make Login
                    login(request, user)
                    return render(request, "home.html")
                else:
                    # Through Invalid Password Message
                    messages.error(request, "Invalid Password")
                    return render(request, "login.html")
            else:
                messages.error(request, "An email has been sent to you email address. please check your inbox and verify your account to login")
                return render(request, "emailSent.html")
        else:
            messages.error(request, "Invalid Email Address")
    return render(request, "login.html")




def Register_Attempt(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        email_taken = User.objects.filter(email=email).first()
        if email_taken:
            messages.error(request, "Email is already exists")
            return render(request, "register.html")
        
        if password != cpassword:
            messages.error(request, "Password not matched")
            return render(request, "register.html")
        
        token = str(uuid.uuid4())
        new_user = User.objects.create(email=email, email_token=token, is_active=False)
        new_user.set_password(password)
        new_user.save()
        Send_Verification_Email(email,token)
        messages.error(request, "An email has been sent to you email address. please check your inbox and verify your account to login")
        return render(request, "emailSent.html")

    return render(request, "register.html")


def VerifyAuthToken(request, auth_token):
    try:
        user_obj = User.objects.filter(email_token=auth_token).first()
        if user_obj:
            user_obj.is_active = True
            user_obj.save()
            messages.error(request, "Your Account is verified ! Please Login Here")
            return redirect('Login_Attempt')
    except:
        messages.error(request, "An Error Occurred, Please Try Again!")
        return redirect('Login_Attempt') 
    


def Forget_Pass_Attempt(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        try:
            user_obj = User.objects.filter(email=email).first()
            if user_obj:
                token = str(uuid.uuid4())
                user_obj.forget_password_token = token
                user_obj.save()
                Send_Password_Reset_Email(email,token)
                messages.error(request, "An email has been sent to you email address. please check your inbox and reset your password")
                return render(request, "emailSent.html")
            else:
                messages.error(request, "Your Email Address is Wrong, Please Try Again")
                return redirect('Forget_Pass_Attempt') 
        except:
            messages.error(request, "An Error Occurred, Please Try Again!")
            return redirect('Login_Attempt') 
        
    return render(request, "forgetpass.html")


def VerifyPasswordToken(request, forget_token):
    try:
        user_obj = User.objects.filter(forget_password_token=forget_token).first()
        if user_obj:
            if request.method == "POST":
                password = request.POST['password']
                cpassword = request.POST['cpassword']

                if password != cpassword:
                    messages.error(request, "Password not matched")
                    return redirect('Verify_Password_Token', forget_token=forget_token)
                user_obj.set_password(password)
                user_obj.save()
                messages.error(request, "Your Password Is Reset ! Please Login Here")
                return redirect('Login_Attempt')
            else:
                return render(request, "resetpassword.html", {'token': forget_token})
        else:
            messages.error(request, "An Error Occurred, Please Try Again!")
            return redirect('Login_Attempt')
    except:
        messages.error(request, "An Error Occurred, Please Try Again!")
        return redirect('Login_Attempt') 
                    
        