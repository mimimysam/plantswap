from django.shortcuts import render, redirect
from .models import Wish
from .forms import WishForm

def add_wish(request):
    wishes = Wish.objects.all()

    if request.method == 'POST':
        form = WishForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WishForm()

    context = {'form' : form, 'wishes' : wishes}
    return render(request, 'wishlist/add_wish.html', context)

def update_wish(request, pk):
    wish = Wish.objects.get(id=pk)

    form = WishForm(instance=wish)

    if request.method == 'POST':
        form = WishForm(request.POST, instance=wish)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}

    return render(request, 'wishlist/update_wish.html', context)

def delete_wish(request, pk):
	wish = Wish.objects.get(id=pk)

	if request.method == 'POST':
		wish.delete()
		return redirect('home')

	context = {'wish' : wish}
	return render(request, 'wishlist/delete_wish.html', context)
