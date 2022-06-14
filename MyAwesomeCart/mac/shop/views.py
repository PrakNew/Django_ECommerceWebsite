from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product
from django.db.models import Q
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
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
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html", {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')