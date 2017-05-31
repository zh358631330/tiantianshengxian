from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.index),
    url('^register', views.register),
    url('^login', views.login),
    url('^user_center_info', views.user_center_info),
    url('^user_center_site', views.user_center_site),
    url('^user_center_info', views.user_center_info),
    url('^cart', views.cart),
    url('^user_center_order', views.user_center_order),
]