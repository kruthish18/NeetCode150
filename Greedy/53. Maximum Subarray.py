class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxSum=float("-inf")

        for i in range(len(nums)):

            if sum<0:
                sum=0

            sum += nums[i]
            maxSum= max(maxSum, sum)

        return maxSum        




#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(1)        