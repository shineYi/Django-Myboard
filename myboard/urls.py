from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='dashboard'),
    url(r'^add/$', views.post_add, name='add_post'),
    url(r'^edit/(?P<pk>\d+)/$', views.post_edit, name='edit_post'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='detail_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/comment/(?P<c_pk>\d+)/edit/$', views.edit_comment, name='edit_comment'),

]
