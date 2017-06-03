#coding=utf-8
from django.shortcuts import render
from tx_user import user_decorator
# Create your views here.
@user_decorator.login
def cart(request):
    context={'title':'购物车'}
    return render(request,'tx_cart/cart.html',context)