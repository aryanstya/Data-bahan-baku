from multiprocessing import context
from django.shortcuts import render
from main.models import dataBahan

def show_bahan(request):
    data_item_bahan = dataBahan.objects.all()
    context = {
        'list_Bahan' : data_item_bahan,
        'nama' : 'Aryan Primasatya',
        'NPM' : '2206081181',  
    }
    return render(request, "main.html", context)
# TODO: Create your views here.