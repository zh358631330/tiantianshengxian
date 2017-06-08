#coding:utf-8
from django.shortcuts import render
from models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from tx_cart.models import *
# Create your views here.
def index(request):
    type_list=TypeInfo.objects.all()
    list = []
    for type in type_list:
        list.append({
            'type':type,
            'click_list': type.goodsinfo_set.order_by('-gclick')[0:3],
            'new_list': type.goodsinfo_set.order_by('-id')[0:4]
        })

    context={'title':'首页',
             'type_list':type_list,
             'list':list,
             'cart_count':cart_count(request)
            }
    return render(request,'tx_goods/index.html',context)

def index2(request,tid):
    t1_click = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[0:3]
    t1_new = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[0:4]
    clicks = []
    for click in t1_click:
        clicks.append({'id':click.id,'title':click.gtitle})
    news = []
    for new in t1_new:
        news.append({'id':new.id,'title':new.gtitle, 'pic':new.gpic.name,'price':new.gprice})
    context = {'title':'主页','clicks':clicks,'news':news,'cart_count':cart_count(request)}
    return JsonResponse(context)

def list(request, tid, lid, sid):
    t1_click = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]
    new = GoodsInfo.objects.filter(gtype_id=int(tid))
    if sid == '1':
        t1_list =new.order_by('-id')
    elif sid == '2':
        t1_list = new.order_by('-gprice')
    elif sid == '3':
        t1_list = new.order_by('-gclick')
    paginator=Paginator(t1_list,5)
    page=paginator.page(int(lid))
    type_name = TypeInfo.objects.get(id=int(tid)).ttitle

    context={'title':type_name,'t1_click':t1_click, 'page':page,'lid':lid,'tid':tid, 'sid':sid,'cart_count':cart_count(request)}
    return render(request,'tx_goods/list.html',context)

def ceshi(request):
    return render(request,'tx_goods/ceshi.html')

def detail(request,lid):
    goods= GoodsInfo.objects.get(id=lid)
    goods.gclick=goods.gclick+1
    goods.save()
    #gtype = TypeInfo.objects.filter(goodsinfo__id=lid)[0]
    t1_click = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'title':'商品详情',
             'goods':goods,
             't1_click':t1_click,
             'cart_count': cart_count(request)
             }
    response =  render(request,'tx_goods/detail.html',context)

    goods_id = "%d"%goods.id
    goods_ids = request.COOKIES.get('goods_ids','')
    if goods_ids != '':
        goods_list = goods_ids.split(',') #['1','2']
        if goods_id in goods_list:
            goods_list.remove(goods_id)
            goods_list.insert(0,goods_id)
        else:
            if len(goods_list) > 5:
                goods_list.pop()
            goods_list.append(goods_id)
        goods_ids = ','.join(goods_list)
    else:
        goods_ids = goods_id
    response.set_cookie('goods_ids',goods_ids)
    return response

def cart_count(request):
    if request.session.has_key('user_id'):
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return count
    else:
        return 0