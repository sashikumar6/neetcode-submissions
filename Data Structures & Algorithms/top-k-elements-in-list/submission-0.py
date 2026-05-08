class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count=Counter(nums)
        common=count.most_common(k)

        for key,value in common:
            ans.append(key)

        return ans    