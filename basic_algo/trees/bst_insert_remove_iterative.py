
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class GFG:
    @staticmethod
    def main(args):
        tree = BST()
        tree.insert(30)
        tree.insert(50)
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.inorder()

class BST:
    root =None

    def insert(self,key):

        node = TreeNode(key)
        # if self.root ==None:
        #     self.root = node
        #     return
        self.helper_insert(self.root,None,node)
        return

    def helper_insert(self,temp,prev,node):
        # compare https://www.geeksforgeeks.org/insertion-in-binary-search-tree/
        # it is just a while loop


        if self.root==None:
            self.root = node
            return

        if (temp== None):
            if prev.val>node.val:
                prev.left =node
            elif prev.val<node.val:
                prev.right =node
            return
        
        if (temp.val>node.val):
            prev = temp
            self.helper_insert(temp.left,prev,node)
        elif (temp.val<node.val):
            prev =temp
            self.helper_insert(temp.right,prev,node)

    def inorder(self):
        temp = self.root
        stack = []
        while (temp != None or not (len(stack) == 0)):
            if (temp != None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.val) + " ", end="")
                temp = temp.right

if __name__ == "__main__":
    GFG.main([])



"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class GFG:
    @staticmethod
    def main(args):
        tree = BST()
        tree.insert(30)
        tree.insert(50)
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.inorder()

class BST:
    root =None

    def insert(self,key):

        node = TreeNode(key)
        if self.root ==None:
            self.root = node
            return
        self.helper_insert(self.root,None,node)
        return

    def helper_insert(self,temp,prev,node):
        # compare https://www.geeksforgeeks.org/insertion-in-binary-search-tree/
        # it is just a while loop
        if (temp== None):
            if prev.val>node.val:
                prev.left =node
            elif prev.val<node.val:
                prev.right =node
            return
        
        if (temp.val>node.val):
            prev = temp
            self.helper_insert(temp.left,prev,node)
        elif (temp.val<node.val):
            prev =temp
            self.helper_insert(temp.right,prev,node)

    def inorder(self):
        temp = self.root
        stack = []
        while (temp != None or not (len(stack) == 0)):
            if (temp != None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.val) + " ", end="")
                temp = temp.right

if __name__ == "__main__":
    GFG.main([])
"""