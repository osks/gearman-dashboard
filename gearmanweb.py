#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import web
import gearman



gearman_hostports = [('localhost', 4730), ('localhost', 4731)]
gearman_connections = {}
for hostport in gearman_hostports:
    gearman_connections[hostport] = gearman.GearmanAdminClient([hostport])

    
def _get_info_from_gearman():
    server_infos = []
    for hostport in gearman_hostports:
        server_info = { 'hostport': hostport }
        
        try:
            gm_conn = gearman_connections[hostport]
            version = gm_conn.get_version()
            status = gm_conn.get_status()
            cl_wks = gm_conn.get_workers()
            clients = [ w for w in cl_wks if len(w['tasks']) == 0 ]
            workers = [ w for w in cl_wks if len(w['tasks']) > 0 ]
            
            server_info['version'] = version
            server_info['status'] = status
            server_info['workers'] = workers
            server_info['clients'] = clients
            server_info['failed'] = False
        except:
            server_info['failed'] = True
        
        server_infos.append(server_info)
    return server_infos



class Helpers:
    @staticmethod
    def tab(name, path, current_tab = None):
        class_str = 'class="current"' if string.lower(current_tab) == string.lower(name) else ''
        return "<li %s><a href=\"%s\">%s</a></li>" % (class_str, path, name)


app = web.auto_application()

class Index(app.page):
    path = '/'
    def GET(self):
        raise web.seeother(Overview.path)

class Tab():
    def current_tab(self):
        return self.__class__.__name__

class Overview(Tab, app.page):
    path = '/overview'
    def GET(self):
        server_infos = _get_info_from_gearman()
        functions_html = render_partial._functions(server_infos)
        workers_html = render_partial._workers(server_infos)
        return render.overview(functions_html, workers_html, self.current_tab())

class Workers(Tab, app.page):
    path = '/workers'
    def GET(self):
        server_infos = _get_info_from_gearman()
        workers_html = render_partial._workers(server_infos)
        return render.workers(workers_html, self.current_tab())

class Clients(Tab, app.page):
    path = '/clients'
    def GET(self):
        server_infos = _get_info_from_gearman()
        clients_html = render_partial._clients(server_infos)
        return render.workers(clients_html, self.current_tab())

class Functions(Tab, app.page):
    path = '/functions'
    def GET(self):
        # check mysql?
        server_infos = _get_info_from_gearman()
        functions_html = render_partial._functions(server_infos)
        return render.functions(functions_html, self.current_tab())
        

tabs = [ (cl.__name__, cl.path) for cl in [Overview, Workers, Clients, Functions] ]


t_globals = {
    'tabs': tabs,
    'print_tab': Helpers.tab,
}

render_partial = web.template.render('templates/', globals=t_globals)
render = web.template.render('templates/', base='layout', globals=t_globals)


if __name__ == "__main__":
    app.run()
