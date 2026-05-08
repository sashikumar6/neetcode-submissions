class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        ans=0
        add=0

        for r in range(len(arr)):
            add+=arr[r]

            if r-l+1>k:
                add-=arr[l]
                l+=1

            if  r - l + 1 == k and add//k >=threshold:
                ans+=1
            
            
            
        return ans