from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        use iterative:
        what i remember : postorder process when it pop up twice
        create a stack e.g [root,is_visited=False]
        1. pop up
        2. if curr is None, we continue
        3. if curr, if is visited: print
        4. if curr, not visited: push to the stack where the curr is True , curr.left and curr.right is False
        """

        traversal = []

        if root is None:
            return []
        
        stack = [[root,False]]

        while True:

            if not stack:
                return traversal
            else:
                curr, visited = stack.pop()

                if not curr:
                    continue
                else:
                    if visited:
                        traversal.append(curr.val)
                    else:
                        stack.append([curr,True])
                        stack.append([curr.right,False])
                        stack.append([curr.left,False])





# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         use recursive:
#         since it is backtracking 
#         the end case: if root == None
#         the purpose: change root to its left and right child and its output is the traversal already done
#         """
#         self.traversal = []
#         self.helper(root)
#         return self.traversal

#     def helper(self,curr):
#         if curr == None:
#             return

#         self.helper(curr.left)
#         self.helper(curr.right)
#         self.traversal.append(curr.val)





if __name__=='__main__':
    s= Solution()
    root = TreeNode(1)
    root.right=TreeNode(2)
    root.right.left = TreeNode(3)
    print(s.postorderTraversal(root)) #[3,2,1]
    print('############################')
    root = TreeNode(val=None)
    print(s.postorderTraversal(root)) #[]
    print('############################')
    root = TreeNode(1)
    print(s.postorderTraversal(root)) #[1]
    print('############################')