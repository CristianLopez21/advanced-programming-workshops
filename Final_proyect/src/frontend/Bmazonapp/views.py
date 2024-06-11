from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def create_account(request):
    return render (request, 'create_account.html')

def add_product(request):
    return render (request, 'add_product.html')

def electronics(request):
    return render (request, 'electronics.html')

def fashion(request):
    return render (request, 'fashion.html')

def homekitchen(request):
    return render (request, 'homekitchen.html')

def product1(request):
    return render (request, 'product1.html')

def shopping_cart(request):
    return render (request, 'shopping_cart.html')

def sportfitness(request):
    return render (request, 'sportfitness.html')
