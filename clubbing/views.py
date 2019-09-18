from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from clubbing.forms import SignUpForm, AddPurchase, FormOrder
from clubbing.models import *


def index(request):
    list_item = Item.objects.all()
    return render(request, 'index.html', context={'items': list_item})


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html')
    else:
        return render(request, 'error.html', context={'error_title': 'Выход',
                                                      'error_content': 'Авторизованные пользователи могут только выйти!'})


def login_page(request):
    # user = authenticate(request)
    # login(request, user)
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        login_str = request.POST["login"]
        password_str = request.POST["password"]
        user = authenticate(username=login_str, password=password_str)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login.html', context={'error_m': 'Не верный логин или пароль'})
        return redirect('index')

# ASd123fkasd123
def register_page(request):
    if request.method == 'GET':
        return render(request, 'register.html', context={'form': SignUpForm()})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'register.html', context={'form': SignUpForm(), 'error_m': 'Ошибка при заполнении формы регистрации'})
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('register')
        login(request, user)
        return redirect('index')


def purchases(request):
    if request.user.is_authenticated and request.user.group == User.ORGANIZER:
        if request.method == 'GET':
            listPurchases = Purchase.objects.all().filter(user=request.user).order_by('-id')
            return render(request, 'purchases.html', context={'purchases': listPurchases})
        else:
            purch = Purchase.objects.get(pk=request.POST['purch'])
            purch.status = request.POST['status']
            purch.save()
            msg = f'Продажа началась для тоавара: {purch.item}' if request.POST['status'] == 'SL' else f'Продажа закрыта: {purch.item}'
            messages.info(request, msg)
            return redirect('purchases')


def detail_item(request, pk):
    d_item = Item.objects.get(pk=pk)
    return render(request, 'detail_item.html', context={'detail': d_item})


def add_purchase(request):
    if request.user.is_authenticated and request.user.group == User.ORGANIZER:
        if request.method == 'GET':
            item_list = Item.objects.all()
            return render(request, 'add_purchase.html', context={'form': AddPurchase(initial={'user': request.user}), 'items': item_list})
        else:
            purch_form = AddPurchase(request.POST, initial={'user': request.user})
            d_item = Item.objects.get(pk=request.POST['item'])
            max_cost_purch = int(request.POST['max_cost'])
            if purch_form.is_valid():
                if d_item.price > max_cost_purch:
                    messages.error(request, 'Максимальная стоимость должна быть не меньше цены за товар')
                    return render(request, 'add_purchase.html', context={'form': AddPurchase(initial={'user': request.user})})

                purch_form.save()
                messages.info(request, 'Товар успешно добавлен')
                return redirect('purchases')
            else:
                messages.error(request, 'Ошибка при заполнении формы добавления товара')
                return render(request, 'add_purchase.html', context={'form': AddPurchase(initial={'user': request.user})})

def clubbings(request):
    if request.user.is_authenticated and request.user.group == 'BR':
        if request.method == 'GET':
            all_purch = Purchase.objects.reverse().all().filter(status=Purchase.OPEN)
            orders = [el['purchase'] for el in Order.objects.all().filter(buyer=request.user).values('purchase')]

            return render(request, 'clubbings.html', context={'orders': orders,
                                                              'purchases': all_purch})
        else:
            form_order = FormOrder(request.POST)
            if form_order.is_valid():
                form_order.save()
                messages.info(request, 'Вы встали в очередь на заказ!')
                return redirect('clubbings')
# def detail_club(request, pk):
#     club = 
#     return render(request, 'clubbings.html', context={'orders': orders, 'purchases': all_purch})