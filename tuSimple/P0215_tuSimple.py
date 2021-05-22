class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        t = []
        for n in nums:
            heapq.heappush(t, -n)        
        for _ in range(k):
            res = heapq.heappop(t)        
        return(-res)