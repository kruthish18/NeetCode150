class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        l=0
        r=1

        while r<len(prices):
            if prices[l]<prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l=r
            r=r+1    
            
        return maxP
        


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(1) 