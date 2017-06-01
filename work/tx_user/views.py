# coding=utf-8
from django.shortcuts import render,redirect
from models import UserInfo
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
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
    count = UserInfo.objects.filter(uname=uname).count()
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
            url=request.COOKIES.get('url','/')
            red=HttpResponseRedirect(url)
            red.set_cookie('url','',max_age=-1)
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=uname
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

def user_center_info(request):
    return render(request,'tx_user/user_center_info.html')

def user_center_site(request):
    return render(request,'tx_user/user_center_site.html')

def user_center_order(request):
    return render(request,'tx_user/user_center_order.html' )

# def join(request):







