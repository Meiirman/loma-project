from django.shortcuts import redirect, render
import requests
from core.forms import CustomBackgroundForm
from core.models import CustomBackground
from couriers.models import Courier
from companies.models import Company, Region

from users import accesses
from users.models import LomaUser
from django.core.files import File
# Create your views here.
TOKEN = "5041015087:AAGQpkjpbS6Pz2yCVOUHcDcQUOKSf-WqfpA"

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

def cleaner(text):
	result = ''
	arr = text.split(" ")
	for j in arr:
		if j != "" and j != "\n" :
			result += j + " "
	return result

def dashboard(request):
    
    return render(request,"core/dashboard.html")



def settings(request):
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)
    requests = []
    f = open("C:/Users/Miko/Desktop/LOMA01/core/couriers_requests.txt", 'r', encoding="UTF-8")
    contents = f.read().split("\n")
    print(contents)
    # .read().split("\n")

    for i in contents:
        ii = i.split("|")
        try:
            requests.append({
                "chat_id": ii[0],
                "username": ii[1],
                "firstname": ii[2],
                "lastname": ii[3],
                "is_active": ii[4],
            })
        except:
            pass

    # print(requests)
    data = {  
        "requests" : requests,
        "backgroundimg" : current_background.background,
        "backgroundform": backgroundForm, 
        "section_name" : "Настройки",
        'access': accesses.get_access_data(request.user)

    }
    return render(request, "core/settings.html", data)

def activate_courier(request, chat_id):

    f = open("C:/Users/Miko/Desktop/LOMA01/core/couriers_requests.txt", 'r', encoding="UTF-8")
    contents = f.read().split("\n")
    
    text = ""
    my_courier = None
    for i in contents:
        print(str(chat_id) + " | " + str(i.split("|")[0]))
        if cleaner(str(chat_id)) == cleaner(str(i.split("|")[0])):
            my_courier = str(i)
            text += str(chat_id)
            text += "|" + i.split("|")[1]
            text += "|" + i.split("|")[2]
            text += "|" + i.split("|")[3]
            text += "|" + str("True\n")
    file = open("C:/Users/Miko/Desktop/LOMA01/core/couriers_requests.txt", 'w', encoding="UTF-8")
    file.write(text)

    register_couriers = Courier(
        name=my_courier.split("|")[2],
        surname=my_courier.split("|")[3],
        telegram_chat_id=my_courier.split("|")[0],
        # available_regions=Region.objects.last(),
        isActive=True,
        telegram_name=my_courier.split("|")[1],
        phone_number=87055071747,
        company = Company.objects.last(),
    )
    register_couriers.save()
    send_message(chat_id, text="Вы были добавлены в курьеры. Теперь вы можете получать и доставлять заказы")
    print("wertytrewftyrewrtyregtretdy")
    return redirect("/settings/")
    
def couriers(request):
    data = {}
    return render(request, "core/couriers.html", data)

    
def orders(request):
    data = {}
    return render(request, "core/orders.html", data)

    
def products(request):
    data = {}
    return render(request, "core/products.html", data)

    
def roles(request):
    data = {}

    
    return render(request, "core/roles.html", data)