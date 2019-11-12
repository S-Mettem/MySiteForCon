from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Sight


# Create your views here.
def index(request):
    return render(request, 'index.html')


def map_view(request):
    return render(request, 'map.html')


def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)


def category_view(request, cat_name):
    category = Category.objects.get(name=cat_name)
    sights = Sight.objects.filter(category=category)
    context = {'category': category, 'sights': sights}
    return render(request, 'category.html', context)


def sight_view(request, cat_name, sight_name):
    category = Category.objects.get(name=cat_name)
    sight = Sight.objects.get(name=sight_name)
    context = {'category': category, 'sight': sight}
    return render(request, 'sight.html', context)
