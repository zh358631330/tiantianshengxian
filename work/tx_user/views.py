from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'tianxian/register.html')

def user_center_info(request):
    return render(request,'tianxian/tinaxianuser_center_info.html')

def user_center_site(request):
    return render(request,'tianxian/user_center_site.html')

def user_center_order(request):
    return render(request,'tianxian/user_center_order.html')






