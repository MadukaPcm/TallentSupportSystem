from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#home page function view.
def HomeView(request):

    return render(request, 'index.html')

#homepage contact view
def ContactView(request):

    return render(request, 'account/contact.html')

#homepage about view..
def AboutView(request):

    return render(request, 'account/about.html')

#login function view.
def LoginView(request):

    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        user = authenticate(request,username=Username,password=Password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request, "Ur are Now logged in")
            return redirect('customerdashboard_url')

        else:
            messages.error(request, "Invalid username || password")
            return redirect("login_url")
 
    context = {}
    return render(request,'account/login.html',context)

def SignoutView(request):

    logout(request)
    return redirect('home_url')

#register function view.
def RegisterView(request):

    context = {}
    return render(request,'account/register.html',context)

def RegisterFunctionView(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')
        usergroup = request.POST.get('Usergroup')

        if User.objects.filter(username = request.POST['Username']).exists():
            messages.info(request, "User already exists")
            return redirect('register_url')

        if len(username) < 5:
            messages.info(request,'username should have atleast 5 characters')
            return redirect('register_url')

        if User.objects.filter(email=request.POST['Email']).exists():
            messages.info(request,'email already taken.')
            return redirect('register_url')

        if password1 != password2:
            messages.info(request,'password does not match')
            return redirect('register_url')

        if len(password1) != 8:
            messages.info(request, 'password, write 8 mixed characters')
            return redirect('register_url')

        else:
            userdata = User.objects.create_user(
                username = username,
                email = email,
                password = password1
            )

            userdata.first_name = First_name
            userdata.last_name = Last_name
            userdata.save()

            if usergroup == '1':
               group = Group.objects.get(name = 'expert')
               user = User.objects.get(username = username)
               user.groups.add(group)

               return redirect('login_url')  

            else:
                group = Group.objects.get(name = 'observer')
                user = User.objects.get(username = username)
                user.groups.add(group)

                return redirect('login_url')  
    else:
        return redirect('login_url')        


def ForgotPasswordView(request):

    context = {}
    return render(request, 'account/forgot_password.html',context)