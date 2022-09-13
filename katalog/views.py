from django.shortcuts import render
from katalog.models import CatalogItem


# TODO: Create your views here.
def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_catalog,
        'nama': 'Mazaya Nur Labiba',
        'id': '2106639485',
    }
    return render(request, "katalog.html", context)
