from django.shortcuts import render
from django.db.models import Q
from myplants.models import Plant
from wishlist.models import Wish
from .forms import SearchForm

def search_plants(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(name__icontains=query)
            results= Plant.objects.filter(lookups).distinct()
            print(results)
            similar = []
            perfect = []

            print("Search for:", query)
            print(request.user, "wants this plant")
            plants = Plant.objects.filter(user=request.user)
            print(request.user, "has these plants: ", plants)

            for result in results:
                print(result.user, "has this plant")
                wishes = Wish.objects.filter(user=result.user)
                print(result.user, "wants these plants: ", wishes)
                matches = plants.filter(name__in=wishes.values_list('name'))
                print("Matches:", matches)
                if not matches:
                    similar.append(result)
                    print("Not a perfect match.", similar)
                else:
                    perfect.append(result)
                    print("This is a perfect match!", perfect)

            context={'results': results,
                    'similar': similar,
                    'perfect': perfect,
                    'submitbutton': submitbutton}

            return render(request, 'swaps/swaps.html', context)
        else:
            return render(request, 'swaps/swaps.html')
    else:
        return render(request, 'swaps/swaps.html')

