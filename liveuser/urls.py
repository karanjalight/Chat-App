""" from django.urls import path
from liveuser.views import  log_out, log_in, sign_up, user_list


urlpatterns = [
    path('login/', log_in, name='log_in'),
    path('logout/', log_out, name='log_out'),
    path('signup/', sign_up, name='sign_up'),
    path('', user_list, name='user_list'),
] """

from django.urls import re_path
from liveuser.views import log_in, log_out, sign_up, user_list


urlpatterns = [
    re_path(r'^log_in/$', log_in, name='log_in'),
    re_path(r'^log_out/$', log_out, name='log_out'),
    re_path(r'^sign_up/$', sign_up, name='sign_up'),
    re_path(r'^$', user_list, name='user_list')
]