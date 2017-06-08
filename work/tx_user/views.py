# coding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
from tx_goods.models import *

import user_decorator
# Create your views here.
def register(request):
    context = {'title':'用户注册/login.'}
    return render(request,'tx_user/register.html',context)

def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    if upwd != upwd2:
        return redirect('/user/register/')
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.ozbjects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title':'登陆','error_name': 0,'error_pwd': 0,'uname':uname}
    return render(request,'tx_user/login.html',context)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu=post.get('jizhu',0)
    user=UserInfo.objects.filter(uname=uname)
    # print(user[0])
    if len(user) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == user[0].upwd:
            url=request.COOKIES.get('red_url','/')
            red=HttpResponseRedirect(url)
            red.set_cookie('url','',max_age=-1)
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=uname
            request.session.set_expiry(0)
            return red
        else:
            context = {'title':'用户登录','error_name':0,
                       'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'tx_user/login.html',context)
    else:
        context={'title':'用户登录', 'error_name' : 1,
                       'error_pwd' : 0, 'uname':uname,'upwd':upwd}
        return render(request,'tx_user/login.html',context)
    return render(request,'tx_user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def user_center_info(request):
    name = request.session['user_name']
    info=UserInfo.objects.filter(uname=name)
    uname=info[0].uname
    uaddress=info[0].uaddress
    uphone=info[0].uphone

    goods_ids = request.COOKIES.get('goods_ids','')
    print(goods_ids)
    if goods_ids != '':
        goods_list = goods_ids.split(',')
        goods_li = []
        for gid in goods_list:
            print(gid)
            goods = GoodsInfo.objects.get(id = int(gid))
            goods_li.append(goods)
    else:
        goods_li = None
    context={'title':'用户中心',
             'uname':uname,
             'uaddress':uaddress,
             'uphone':uphone,
             'goods_li':goods_li}
    return render(request,'tx_user/user_center_info.html',context)

@user_decorator.login
def user_center_site(request):
    name = request.session['user_name']
    info = UserInfo.objects.filter(uname=name)
    ushou = info[0].ushou
    uaddr = info[0].uaddress
    uphone = info[0].uphone
    context = {'title':'用户中心','ushou': ushou, 'uaddr': uaddr, 'uphone': uphone}
    return render(request,'tx_user/user_center_site.html',context)

@user_decorator.login
def site(request):
    post=request.POST
    ushou=post.get('ushou')
    uaddr=post.get('uaddr')
    uyoubian=post.get('uyoubian')
    uphone=post.get('uphone')
    user = UserInfo.objects.get(id=request.session['user_id'])
    user.ushou=ushou
    user.uaddress=uaddr
    user.uyoubian=uyoubian
    user.uphone=uphone
    user.save()
    context ={'title':'用户中心','ushou':ushou,'uaddr':uaddr, 'uyou':uyoubian, 'uphone':uphone,'user':user}

    return HttpResponseRedirect('/user/user_center_site/',context)

@user_decorator.login
def user_center_order(request):
    return render(request,'tx_user/user_center_order.html' )

# def join(request):







