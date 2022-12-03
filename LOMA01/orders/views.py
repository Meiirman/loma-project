# from distutils.log import error]
import json
from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from companies.models import Company
from core.forms import CustomBackgroundForm
from core.models import CustomBackground
from core.views import TOKEN

from orders.forms import OrderForm, ProdutForm
from users.models import LomaUser
from .models import Order, Product, Stage
from users import accesses


def check_data():
    f = open("C:/Users/Miko/Desktop/LOMA01/change_data.txt", 'r', encoding="UTF-8")
    contents = f.read().split("\n")
    try:
        oredr = Order.objects.get(id=contents[0].split('|')[0])
        stage = Stage.objects.get(id=contents[0].split('|')[1])
        oredr.stage = stage
        oredr.message_sended = True
        oredr.save()
    except:
        pass


def send_message(chat_id, text, data=None, keyboard=None):
    data = {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": keyboard
    }
    r = requests.post("https://api.telegram.org/bot" + TOKEN + "/", params=data )
    print(r.text)


def get_summ(my_arr):
    summ = 0
    for i in my_arr:
        summ += i.budget
    
    return summ

def orders_red(request):
    return redirect("/orders")

def orders(request):
    check_data()
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        print("sdfg")
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        print(backgroundForm.is_valid())
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    else:
        
        print("sdfg emes")
        backgroundForm = CustomBackgroundForm(instance=current_background)
    # print(request)
    data = {}
    print(request.user)
    if request.user.is_authenticated:
        results = Order.objects.all()
        print(results)
        data = {
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm, 
            'doc_title': "LOMA | Заказы",
            "results" : results,    
            "section_name": "Заказы",
            'count': results.__len__,
            'summ':  get_summ(results),       
            'stages':  Stage.objects.all(),  
            #  "userdata": request.user.is_superuser 
            'access': accesses.get_access_data(request.user)    
        }
    else:
        data = {
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm, 

            'doc_title': "LOMA | Заказы",
            # "results" : results,    
            "section_name": "Заказы",
            # 'count': results.__len__,
            # 'summ':  get_summ(results),       
            'stages':  Stage.objects.all(),  
            #  "userdata": request.user.is_superuser 
            'access': {
                'update_settings': False,
                'change_stage': False,
                'update_orders': False,
                'update_product_info': False,
                'can_change_product_total_among': False,
            }    
        }
    return render(request, "orders/orders.html", data)


# def create_ochen_mnogo_zakazov(request):
#     data = {}
#     return render(request, "orders/orders.html", data)


def order_info(request, order_id):
    check_data()
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        print("Кырды")
        backgroundForm = CustomBackgroundForm(request.POST)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)


    print(order_id)
    try:
        order = Order.objects.filter(id=order_id)[0]
        # text += "Заказ №" + str(order.id) + "\n"
        # text += "Дата доставки: " + str(order.delivery_date) + "\n"
        # text += "Ответственный заказа: " + str(order.responsible) + "\n"
        # text += "Ответственный за доставку: " + str(order.courier.name) +' '+str(order.courier.surname)+ "\n"
        # text += "Адрес доставки: " + str(order.courier.name) +' '+str(order.courier.surname)+ "\n"


        text = ""
        text +="🧾 Номер Заказа : "+  str(order.id) + '\n'
        text +="👤 Имя клиента : " + str(order.client_FIO) + '\n'
        text +="📱 Телефон : "+ str(order.client_phone) + '\n'
        text +="🚛 Адрес : " + str(order.address) + '\n'
        text +="📝 Коммент : "+ str(order.description   ) + '\n'
        text +="👤 Ответственный за заказ : " + str(order.responsible) + '\n'
        text +="" + '\n'
        text +="💵 Бюджет :   "+str(order.budget)+" тенге" + '\n'
        text +="📦 Продукт : " + str(order.product)
        
        
        keyboard = {
            "inline_keyboard": [
                [
                    {
                        "text": "Доставлено", 
                        "callback_data": str(order.id) + "|5" 
                    },
                    {
                    "text": "Провал", "callback_data": str(order.id) + "|8" 
                    }
                ]

            ]
        }
        

        
        
        if order.stage.is_main_stage == True and order.message_sended == False :
            send_message(order.courier.telegram_chat_id, text, keyboard=json.dumps(keyboard))
            order.message_sended = True
        
        order.save()
        data = {
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm, 

            'order' : order,
            'error': False,            
        }
    except Exception:
        data = {
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm, 

            'order' : {},
            'error': True,            
        }
        pass
    return render(request, "orders/one_order.html", data)


def delete_order(request, order_id):

    check_data()
    # try:
    order = Order.objects.get(id=order_id)
    print(order.__dict__)
    order.save()
    order.delete()
    
    # except Exception:
    #     print(Exception)
    #     pass
    return redirect("/orders")

def order_update(request, order_id):
    check_data()
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/orders/'+str(order_id)+'/info', order.id)
    else:
        form = OrderForm(instance=order)

    return render(request, "orders/new_order.html", {"backgroundimg" : current_background.background,"form":form})

def new_order(request):
    check_data()
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    # print(LomaUser.objects.get(user=request.user).company)
    if request.POST:
        f = OrderForm(request.POST)
        f.save()
        fa = Order.objects.last()
        fa.source = "Создан вручную"
        fa.creator = LomaUser.objects.get(user=request.user)
        fa.company = LomaUser.objects.get(user=request.user).company
        fa.save()
        # print(LomaUser.objects.get(user=request.user).company)
        return redirect('/orders/'+str(fa.id)+"/info")
    form = OrderForm
    # print(reque   st.user)
    return render(request, "orders/new_order.html", {"backgroundimg" : current_background.background,"form":form})



# ____________________________________________________________________________

def products(request):
    check_data()
    if request.POST:
        f = ProdutForm(request.POST)
        f.company = Company.objects.last() 
        f.save()
        return redirect('/products')
    form = ProdutForm()

    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)

    # print(request)
    data = {}
    if request.GET:
        results = Product.objects.filter(name__unaccent__lower__trigram_similar=request.GET.search)
        data = {   
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm,
            "results" : results,
            "section_name":"Продукты",
            "form":form       
        }  
    else:
        results = Product.objects.all()
        data = {   
            "backgroundimg" : current_background.background,
            "backgroundform": backgroundForm,
            "section_name":"Продукты",       
            "results" : results  ,
            "form":form       

        }
    return render(request, "orders/products.html", data)


def product_info(request, product_id):
    check_data()
    try:
        product = Product.objects.filter(id=product_id)[0]
    except Exception:
        product = {
            'name': 'There is no such order',
            'description': 'There is no such order',
            'create_date': 'There is no such order',
            'change_date': 'There is no such order',
            'creator': 'There is no such order',
            'stage': 'There is no such order',
            'responsible': 'There is no such order',
        }
    return render(request, "orders/one_product.html", {'product':product})


def delete_product(request, product_id):
    check_data()
    try:
        
        print(product_id)
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception:
        pass
    return redirect("/orders/products")

def product_update(request, product_id):
    check_data()
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProdutForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/orders/products/'+str(product_id)+'/info', product.id)
    else:
        form = ProdutForm(instance=product)

    return render(request, "orders/new_product.html", {"form":form})

def new_product(request):
    check_data()
    if request.POST:
        f = ProdutForm(request.POST)
        f.company = Company.objects.last() 
        f.save()
        return redirect('/products')
    form = ProdutForm()
    return render(request, "orders/new_product.html", {"form":form})





