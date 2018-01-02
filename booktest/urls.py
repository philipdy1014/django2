from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
#    url(r'^myexp$', views.myExp),
    url(r'^uploadPic$', views.uploadPic),
    url(r'^uploadHandle$', views.uploadHandle),
    url(r'^herolist/(\d*)$', views.herolist),
    url(r'^area/$', views.area),
    url(r'^pro/$', views.pro),
    url(r'^city(\d+)/$', views.city),
    url(r'^dis(\d+)/$', views.dis),
    url(r'^htmlEditor/$', views.htmlEditor),
    url(r'^htmlEditorHandle/$', views.htmlEditorHandle),
    url(r'^cache1/$', views.cache1),
    url(r'^mysearch/$', views.mysearch),
    url(r'^celeryTest/$', views.celeryTest),
]