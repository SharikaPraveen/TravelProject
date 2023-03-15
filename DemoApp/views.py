from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Place
from .models import Team


# Create your views here.
def Home(request):
    obj = Place.objects.all()
    test = Team.objects.all()
    return render(request,"index.html",{'response': obj, 'result': test})


def login(request):
    # # print(">>>>>>>>>>>>>>", request.get)
    # print(">>>>>>>>>>>>>>", request.POST)

    if request.method == 'POST':
        # print("abc")

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # print("logged")
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            # print("invalid")
            return redirect('login')
    #print("user created")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

# def method(request):
#     n1 = int(request.GET['n1'])
#     n2 = int(request.GET['n2'])
#     addition = n1 + n2
#     subtraction = n1 - n2
#     multiplication = n1 * n2
#     division = n1 / n2
#     cal = {'add': addition, 'sub': subtraction, 'mul': multiplication, 'div': division}
#     return render(request, 'Result.html',{'Key':cal})
#
