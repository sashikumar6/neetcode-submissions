class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        #find peak
        n=mountainArr.length()
        l=1
        r=n-2 # peak can't be in 0 or n

        while l<=r:
            m=(l+r)//2
            left,mid,right=mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)

            if left<mid<right: #we are in left sorted portion, peak can't be here
                l=m+1
            elif left>mid>right: #we are in right sorted portion
                r=m-1
            else:
                break
        
        peak=m

#look in left sorted portion
        l=0
        r=peak
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            
            if val > target:
                r=m-1
            elif val < target:
                l=m+1
            else:
                return m

#look in right sorted portion
        l=peak
        r=n-1
        while l<=r:
            m=(l+r)//2
            val=mountainArr.get(m)
            if val < target:
                r=m-1
            elif val > target:
                l=m+1
            else:
                return m
    
        return -1
        

                