from django.conf.urls import include, url
from .views import MessageLikeAPIView,MessageListCreateAPIView

urlpatterns = [
    url(r'', MessageListCreateAPIView.as_view(), name='message-create'),
    url(r'^(?P<pk>\d+)/like',MessageLikeAPIView.as_view(),name='message-like')

]
