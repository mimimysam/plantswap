from django.shortcuts import render
from django.db.models import Q
from myplants.models import Plant
from .forms import SearchForm

def search_plants(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query)

            results= Plant.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'swaps/swaps.html', context)

        else:
            return render(request, 'swaps/swaps.html')

    else:
        return render(request, 'swaps/swaps.html')
