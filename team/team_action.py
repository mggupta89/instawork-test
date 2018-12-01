from response.base import APIResponseBase
from django.http import HttpResponse
import logging

from team.team_helper import TeamHelper


class TeamAction(APIResponseBase):

    def __init__(self, **kwargs):
        super(TeamAction, self).__init__(**kwargs)
        self.team_helper = TeamHelper()

    '''
    If no team id, then return all teams
    If team id is in url, then return the particular team
    '''
    def get_action(self):
        ctxt = {}
        self._data = ctxt
        team_id = self.request.GET.get('team_id')
        if not team_id:
            teams = self.team_helper.get_all_teams()
            ctxt['teams'] = [t.to_json() for t in teams]
        else:
            team = self.team_helper.get_team_by_id(team_id)
            if not team:
                self.set_bad_req('Invalid team id')
            else:
                ctxt['team'] = team.to_json()
            return self._data


    def delete_action(self):
        pass

    def put_action(self):
        pass

