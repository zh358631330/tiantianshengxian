from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'tianxian/index.html')

def register(request):
    return render(request,'tianxian/register.html')

def user_center_info(request):
    return render(request,'tianxian/user_center_info.html')

def user_center_site(request):
    return render(request,'tianxian/user_center_site.html')

def user_center_order(request):
    return render(request,'tianxian/user_center_order.html')

def login(request):
    return render(request, 'tianxian/login.html')

def cart(request):
    return render(request, 'tianxian/cart.html')

def user_center_order(request):
    return render(request, 'tianxian/user_center_order.html')








