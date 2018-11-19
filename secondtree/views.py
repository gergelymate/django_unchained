from django.shortcuts import render
from django.http import Http404
from .models import ItemDet
#Lekérdezi az adatbázisból a tárgyakat
def index(request): 
	all_itemdets = ItemDet.objects.all()
	return render(request, 'sitee/index.html', {'all_itemdets':all_itemdets})


# X tárgyat nyitja meg ami a fő oldalt kivan listázva.
def detail(request, ItemDet_id):
	try:
		item = ItemDet.objects.get(pk=ItemDet_id)
	except ItemDet.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'sitee/item.html', {'item':item})