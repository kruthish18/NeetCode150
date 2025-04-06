class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for i in range(len(nums)):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                return False    

        return True


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(n)        