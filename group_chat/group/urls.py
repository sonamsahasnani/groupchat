
from django.conf.urls import include, url
from .views import GroupCreateAPIView,GroupAddMembersAPIView,GroupSearchMembersAPIView

urlpatterns = [
    url(r'^create', GroupCreateAPIView.as_view(), name='group-create'),
    url('group/(?P<pk>\d+)/add_member/',GroupAddMembersAPIView.as_view(),name='group-add-members'),
    url('group/(?P<pk>\d+)/search_member/',GroupSearchMembersAPIView.as_view(),name='group-search-members')

]
