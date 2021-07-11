  #prints the outer line of the tree(border) we can do the same where we only want the upper two sides of the boder that is here we include all three sides of the triangle
  #but if we want to exclude the bottom edge we simply should not include the leaf node
  #time complexity here is O(n)
  #space compplexity is O(n)
  
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

    def leftView(self, root, level, result):
      if not root:
        return
      if (self.maxLevel<level):
        result.append(root.data)
        self.maxLevel=level
      if (root.left==None and root.right==None) and root.data not in result:
        result.append(root.data)
      self.leftView(root.left, level+1, result)
      self.leftView(root.right, level+1, result)

    def rightView(self, root, level, result):
      if not root:
        return
      if (self.maxLevel<level):
        if root.data not in result:
          result.append(root.data)
        self.maxLevel=level
      self.rightView(root.right, level+1, result)
      self.rightView(root.left, level+1, result)
  
  
  
  if __name__=="__main__":
    obj=Tree()
    result=[]
    #the tree 
    """
              1
          2         3
      4      5    6     7
    11         9 10       12
            13 
      expected answer is 12 10 13 11 4 2 1 3 7


               1
          2        3
                      7

      expected answer is 2 1 3 7
    """
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.left.left=Node(11)
    root.left.right=Node(5)
    root.left.right.right=Node(9)
    root.left.right.right.right=Node(13)
    root.right.left=Node(6)
    root.right.left.left=Node(10)
    root.right.right=Node(7)
    root.right.right.right=Node(12)
    obj.leftView(root, 1, result)
    result.reverse()
    obj.maxLevel=1
    obj.rightView(root.right, 2, result)
    print(result)



