from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import UserListCreateAPIView,UserLoginAPIView,UserLogoutAPIView
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^register', UserListCreateAPIView.as_view(), name='user-register'),
    url(r'^login', UserLoginAPIView.as_view(), name='user-login'),
    url(r'^logout', UserLogoutAPIView.as_view(), name='user-logout'),
]
