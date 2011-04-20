import gearman

gearman_hostports = [('gearman01', 4730), ('gearman02', 4730)]
gearman_connections = {}
for hostport in gearman_hostports:
    gearman_connections[hostport] = gearman.GearmanAdminClient([hostport])


def get_info_from_gearman():
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
