# https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/
# https://github.com/alldaygzchen/mycode/blob/main/trees/exercise/257_e_binaryTreePaths.py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isLeafPath(root, path,record):
    #  output: whether the root to leaf has path
    #  backtracking because it will trace back if meet zero
    #  since path is global, it read the global path first (delete)
    #  check the root head before recurion   
    
    # current path starts with 0 and null
    if not root or root.val == 0:
        return False
    

    ################################################################
    
    # no path to continue => which is leaf node
    if not root.left and not root.right:
        path.append(root.val)
        record.extend(path)
        return True
    
    # still has path to continue 
    path.append(root.val)
    if isLeafPath(root.left, path.copy(),record):
        return True
    if isLeafPath(root.right, path.copy(),record):
        return True
    # path.pop()
    return False


def helper(root, path, paths):
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print('path',path)
    # print('paths',paths)
    if not root or root.val==0:
        return
    # print('current root',root.val)
    # print('current root',root.val)
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


    if root.left is None and root.right is None:
        path.append(root.val)
        paths.append(path)
        return
    
    elif root.left is None:
        path.append(root.val)
        helper(root.right, path.copy(), paths)
    elif root.right is None:
        path.append(root.val)
        helper(root.left, path.copy(), paths)
    else:
        path.append(root.val)
        helper(root.left, path.copy(), paths)
        helper(root.right, path.copy(), paths)


def allLeafPath(root):

    paths = []

    if not root:
        return [[]]


    helper(root,[],paths)
    return paths
 
def printArray(paths):
    print('answer',paths)
    # for path in paths:
    #     for i in path:
    #         print(i, " ", end="")
    #     print()

############################################################### wrong
def isLeafPath2(root, path):

    if not root or root.val == 0:
        return False
    

    ################################################################
    
    # no path to continue => which is leaf node
    if not root.left and not root.right:
        path.append(root.val)
        return True
    
    # still has path to continue 
    path.append(root.val)
    if isLeafPath2(root.left, path.copy()):
        return True
    if isLeafPath2(root.right, path.copy()):
        return True
    # path.pop()
    print('path',path)
    return False

if __name__=="__main__":
    # root = TreeNode(10)
    # root.left = TreeNode(8)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(2)
    root = TreeNode(4)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(3)
    root.right.left.right = TreeNode(4)
    root.right.right = TreeNode(0)
    ###############################
    paths = allLeafPath(root)
    printArray(paths)
    ################################
    the_leaf_path = []
    print(isLeafPath(root,[],the_leaf_path))
    print('answer',the_leaf_path)
    ################################
    the_leaf_path = []
    print(isLeafPath2(root,the_leaf_path))
    print('answer',the_leaf_path)