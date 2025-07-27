class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[] 

        for i, temp in enumerate(temperatures):
            while stack and temp[i]>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i-stackInd

            stack.append([temp, i])        


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(n)        