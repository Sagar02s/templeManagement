from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login',userlogin, name='userlogin'),
    path('logout',userlogout, name='userlogout'),
    path('immovable',immovable, name='immovable'),
    path('movable',movable, name='movable'),
    path('inc_exp',incExp, name='inc_exp'),
    path('kaanike',kaanike, name='kaanike'),
    path('masters',masters, name='masters'),
    path('pooja_report',poojaReport, name='pooja_report'),
    path('user_report',userReport, name='user_report'),
    path('profile',profile, name='profile'),
    path('provision',provision, name='provision'),
    path('seva',seva, name='seva'),

]
