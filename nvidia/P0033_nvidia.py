class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1        
        while lo <= hi:   
            if target == nums[lo]: return lo
            if target == nums[hi]: return hi                   
            mid = (lo+hi)//2            
            if target == nums[mid]: return mid
            if nums[lo] <= nums[mid] <= nums[hi]:
                if target < nums[mid]: hi = mid - 1
                else: lo = mid + 1
            elif nums[hi] <= nums[lo] <= nums[mid]:
                if nums[lo] < target < nums[mid]: hi = mid - 1
                else: lo = mid + 1                
            elif nums[mid] <= nums[hi] <= nums[lo]:
                if nums[mid] < target < nums[hi]: lo = mid + 1
                else: hi = mid - 1               
        return -1