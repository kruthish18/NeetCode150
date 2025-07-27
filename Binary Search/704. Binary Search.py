class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l=0
        r= len(nums)

        while (l<=r):
            mid = (r-l)/2 + l
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1

        return False            