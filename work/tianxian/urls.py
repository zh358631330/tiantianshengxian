from django.conf.urls import url
import views
urlpatterns=[
    url('^index/$',views.index),
    url('^cart/$', views.cart),
]