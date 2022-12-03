from cgi import print_arguments
from xmlrpc.client import ProtocolError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from companies.models import Company
from core.models import CustomBackground

from users.models import LomaUser, Role


# Create your views here.
def login(request):
    
    user_login = request.session.get('user_login', None)
    user_isOnline = request.session.get('isOnline', False)
    print(user_login)
    print(user_isOnline)
    if user_isOnline:
        request.session['isOnline'] = False
        request.session['user_login'] = None
    data={
        'isOnline': request.session.get('isOnline', False),
        'user_login': request.session.get('user_login', None)
    }
    return render(request, 'loma_auth/login.html', {'data': data})
    # return HttpResponse("<h1>Login page</h1><a href='/auth/reg'>Reg</a>")


def registration(request):
    
    print(request.GET)
    data={
            'isOnline': request.session.get('isOnline', False),
            'user_login': request.session.get('user_login', 'Azamat@mail.ru')
        }
    request.session['isOnline'] = True
    request.session['user_login'] = None
    return render(request, 'loma_auth/registration.html', {'data':data})
    # return HttpResponse("<h1>Registration page</h1><a href='/auth'>Auth</a>")


#  user_name, user_email, user_password
def registrate_user(request):

    print('Запрос на регистрацию')
    print(request.GET)
    
    # инициализация
    user_name = request.GET['user_name']
    user_email = request.GET['user_email']
    user_password = request.GET['user_password']
    user = User.objects.filter(email=user_email)
    if user:
        print(user)
        data = {
            'email': user[0].email,
            'error':{
                'context':'Пользователь с такой почтой уже существует',
                'bool': True
            }
        }
    else:
        user = User.objects.create_user(user_name, user_email, user_password)
        user.save()
        userr = User.objects.last()
        role = Role.objects.last()
        ccomany = Company.objects.last()
        lomauser = LomaUser(user=userr ,role=role ,company=ccomany)
        lomauser.save()
        lastbag = CustomBackground.objects.last().background
        background = CustomBackground(user=lomauser, background=lastbag)
        background.save()
        print("Все окей")

        return redirect('/auth/login')  



    
    return render(request, 'loma_auth/registration.html', {'data':data})
