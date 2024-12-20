# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=[root]
        level=0
        
        while queue:
            size=len(queue)
            nodes=[]
            for i in range(size):
                node=queue.pop(0)
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            if   level%2==1:
                left,right=0,len(nodes)-1
                while right>left:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                    left+=1
                    right-=1
            level+=1

        return root
            