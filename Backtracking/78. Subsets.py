class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[]           
        res=[]

        self.helper(0, arr, res, nums)
        return res
    
    def helper(self, i,arr, res, nums):
        if i>=len(nums):
            answer=list(arr)
            res.append(answer)
            return res
        
        arr.append(nums[i])
        self.helper(i+1, arr, res, nums)
        arr.remove(nums[i])
        self.helper(i+1, arr, res, nums)


#Time & Space Complexity 
#Time complexity: O(nlogn) 
#Space complexity: O(n)        