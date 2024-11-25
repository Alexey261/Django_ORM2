from django.shortcuts import render
# from .forms import UserRegister
from task1.models import *


def index(request):
    return render(request, 'platform.html')

def cart(request):
    return render(request, 'cart.html')

def games(request):
    # gds = ['Counter-Strike', 'Quake III Arena', 'Doom 2: Hell on Earth']
    gds = Game.objects.all()
    data = {'goods': gds}
    return render(request, 'games.html', context=data)



# users = [['Vasya', 'xyz717~!@', 18]]

def sign_up(request):

    info = {}
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        users = Buyer.objects.all()
        if any(l.name == login for l in users):
            err_msg = 'Пользователь уже существует'
        elif not(password == repeat_password):
            err_msg = 'Пароли не совпадают'
        elif int(age) < 18:
            err_msg = 'Вы должны быть старше 18'
        else:
            err_msg = 'Привет, '
            # users.append([login, password, int(age)])
            Buyer.objects.create(name=login, balance=0, age=age, password=password)

        info['error'] = err_msg
        info['user'] = [login, password, repeat_password, age]

        return render(request, 'registration_page.html', context=info)

    return render(request, 'registration_page.html')

