from django.views.generic.base import View
from django.http import HttpResponse
import json

class APIResponseBase(View):
    def __init__(self, **kwargs):
        super(APIResponseBase, self).__init__(**kwargs)
        self._data = {}
        self.status_code = 200
        self.status = 'success'
        self.errors = []
        self.message = ''

    def render_to_response(self, **response_kwargs):
        _context = {}
        _context.update({'data': self._data})
        _context.update({
            'status': self.status,
            'status_code': self.status_code,
            'message': self.message,
            'errors': self.errors,
        })
        return HttpResponse(json.dumps(_context))

    def get(self, request, *args, **kwargs):
        self.get_action(request, *args, **kwargs)
        return self.render_to_response()

    def put(self, request, *args, **kwargs):
        self.put_action(request, *args, **kwargs)
        return self.render_to_response()

    def post(self, request, *args, **kwargs):
        self.post_action(request, *args, **kwargs)
        return self.render_to_response()

    def delete(self, request, *args, **kwargs):
        self.delete_action(request, *args, **kwargs)
        return self.render_to_response()

    def set_status(self, status, status_code, msg):
        self.status = status
        self.status_code = status_code
        self.message = msg

    def set_success(self, msg=''):
        self.status = 'success'
        self.status_code = 200
        self.message = msg

    def set_bad_req(self, msg):
        self.status = 'failed'
        self.status_code = 400
        self.message = msg

    def set_error(self, msg):
        self.status = 'failed'
        self.status_code = 500
        self.message = msg