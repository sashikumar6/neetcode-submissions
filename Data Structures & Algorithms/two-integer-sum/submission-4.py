class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        left=0
        right=len(nums)-1

        sortednums=[(val,i) for i,val in enumerate(nums)]
        sortednums.sort(key=lambda x:x[0])

        ans=[]
        while(left<right):
            if sortednums[left][0]+sortednums[right][0]>target:
                right-=1
            elif sortednums[left][0]+sortednums[right][0]<target:
                left+=1
            elif sortednums[left][0]+sortednums[right][0] ==target and left != right:
                ans.append(sortednums[left][1])
                ans.append(sortednums[right][1])
                break
        ans.sort()
        return ans
    