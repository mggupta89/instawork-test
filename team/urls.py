from django.urls import path

from team.team_action import TeamAction

urlpatterns = [
    path('', TeamAction.as_view()),
    path('<int:id>/', TeamAction.as_view()),
]