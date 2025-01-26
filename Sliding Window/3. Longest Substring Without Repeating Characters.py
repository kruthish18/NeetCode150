class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        start=0
        count=0

        for i in range(len(s)):
            while s[i] in seen:    
                start+=1
                seen.remove(s[i])    

            seen.add(s[i])
            count = max(count, len(seen))


        return count        
        

#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(1) 