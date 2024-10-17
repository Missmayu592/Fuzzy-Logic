
# ------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------


from django.shortcuts import render

# Create your views here.

def fullpage(request): 
    return render(request, 'main/fullpage.html')


    
# def signup(request):

#     return render(request, 'main/signup.html')




def about(request): 
    return render(request, 'main/about.html')



#==================================================
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from main import settings
# from django.core.mail import send_mail

def signup(request):
    if request.method == "POST":
        username = request.POST['fname']
        # fname = request.POST['fname']
        # lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        print(username, email, pass1)
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            # return redirect('home')
            return HttpResponse('email already taken')
        
        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            # return redirect('home')
            return HttpResponse('password mismatch')

        
        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        login( request, myuser)
        print('user created and logged in')
        return redirect('home')


        #Send Email
        subject = 'Welcome Parents!'
        message = "Hello" + myuser.username + "!!\n" + "Dear Parents of child , Your child good at this subject." + "\n" + "Thank You for Visiting us.\n\nOfficial Student - XYZ"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'main/signup.html')



# def login(request): 
#     if request.method == "POST":
#         pass
    
#     return render(request, 'main/login.html')


def singin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            print('user logged in.')
            return redirect('home')

        else:
            messages.error(request, "Bad Credentials!!")
            # return redirect('home')
            return HttpResponse('no such user exists.')
    
    return render(request, 'main/login.html')


def sign_out(request): 
    logout(request)
    return redirect('home')
