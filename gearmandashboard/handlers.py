import logging

from pyramid_handlers import action
from pyramid.httpexceptions import HTTPFound

import gearmandashboard.models as model

log = logging.getLogger(__name__)


class Handler(object):
    def __init__(self, request):
        self.request = request
        self.url = self.request.url_generator


class Main(Handler):
    def __init__(self, request):
        Handler.__init__(self, request)
        self.server_infos = model.get_info_from_gearman()

    def tabs(self):
        return [ (action, self.url.route('main', action=action))
                 for action in
                 [ 'overview', 'workers', 'clients', 'functions' ] ]
            
    @action()
    def index(self):
        return HTTPFound(location=self.url.route('main', action='overview'))

    @action(renderer="overview.jinja2")
    def overview(self):
        return dict(tabs=self.tabs(), server_infos=self.server_infos, current_tab='overview')

    @action(renderer="workers.jinja2")
    def workers(self):
        return dict(tabs=self.tabs(), server_infos=self.server_infos, current_tab='workers')

    @action(renderer="clients.jinja2")
    def clients(self):
        return dict(tabs=self.tabs(), server_infos=self.server_infos, current_tab='clients')

    @action(renderer="functions.jinja2")
    def functions(self):
        return dict(tabs=self.tabs(), server_infos=self.server_infos, current_tab='functions')
