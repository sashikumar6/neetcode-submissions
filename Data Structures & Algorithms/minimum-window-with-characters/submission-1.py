class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        window={}

        for i in t:
            countT[i]=1+countT.get(i,0)
        
        have=0
        need=len(countT)
        res=[-1,-1]
        resLength=float('infinity')

        l=0
        for r in range(len(s)):
            i=s[r]
            window[i]=1+window.get(i,0)

            if i in countT and window[i]==countT[i]:
                have+=1
            
            while have==need:
                if (r-l+1) < resLength:
                    res=[l,r]
                    resLength=(r-l+1)

                window[s[l]]-=1    
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        
        l,r=res
        return s[l:r+1] if resLength != float('infinity') else ""              