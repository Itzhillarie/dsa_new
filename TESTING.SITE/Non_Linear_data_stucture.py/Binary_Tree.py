
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode("Q")
nodeW = TreeNode("W")
nodeE = TreeNode("E")
nodeR = TreeNode("R")
nodeT = TreeNode("T")
nodeY = TreeNode("Y")

root.left = nodeW
root.right = nodeE

nodeW.left = nodeT

nodeE.right = nodeR

nodeR.right = nodeY

print(root.left.data)
"""

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
"""
# Test
print("root.left.data:", root.left.data)