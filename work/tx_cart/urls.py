from django.conf.urls import url
import views
urlpatterns=[
    url('^$',views.cart),
    url('^add(\d+)_(\d+)/$',views.add),
    url('^del/$',views.delete),
    url('^count_change/$',views.count_change)
]