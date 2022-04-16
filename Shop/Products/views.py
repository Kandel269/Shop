from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


# Create your views here.

def index(request):
    # allBoardGame = Product.objects.all()
    # oneBoardGame = Product.objects.get(pk = 6)
    # categoryBoardGame = Product.objects.filter(Category = 3)
    # ProducerBoardGame = Product.objects.filter(Producer = 1)
    # priceBoardGame = Product.objects.filter(price = 80)
    # categoryName = Category.objects.get(id = 2)
    # null = Product.objects.filter(Category__isnull=True)
    # notNull = Product.objects.filter(Category__isnull=False)
    # containsBoardGame = Product.objects.filter(describe__icontains = '-')
    category = Category.objects.all()
    data = {'category': category}
    return render(request, 'templates.html', data)

def category(request, id):
    category_user = Category.objects.get(pk = id)
    return HttpResponse(category_user)

def product(request, id):
    product_user = Product.objects.get(pk = id)
    data = {'product_user' : product_user}
    return render(request, 'Product.html', data)