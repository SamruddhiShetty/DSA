  #this can be done on right side only as well
  #time complexity is O(n) since i go through all the nodes
  #space complexity is 0
  
  class Node:
    def __init__(self, data):
      self.data=data
      self.left=None
      self.right=None
  
  class Tree:
    maxLevel=0

    # def printTree(self, root):
    #   print(root.data)
    #   selfPrintTree(sekl)

    def leftView(self, root, level):
      if not root:
        return
      if (self.maxLevel<level):
        print(root.data, end=" ")
        self.maxLevel=level
      self.leftView(root.left, level+1)
      self.leftView(root.right, level+1)
  
  
  
  if __name__=="__main__":
    obj=Tree()
    #the tree 
    """
              1
          2       3
      4      5 6     7

      expected answer is 1, 2, 4


               1
          2        3
                      7
    """
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    # root.right.left=Node(6)
    root.right.right=Node(7)
    obj.leftView(root, 1)



