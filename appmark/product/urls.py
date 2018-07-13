from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^products/$', views.product_list),
    url(r'^products/(?P<pk>[0-9]+)/$', views.product_detail),
]