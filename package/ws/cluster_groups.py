class ClusterGroups:
    """
    Class to manage cluster groups.
    """
    def __init__(self, name):
        """
        Initialize the ClusterGroups object.

        :param name: Name of the cluster group.
        """
        self.name = name
        self.cluster_groups = []

    def get_clusters(self):
        """
        Get the list of cluster groups.

        :return: List of cluster groups.
        """
        return self.cluster_groups
    
    def add_cluster(self, cluster_group):
        """
        Add a new cluster.

        :param cluster_group: Cluster to add.
        """
        self.cluster_groups.append(cluster_group)

    def remove_cluster_group(self, cluster_group):
        """
        Remove a cluster group.

        :param cluster_group: Cluster group to remove.
        """
        self.cluster_groups.remove(cluster_group)

    def remove_cluster_by_sid(self, sid):
        """
        Remove a cluster group by session ID.

        :param sid: Socket ID of the cluster to remove.
        """
        for cluster in self.cluster_groups:
            if cluster['sid'] == sid:
                self.cluster_groups.remove(cluster)
                break

    def find_cluster_by_ip(self, ip):
        """
        Find a cluster group by IP address.

        :param ip: IP address of the cluster to find.
        :return: Cluster group if found, None otherwise.
        """
        for cluster in self.cluster_groups:
            if 'ip' in cluster and cluster['ip'] == ip:
                return cluster
        return None
    
    def find_client(self):
        """
        Find a client in the cluster group.

        :return: Client if found, None otherwise.
        """
        for cluster in self.cluster_groups:
            if not 'ip' in cluster:
                return cluster
        return None