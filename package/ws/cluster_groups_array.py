class ClusterGroupsArray:
    """
    Class to manage cluster groups.
    """

    def __init__(self):
        """
        Initialize the ClusterGroupsArray object.
        """
        self.cluster_groups_array = []

    def get_cluster_groups(self):
        """
        Get the list of cluster groups.

        :return: List of cluster groups.
        """
        return self.cluster_groups_array
    
    def add_cluster_group(self, cluster_group):
        """
        Add a new cluster group.

        :param cluster_group: Cluster group to add.
        """
        self.cluster_groups_array.append(cluster_group)

    def remove_cluster_group(self, cluster_group):
        """
        Remove a cluster group.

        :param cluster_group: Cluster group to remove.
        """
        self.cluster_groups_array.remove(cluster_group)

    def find_cluster_group_by_name(self, name):
        """
        Find a cluster group by name.

        :param name: Name of the cluster group to find.
        :return: Cluster group if found, None otherwise.
        """
        for cluster_group in self.cluster_groups_array:
            if cluster_group.name == name:
                return cluster_group
        return None
    
    def find_cluster_group_by_sid(self, sid):
        """
        Find a cluster group by session ID.

        :param sid: Session ID of the cluster group to find.
        :return: Cluster group if found, None otherwise.
        """
        for cluster_group in self.cluster_groups_array:
            for cluster in cluster_group.get_clusters():
                if cluster['sid'] == sid:
                    return cluster_group
        return None
    
    def find_cluster_group_by_ip(self, ip):
        """
        Find a cluster group by IP address.

        :param ip: IP address of the cluster group to find.
        :return: Cluster group if found, None otherwise.
        """
        for cluster_group in self.cluster_groups_array:
            for cluster in cluster_group.get_clusters():
                if 'ip' in cluster and cluster['ip'] == ip:
                    return cluster_group
        return None
