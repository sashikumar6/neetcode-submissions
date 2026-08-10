class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sfreq=defaultdict(int)
        Tfreq=defaultdict(int)

        for i in s:
            Sfreq[i]+=1
        for i in t:
            Tfreq[i]+=1

        if Sfreq==Tfreq:
            return True
        else:
            return False