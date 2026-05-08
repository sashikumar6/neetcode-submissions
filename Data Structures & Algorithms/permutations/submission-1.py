class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]

        for n in nums:
            temp=[]
            for p in perms:
                for i in range(len(p)+1):
                    p_copy=p[:]
                    p_copy.insert(i,n)

                    temp.append(p_copy)

            perms=temp

        return perms    
