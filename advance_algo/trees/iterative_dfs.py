# https://www.enjoyalgorithms.com/blog/iterative-binary-tree-traversals-using-stack

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def inorder(curr):

    """
    every node will be in the stack where the priority follows left to right
    left -> middle -> right

    """
    stack = []

    while True:

        if curr is None and len(stack)==0:
            return 

        if curr:
            stack.append(curr) 
            #next step
            curr = curr.left

        else:
            curr = stack.pop()
            print(curr.val)
            #next step
            curr = curr.right
            
def preorder(curr):

    """
    only right node will be in the stack where the priority follows the nearest curr right node
    middle -> left -> right

    """
    stack = []

    while True:

        if curr is None and len(stack)==0:
            return 

        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right) 

            #next step
            curr = curr.left

        else:
            curr = stack.pop()


def postorder(curr):

    """
    all node will be in the stack but there need to be an additional visit stack
    left -> right -> middle

    """
    stack = [[curr,False]]

    while True:

        if not stack:
            return 
        
        curr, visited = stack.pop()

        # if curr is None,we dont print and we do not go any further
        if curr:
            if visited:
                print(curr.val)

            else:
                stack.append([curr,True])
                stack.append([curr.right,False])
                stack.append([curr.left,False])
if __name__=="__main__":
    
    root = TreeNode(1,None,None)
    root.left = TreeNode(2,None,None)
    root.right = TreeNode(3,None,None)
    root.left.left  = TreeNode(4,None,None)
    root.right.right = TreeNode(5,None,None)
    print('inorder')
    inorder(root) #42135
    print('preorder') #12435
    preorder(root)
    print('postorder') #12435
    postorder(root) #42531

# def postorder(curr):

#     """
#     all node will be in the stack but there need to be an additional visit stack
#     left -> right -> middle

#     """
#     stack = [curr]
#     visit = [False]

#     while True:

#         if not stack:
#             return 
        
#         curr, visited = stack.pop(), visit.pop()

#         if curr:
#             if visited:
#                 print(curr.val)

#             else:
#                 stack.append(curr)
#                 visit.append(True)
#                 stack.append(curr.right)
#                 visit.append(False)
#                 stack.append(curr.left)
#                 visit.append(False)
            