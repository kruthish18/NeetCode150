class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in myDict:
                myDict[nums[i]] = i
            else:
                return [myDict[diff] , i]


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(n)        