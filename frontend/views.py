from django.shortcuts import render

from frontend.models import Index, PostImage
from frontend.models import LatestBlog
from frontend.models import *

# Create your views here.
def index(request):
    data=Index.objects.all()
    images=PostImage.objects.all()
    blogs=LatestBlog.objects.all()


    return render(request,"index.html",{'data':data,'images':images,'blogs':blogs})

def aboutus(request):
    about=AboutUs.objects.all()

    return render(request,"about-us.html",{'about':about})

def log(request):
    Blog=blog.objects.all()

    return render(request,"blog.html",{'Blog':Blog})


def con(request):
    cont=contact.objects.all()

    return render(request,"contact-us.html",{'cont':cont})        


def categories(request):
    cat=Category.objects.all()

    return render(request,"categories.html",{'cat':cat})

def candidate(request):

    return render(request,"candidate-listing.html")    