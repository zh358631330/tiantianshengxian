from django.conf.urls import url
import views

urlpatterns=[
    url('^$',views.index),

    url('^ceshi$',views.ceshi),
    url('^sort$',views.sort),

    url('^index2(\d+)/$',views.index2),
    url('^list(\d+)_(\d+)*/$',views.list),
    url('^detail(\d+)_(\d+)+/$', views.detail),
]