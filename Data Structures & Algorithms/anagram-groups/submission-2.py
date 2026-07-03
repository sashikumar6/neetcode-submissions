class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)

        for i in strs:
            count=[0]*26
            for ch in i:
                count[ord(ch)-ord('a')]+=1
            freq[tuple(count)].append(i)
        ans=list((freq).values())
        return ans       