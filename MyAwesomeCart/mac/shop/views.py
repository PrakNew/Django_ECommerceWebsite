from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product
from django.db.models import Q
# Create your views here.

def index(request):
    # return HttpResponse('heyyyyy how you doin!!!! shoppppppppppp')
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={"allProds":allProds}
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)

def test(request):
    # return HttpResponse('heyyyyy how you doin!!!! shoppppppppppp')
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={"allProds":allProds}
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    return render(request, 'shop/indextest.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

