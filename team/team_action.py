import utils
from exceptions import InstaworkException
from response.base import APIResponseBase
from team.team_helper import TeamHelper
from django.conf import settings


class TeamAction(APIResponseBase):
    def __init__(self, **kwargs):
        super(TeamAction, self).__init__(**kwargs)
        self.team_helper = TeamHelper()

    '''
    If no team id, then return all teams
    If team id is in url, then return the particular team
    '''
    def get_action(self, request, *args, **kwargs):
        ctxt = {}
        self._data = ctxt
        team_id = kwargs.get('id')
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


    def delete_action(self, request, *args, **kwargs):
        team_id = kwargs.get('id')
        if not team_id:
            self.set_bad_req("Invalid team")
        from exceptions import InstaworkException
        try:
            self.team_helper.delete_team(team_id)
        except InstaworkException as e:
            self.set_error(str(e))
        return self._data

    def post_action(self, request, *args, **kwargs):
        ctxt = {}
        self._data = ctxt
        post_data = request.POST
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        phone = post_data.get('phone')
        email = post_data.get('email')
        role = post_data.get('role')
        self.validate_data(first_name, last_name, email, phone, role)

        if self.errors:
            self.set_bad_req('Invalid data')
            return self._data
        else:
            try:
                team = self.team_helper.create_team(first_name, last_name, email, phone, role)
            except InstaworkException as e:
                self.set_error(str(e))
                return self._data
            ctxt['team'] = team.to_json()
            return self._data

    def put_action(self, request, *args, **kwargs):
        ctxt = {}
        self._data = ctxt
        team_id = kwargs.get('id')
        if not team_id:
            self.set_bad_req('Invalid team')
        post_data = request.body
        print(post_data)
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        phone = post_data.get('phone')
        email = post_data.get('email')
        role = post_data.get('role')
        if first_name:
            self.validate_first_name(first_name)
        if last_name:
            self.validate_last_name(last_name)
        if email:
            self.validate_email(email)
        if phone:
            self.validate_phone(phone)
        if role:
            self.validate_role(role)
        if self.errors:
            self.set_bad_req('Invalid data')
            return self._data
        print(email)
        try:
            team = self.team_helper.update_team(team_id, first_name, last_name, email, phone, role)
        except InstaworkException as e:
            self.set_error(str(e))
            return self._data
        ctxt['team'] = team.to_json()
        return self._data


    def validate_data(self, first_name, last_name, email, phone, role):
        self.validate_first_name(first_name)
        self.validate_last_name(last_name)
        self.validate_email(email)
        self.validate_phone(phone)
        self.validate_role(role)

    def validate_first_name(self, first_name):
        if not first_name:
            self.errors.append('First name required')

    def validate_last_name(self, last_name):
        if not last_name:
            self.errors.append('Last name required')

    def validate_email(self, email):
        if not email or not utils.is_valid_email(email):
            self.errors.append('Invalid email')

    def validate_phone(self, phone):
        if not phone:
            self.errors.append('Invalid phone')

    def validate_role(self, role):
        if not role or role not in settings.INSTA_ROLES:
            self.errors.append('Invalid role')

