import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import ProductEntry  
from main.forms import ProductEntryForm
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')

def show_main(request):
    products = ProductEntry.objects.filter(user=request.user)

    context = {
        'npm': '2306244886',
        'nama': request.user.username,
        'kelas': 'PBP C',
        'shop_name':'INTI JAYA',  
        'product_entry' : products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_name_entry(request):
    form = ProductEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        name_entry = form.save(commit=False)
        name_entry.user = request.user
        name_entry.save()
        return redirect('main:show_main')
    context={'form':form}
    return render(request,'create_name_entry.html',context)

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type='application/json')

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response