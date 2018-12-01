from django.conf.urls import url, include

from team.team_action import TeamAction

urlpatterns = [
    url(r'^', TeamAction.as_view()),
    url(r'^/(?P<team_id>\d+)/$', TeamAction.as_view()),
]