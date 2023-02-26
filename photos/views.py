from django.shortcuts import render, redirect
from .models import *

def gallery(request):
    category_searched = request.GET.get('category_clicked')
    if category_searched == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category_searched)

    categories = Category.objects.all()
    
    return render(request, 'photos/gallery.html', context={'categories': categories, 'photos': photos})

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', context={'photo': photo})

def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image_posted = request.FILES.get('image')

        if data['category'] != 'none':
            category_name = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category_name, created = Category.objects.get_or_create(name=data['category_new'])

        else:
            category_name = None
        
        photo = Photo.objects.create(
            category = category_name,
            image = image_posted,
            description = data['description']
        )

        return redirect("/")

    return render(request, 'photos/add.html', context={'categories': categories})