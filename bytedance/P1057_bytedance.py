class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dists = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
                dists.append((dist,j,i))             
        bikes_used = set()
        res = [-1]*len(workers)
        for dist, bike, worker in sorted(dists):
            if (bike not in bikes_used) and (res[worker]==-1):
                res[worker] = bike
                bikes_used.add(bike)
        return res