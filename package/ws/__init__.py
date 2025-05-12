from package import app
from flask_socketio import SocketIO, join_room, rooms
from package.models.user import User
from .cluster_groups import ClusterGroups
from .cluster_groups_array import ClusterGroupsArray
from flask import request
sio = SocketIO(app, cors_allowed_origins='*')

cluster_groups_array = ClusterGroupsArray()

@sio.on('connect')
def connect(auth):
    if not auth or 'token' not in auth:
        raise ConnectionRefusedError('Authentication token is required')
    user = User.query.filter_by(usertoken=auth['token']).first()
    if not user:
        raise ConnectionRefusedError('Invalid authentication token')
    
    cluster_group = cluster_groups_array.find_cluster_group_by_name(user.username)
    if cluster_group:
        if 'ip' in auth:
            cluster_group.add_cluster({"ip": auth['ip'], "sid": request.sid})
        else:
            cluster_group.add_cluster({"sid": request.sid})
      
        print('Cluster group:', cluster_group.get_clusters())
    else:
        cluster_group = ClusterGroups(user.username)
        if 'ip' in auth: 
            cluster_group.add_cluster({"ip": auth['ip'], "sid": request.sid})         
        else:
            cluster_group.add_cluster({"sid": request.sid})

        cluster_groups_array.add_cluster_group(cluster_group)
        print('Cluster group:', cluster_group.get_clusters())

    join_room(user.username)
    print('Client connected:', ) 

@sio.on('disconnect')
def disconnect():
    print('Client disconnected:', request.sid)
    group = cluster_groups_array.find_cluster_group_by_sid(request.sid)
    if group:
        group.remove_cluster_by_sid(request.sid)
        if group.get_clusters() == []:
            cluster_groups_array.remove_cluster_group(group)
            print('Cluster group removed:', group.name)
        print('Cluster group after disconnect:', group.get_clusters())

@sio.on('get_cluster')
def get_cluster():
    print('Client:', request.sid)
    group = cluster_groups_array.find_cluster_group_by_sid(request.sid)
    
    data = []

    for cluster in group.get_clusters():
        if 'ip' in cluster:
            data.append({"ip": cluster['ip']})
        
    print('Cluster ips:', data)
    return data

@sio.on('*')
def catch_all(event, data):
    if "ip" in data:
        group = cluster_groups_array.find_cluster_group_by_ip(data['ip'])
        cluster = group.find_cluster_by_ip(data['ip'])
        if cluster:
            print('Cluster:', cluster)
            sid = cluster['sid']
            sio.emit(event, data, to=sid)    
    else:
        group = cluster_groups_array.find_cluster_group_by_sid(request.sid)
        client = group.find_client()
        if client:
            print('Client:', client)
            sio.emit(event, data, to=client['sid'])
        else:
            print('Client not found in group:', group.name)
