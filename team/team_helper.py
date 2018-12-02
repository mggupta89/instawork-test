from django.db import IntegrityError

from team.models import Team
from exceptions import InstaworkException

class TeamHelper(object):

    def get_team_by_id(self, team_id):
        try:
            return Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return None

    def delete_team(self, team_id):
        team = self.get_team_by_id(team_id)
        if not team:
            raise InstaworkException('Invalid team')
        team.delete()

    def get_all_teams(self):
        return Team.objects.all()


    def create_team(self, first_name, last_name, email, phone, role):
        try:
            team = Team.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, role=role)
        except IntegrityError as e:
            raise InstaworkException('Email already exists')
        return team

    def update_team(self, team_id, first_name='', last_name='', email='', phone='', role=''):
        team = self.get_team_by_id(team_id)
        if not team:
            raise InstaworkException('Invalid team')
        if first_name:
            team.first_name=first_name
        if last_name:
            team.last_name=last_name
        if email:
            team.email=email
        if phone:
            team.phone=phone
        if role:
            team.role=role
        print(team.email)
        team.save()
        return team

