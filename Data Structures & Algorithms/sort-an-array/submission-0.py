class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums,left,right):
            if left >=right:
                return
            
            i=left
            j=right

            pivot=nums[(left+right)//2]

            while i<=j:
                while nums[i]<pivot:
                    i+=1
                while nums[j]>pivot:
                    j-=1
                
                if i<=j:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1

            quicksort(nums,left,j)
            quicksort(nums,i,right)

        quicksort(nums,0,len(nums)-1)
        return nums