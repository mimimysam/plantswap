from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plant
from account.models import Account
from wishlist.models import Wish
from .forms import PlantForm
from wishlist.forms import WishForm
from django.http import JsonResponse

@login_required(login_url='login/')
def index(request):
    plants = Plant.objects.filter(user=request.user)
    wishes = Wish.objects.filter(user=request.user)
    accounts = Account.objects.all()

    context = {'plants' : plants, 'wishes' : wishes, 'accounts' : accounts}
    return render(request, 'myplants/index.html', context)

def add_plant(request):
    plants = Plant.objects.filter(user=request.user)
    wishes = Wish.objects.filter(user=request.user)

    if request.method == 'POST':
        plantform = PlantForm(request.POST)
        wishform = WishForm(request.POST)

        if plantform.is_valid():
            plantform.instance.user = request.user
            plantform.save()
            return redirect('home')

        if wishform.is_valid():
            wishform.instance.user = request.user
            wishform.save()
            return redirect('home')
    else:
        plantform = PlantForm()
        wishform = WishForm()

    context = {'plantform' : plantform, 'plants' : plants, 'wishform' : wishform, 'wishes' : wishes}
    return render(request, 'myplants/add_plant.html', context)

def update_plant(request, pk):
    plant = Plant.objects.get(id=pk)

    form = PlantForm(instance=plant)

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}

    return render(request, 'myplants/update_plant.html', context)

def delete_plant(request, pk):
	plant = Plant.objects.get(id=pk)

	if request.method == 'POST':
		plant.delete()
		return redirect('home')

	context = {'plant' : plant}
	return render(request, 'myplants/delete_plant.html', context)

def get_locations(request):
    resp = Account.objects.all().values('id', 'first_name', 'email', 'latitude', 'longitude')
    return JsonResponse(list(resp), safe=False)

def get_plants_by_user(request, pk):
    resp = Plant.objects.filter(user__id=pk).values('name')
    return JsonResponse(list(resp), safe=False)

def other_user(request, pk):
    plants = Plant.objects.filter(user__id=pk).values('name')
    wishes = Wish.objects.filter(user__id=pk).values('name')
    account = Account.objects.get(id=pk)

    context = {'plants' : plants, 'wishes' : wishes, 'account' : account}
    return render(request, 'myplants/other_user.html', context)