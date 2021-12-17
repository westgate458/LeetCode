class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """        
        self.vals = [0]*length
        self.snaps_ids = [[-1] for _ in range(length)]
        self.snaps_val = [[0] for _ in range(length)]
        self.snap_id = -1
        self.changed = set()

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.vals[index]!=val:
            self.vals[index] = val     
            self.changed.add(index)

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1        
        if self.changed:
            for i in list(self.changed):
                self.snaps_ids[i].append(self.snap_id)
                self.snaps_val[i].append(self.vals[i])
            self.changed = set()        
        return self.snap_id
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """               
        return self.snaps_val[index][bisect.bisect_right(self.snaps_ids[index],snap_id)-1]  
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)