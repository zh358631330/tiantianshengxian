from django.conf.urls import url
import views

urlpatterns=[
    url('register/$',views.register),
    url('user_center_info/$',views.user_center_info),
    url('user_center_site/$', views.user_center_site),
    url('user_center_order/$', views.user_center_order),
]