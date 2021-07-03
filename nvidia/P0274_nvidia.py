class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n+1)
        for c in citations:
            if c > n:
                buckets[n] += 1
            else:
                buckets[c] += 1        
        pre = 0
        for i, b in enumerate(buckets[::-1]):
            pre += b
            if pre >= n-i:
                return n-i            
        return n
                