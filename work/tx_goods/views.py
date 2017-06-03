#coding:utf-8
from django.shortcuts import render
from models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    t1_click = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    t1_new = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    t3_click = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
    t3_new = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    t4_click = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    t4_new = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t5_new = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    t6_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t6_new = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    context={'title':'首页', 't1_click':t1_click, 't1_new':t1_new,
             't3_click':t3_click, 't3_new':t3_new,
             't4_click':t4_click, 't4_new':t4_new,
             't5_click':t5_click, 't5_new':t5_new,
             't6_click':t6_click, 't6_new':t6_new}
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
def list(request):
    t1_click = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:3]
    t1_news =GoodsInfo.objects.filter(gtype_id=1).order_by('-id')
    context={'title':'水果','t1_click':t1_click, 't1_news':t1_news}
    return render(request,'tx_goods/list.html',context)

def detail(request):
    return render(request,'tx_goods/detail.html')
