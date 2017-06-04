#coding:utf-8
from django.shortcuts import render
from models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
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
             'list':list
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
    context = {'title':'主页','clicks':clicks,'news':news}
    return JsonResponse(context)
def list(request,tid,lid,sid):
    t1_click = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    new = GoodsInfo.objects.filter(gtype_id=int(tid))
    if sid == '1':
        t1_list =new.order_by('-id')
    elif sid == '2':
        t1_list = new.order_by('-gprice')
    elif sid == '3':
        t1_list = new.order_by('-gclick')
    paginator=Paginator(t1_list,1)
    page=paginator.page(int(lid))
    type_name = TypeInfo.objects.get(id=int(tid)).ttitle

    context={'title':type_name,'t1_click':t1_click, 'page':page,'lid':lid,'tid':tid}
    return render(request,'tx_goods/list.html',context)

def sort(request,tid,lid):

    t1_click = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]
    t1_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    paginator = Paginator(t1_list, 5)
    page = paginator.page(lid)
    type_name = TypeInfo.objects.get(id=int(tid)).ttitle

    context = {'title': type_name, 't1_click': t1_click, 'page': page, 'lid': lid, 'tid': tid}
    return JsonResponse(context)

def ceshi(request):
    return render(request,'tx_goods/ceshi.html')

def detail(request,tid,lid):
    goods= GoodsInfo.objects.get(id=lid)
    gtype = TypeInfo.objects.filter(goodsinfo__id=lid)[0]
    t1_click = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')[0:2]
    context={'title':'商品详情',
             'goods':goods,
             't1_click':t1_click
             }
    return render(request,'tx_goods/detail.html',context)
