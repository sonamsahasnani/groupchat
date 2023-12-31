"""group_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^groups/', include('group.urls')),
    url(r'^message/', include('group_messages.urls')),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
]
