class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        white=0
        mini=float('inf')

        for r in range(len(blocks)):
            if blocks[r]=='W':
                white+=1

            while r-l+1>k:
                if blocks[l]=='W':
                    white-=1
                l+=1

            if r-l+1==k:
                mini=min(mini,white)

        return mini


#we calculate how many white we saw until now
#if window size exceeds, if the oldest element(l) is white we can remove that and extend
#if we find a solution, save it look for better solution