class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        top=0
        bot=row-1

        while(top<=bot):
            row=(top+bot)//2
            if matrix[row][0] > target:
                bot=row-1
            elif matrix[row][-1] < target:
                top=row+1
            else:
                break
            
        if not (top<=bot):
            return False

        low=0
        high=col-1
        row=(top+bot)//2
        while (low<=high):
            mid=(low+high)//2
            if target<matrix[row][mid]:
                high=mid-1
            elif target>matrix[row][mid]:
                low=mid+1
            else:
                return True
        return False