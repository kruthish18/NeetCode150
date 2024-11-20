class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m=len(matrix)
        n=len(matrix[0])

        low=0
        high= (m*n)-1

        while low<=high:

            mid = (high-low)//2 + low
            mid_element = matrix[mid//n][mid%n]

            if mid_element<target:
                low=mid+1
            elif mid_element>target:
                high=mid-1
            elif mid_element==target:
                return True

        return False