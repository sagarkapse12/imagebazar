from django.shortcuts import render,redirect

from .models import *
def show_image(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context={'images':images,
             'categories':categories}




    return render(request,"imageapp/index.html",context)

def show_category(request,cid):
    categories = Category.objects.all()
    category = Category.objects.get(pk=cid)
    print(category)

    images = Image.objects.filter(cat=category)
    context = {'images': images,
               'categories': categories}
    return render(request, "imageapp/index.html", context)


def home(request):
    return redirect('/home/')

