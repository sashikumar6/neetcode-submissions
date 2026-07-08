class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq=defaultdict(list)
        ans=[]

        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            freq[tuple(count)].append(word)
        
        for word, freq in freq.items():

            ans.append(freq)

        return list(ans)
                
