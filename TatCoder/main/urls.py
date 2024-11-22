from django.urls import path
from . import views

urlpatterns = [

       path('', views.index, name='index'),
       path('data/', views.data, name='data'),
       path('data/test/', views.test, name='test'),
       path('test/', views.test, name='test')
]

