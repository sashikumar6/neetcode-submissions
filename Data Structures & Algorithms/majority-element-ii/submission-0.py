class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1=defaultdict(int)

        for i in nums:
            counter1[i]+=1

            if len(counter1)<=2:
                continue
            new_count=defaultdict(int)
            for item,count in counter1.items():
                if count>1:
                    new_count[item]=count-1
            counter1=new_count

        res=[]

        for i in counter1:
            if nums.count(i) > len(nums)//3:
                res.append(i)
        
        return res
            

                
