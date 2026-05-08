class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=k
        ans=0
        add=0

        while r<len(arr)+1:
            add=sum(arr[l:r])
            print(arr[l:r], "sum=",add, "avg=" ,add//k)

            if add//k >=threshold:
                ans+=1
            
            
            l+=1
            r+=1
        return ans