class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num=0
        for i in digits:
            num=num*10+i
        res=num+1

        ans=[]
        for i in str(res):
            ans.append(int(i))

        return ans
    