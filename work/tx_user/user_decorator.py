from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'login':0})
            else:
                return redirect('/user/login/')
            # red=HttpResponseRedirect('/user/login/')
            # red.set_cookie('url',request.get_full_path())
            # return red
    return login_fun