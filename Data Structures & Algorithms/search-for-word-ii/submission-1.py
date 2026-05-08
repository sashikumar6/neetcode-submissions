class TrieNode():
    def __init__(self):
        self.children={}
        self.endofWord=False

    def addWord(self,word):
        cur=self

        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.endofWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            root.addWord(word)

        ROW = len(board)
        COL = len(board[0])
        res,visit=set(),set()

        def dfs(r,c,node,word):
            if (r < 0 or r >= ROW or c < 0 or c >= COL or
                board[r][c] not in node.children or
                (r,c) in visit):
                return 
            
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]

            if node.endofWord:
                res.add(word)

            dfs(r+1,c,node,word) 
            dfs(r-1,c,node,word) 
            dfs(r,c+1,node,word) 
            dfs(r,c-1,node,word)

            visit.remove((r,c))
        
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,root,"")
        
        return list(res)










