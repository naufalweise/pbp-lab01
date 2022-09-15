from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

def show_wishlist(request):
	data_barang_wishlist = BarangWishlist.objects.all()
	context = {
		'list_barang': data_barang_wishlist,
    	'nama': 'Weise'
	}
	return render(request, "wishlist.html", context)

def get_xml(request):
	data = BarangWishlist.objects.all()
	return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def get_json(request):
	data = BarangWishlist.objects.all()
	return HttpResponse(serializers.serialize("json", data), content_type="application/json")
	
def get_json_by_id(request, id):
	data = BarangWishlist.objects.filter(pk=id)
	return HttpResponse(serializers.serialize("json", data), content_type="application/json")