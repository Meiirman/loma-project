from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.forms import CustomBackgroundForm
from core.models import CustomBackground

from couriers.forms import CourierForm
from couriers.models import Courier
from users import accesses
from users.models import LomaUser

# Create your views here.
def couriers(request):
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)
    results = Courier.objects.all()
    data = {
        "backgroundimg" : current_background.background,
        "backgroundform": backgroundForm,
        'doc_title': "LOMA | Курьеры",
        "results" : results,    
        "section_name": "Курьеры",
        'count': results.__len__,       
        #  "userdata": request.user.is_superuser 
        'access': accesses.get_access_data(request.user)    
    }
    return render(request, "couriers/couriers.html", data)


def courier_requests(request):
    return render(request, "couriers/couriers.html", {})


def new_courier(request):
    
    if request.POST:
        f = CourierForm(request.POST)
        f.save()
        return redirect('/couriers')
    form = CourierForm
    return render(request, "couriers/new_courier.html", {'form':form})




def courier_info(request, courier_id):
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)
    print(courier_id)
    try:
        courier = Courier.objects.filter(id=courier_id)[0]
        print(courier.__dict__)
    except Exception:
        courier = {
            'name': 'There is no such order',
            'description': 'There is no such order',
            'create_date': 'There is no such order',
            'change_date': 'There is no such order',
            'creator': 'There is no such order',
            'stage': 'There is no such order',
            'responsible': 'There is no such order',
        }
    return render(request, "couriers/one_courier.html", { "backgroundimg" : current_background.background,
        "backgroundform": backgroundForm,'courier':courier})


def delete_courier(request, courier_id):
    if courier_id>0:
        pass
    else:
        return redirect("/couriers")


    try:
        courier = Courier.objects.get(id=courier_id)
        courier.delete()
    except Exception:
        pass

    return redirect("/couriers")


def courier_update(request, courier_id):
    lomauser = LomaUser.objects.get(user=request.user)
    current_background = CustomBackground.objects.get(user=lomauser)
    if request.POST:
        backgroundForm = CustomBackgroundForm(request.POST, instance=current_background)
        if backgroundForm.is_valid():
            backgroundForm.save()
            return redirect('/orders')
    backgroundForm = CustomBackgroundForm(instance=current_background)
    courier = Courier.objects.get(id=courier_id)

    if request.method == 'POST':
        form = CourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()
            return redirect('/couriers/'+str(courier_id)+'/info', courier.id)
    else:
        form = CourierForm(instance=courier)

    return render(request, "couriers/new_courier.html", { "backgroundimg" : current_background.background,
        "backgroundform": backgroundForm,"form":form, })
