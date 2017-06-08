#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from tx_user import user_decorator
from models import *
from tx_user.user_decorator import *
# Create your views here.
@user_decorator.login
def cart(request):
    cart_list = CartInfo.objects.filter(user_id=request.session['user_id'])
    context = {'title': '购物车',
               'cart_list': cart_list}
    return render(request, 'tx_cart/cart.html', context)
@user_decorator.login
def add(request,lid,count):
    carts = CartInfo.objects.filter(goods_id=lid,user_id=request.session['user_id'])
    if len(carts) == 0:
        cart = CartInfo()
        cart.goods_id = int(lid)
        cart.user_id = request.session['user_id']
        cart.count = int(count)
        cart.save()
    else:
        carts[0].count += int(count)
        carts[0].save()
    if request.is_ajax():
        return JsonResponse({
            'count': CartInfo.objects.filter(user_id=request.session['user_id']).count()})
    else:
        return HttpResponse('ok')
@user_decorator.login
def delete(request):
    cid = request.GET.get('id')
    cart = CartInfo.objects.filter(id=cid)[0]
    cart.delete()
    return JsonResponse({'data':'ok'})
@user_decorator.login
def count_change(request):
    cart_id = int(request.GET.get('id'))
    count = int(request.GET.get('count'))
    cart = CartInfo.objects.get(id = cart_id)
    if  count > cart.goods.gkucun:
        count = cart.goods.gkucun
    cart.count = count
    cart.save()
    return JsonResponse({"data":"ok",'count':count})

