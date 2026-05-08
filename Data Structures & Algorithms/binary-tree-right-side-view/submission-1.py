# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        
        q=collections.deque([root])

        while q:
            rightside=None
            for _ in range(len(q)):
                root=q.popleft()
                rightside=root

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            if rightside:
                res.append(rightside.val)
        return res



        