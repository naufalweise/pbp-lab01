from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from wishlist.forms import WishlistForm
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_POST

@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Weise',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "wishlist.html", context)

@login_required(login_url='/wishlist/login/')
def show_wishlist_ajax(request):
    context = {
        'nama': 'Weise',
        'last_login': request.COOKIES['last_login'],
        'form': WishlistForm()
    }
    return render(request, "wishlist_ajax.html", context)


def get_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def get_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def get_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_xml_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response

@require_POST
def create_wishlist(request):
    form = WishlistForm(request.POST)
    if form.is_valid():
        form.save()
        print("OK")
        return HttpResponse(status=200)
    print(form.errors.as_json())
    return HttpResponse(status=400)
    