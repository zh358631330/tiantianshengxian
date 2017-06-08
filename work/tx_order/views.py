#coding:utf-8
from django.shortcuts import render
from tx_cart.models import *
from tx_user import user_decorator,models
from django.http import JsonResponse
# Create your views here.
@user_decorator.login
def order(request):
    user_id = request.session.get('user_id')
    user = models.UserInfo.objects.get(id=user_id)
    carts_list = request.GET.getlist('cart.id')

    carts= CartInfo.objects.filter(id__in=carts_list)
    context={'title':'提交订单',
             'carts':carts,
             'user':user
    }
    return render(request,'tx_order/place_order.html',context)