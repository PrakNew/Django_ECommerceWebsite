from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  #  return HttpResponse('heyyyyy how you doin!!!! blogggggggg')
  return render(request,'blog/index.html')
