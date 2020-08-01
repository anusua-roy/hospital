from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.user, name='user'),
    path('user/roomlist', views.roomlist, name='roomlist'),
    path('user/lablist', views.lablist, name='lablist'),
    path('user/doclist', views.doclist, name='doclist'),
    path('user/patientlist', views.patientlist, name='patientlist'),
    path('user/patientlist/bill', views.bill, name='bill'),
    path('user/profile', views.profile, name='profile'),
]