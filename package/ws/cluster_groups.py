class ClusterGroups:
    """
    Class to manage cluster groups.
    """
    def __init__(self, name):
        """
        Initialize the ClusterGroups object.

        :param cluster_groups: List of cluster groups.
        """
        self.name = name
        self.cluster_groups = []

    def get_cluster_groups(self):
        """
        Get the list of cluster groups.

        :return: List of cluster groups.
        """
        return self.cluster_groups
    
    def add_cluster_group(self, cluster_group):
        """
        Add a new cluster group.

        :param cluster_group: Cluster group to add.
        """
        self.cluster_groups.append(cluster_group)

    def remove_cluster_group(self, cluster_group):
        """
        Remove a cluster group.

        :param cluster_group: Cluster group to remove.
        """
        self.cluster_groups.remove(cluster_group)

    def remove_cluster_group_by_sid(self, sid):
        """
        Remove a cluster group by session ID.

        :param sid: Session ID of the cluster group to remove.
        """
        for cluster in self.cluster_groups:
            if cluster['sid'] == sid:
                self.cluster_groups.remove(cluster)
                break