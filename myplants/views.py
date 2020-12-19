from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plant
from account.models import Account
from wishlist.models import Wish
from .forms import PlantForm

@login_required(login_url='login/')
def index(request):
    plants = Plant.objects.filter(user=request.user)
    wishes = Wish.objects.filter(user=request.user)
    accounts = Account.objects.all()
    # myAccount = Account.objects.get(user=request.user)

    context = {'plants' : plants, 'wishes' : wishes, 'accounts' : accounts}
    return render(request, 'myplants/index.html', context)

def add_plant(request):
    plants = Plant.objects.filter(user=request.user)

    if request.method == 'POST':
        form = PlantForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = PlantForm()

    context = {'form' : form, 'plants' : plants}
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
