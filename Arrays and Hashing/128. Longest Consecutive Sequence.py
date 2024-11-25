class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        # print(numSet)
        max_length=0

        for num in nums:
            if num-1 not in numSet:
                length=0

                while num+length in numSet:
                    length+= 1
                    # print(length)
                max_length= max(max_length, length)    

        return max_length              



#Time & Space Complexity 
#Time complexity: O(nlogn) 
#Space complexity: O(n)        