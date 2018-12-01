from team.models import Team

class TeamHelper(object):

    def get_team_by_id(self, team_id):
        try:
            return Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return None

    def delete_team(self, team_id):
        pass