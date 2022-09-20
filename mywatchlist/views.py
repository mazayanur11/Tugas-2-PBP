from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchListItem.objects.all()
    result = " "
    watch = 0
    unwatched = 0

    for movie in data_barang_mywatchlist:
        if (movie.watched): 
            watch += 1
        else: 
            unwatched += 1

    if watch >= unwatched: 
        result = "Selamat, kamu sudah banyak menonton!"
    else:
        result = "Wah, kamu masih sedikit menonton!" 

    context = {
        'list_barang': data_barang_mywatchlist,
        'nama': 'Mazaya Nur Labiba',
        'npm': '2106639485',
        'result': result,
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")