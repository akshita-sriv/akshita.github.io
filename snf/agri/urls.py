from . import views
from django.conf.urls import url
urlpatterns =[
    url(r'^$', views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^update/$',views.update,name='update'),
    url(r'^updateform/$',views.updateform,name='updateform'),
    url(r'^naturalfarming/$',views.naturalfarming,name='naturalfarming'),
    url(r'^farmingbenefits/$',views.farmingbenefits,name='farmingbenefits'),
    url(r'^index_loggedin/$',views.index_loggedin,name='index_loggedin'),
    url(r'^farmerdetails/$',views.farmerdetails,name='farmerdetails'),
    ]
     
     
