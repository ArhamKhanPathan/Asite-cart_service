from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact
def index(request):
    # products = product.objects.all()
    # print(products)
    # n = len(products)
    # no_of_slides = n//4 + ceil((n//4)+(n//4))

    # params = {'no_of_slides': no_of_slides, 'range': range(1,no_of_slides),  'products': products}
    # all_prods = [[products, range(1, no_of_slides), no_of_slides],[products, range(1, no_of_slides), no_of_slides]]
    all_prods =[]
    all_cat = product.objects.values('category','id')
    cats = {item['category'] for item in all_cat}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        no_of_slides = n//4 + ceil((n//4)+(n//4))
        all_prods.append([prod, range(1,no_of_slides), no_of_slides])
    params = {"all_prods": all_prods}
    return render(request, 'shop/index.html', params)
# Create your views here.

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', ' ')
        email = request.POST.get('email', ' ')
        phone = request.POST.get('phone', ' ')
        desc = request.POST.get('desc', ' ')
        print(name, email, phone, desc)
        cont = Contact(name=name, email=email, phone=phone, desc=desc)
        cont.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodView(request, myid):
    # fetch the product using id
    pro = product.objects.filter(id = myid)
    # print(pro)
    return render(request, 'shop/prodView.html', {'product': pro[0]})    #

def checkout(request):
    return render(request, 'shop/checkout.html')