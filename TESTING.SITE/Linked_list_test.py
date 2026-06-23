class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

def traverse_linkedlist(head):
   currentNode = head
   while currentNode:
      print(currentNode.data, end="->")
      currentNode = currentNode.next
   print("None")
node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

traverse_linkedlist(node1)

"""
git merge works locally while gh(GITHUB CLI)
GIT MERGE:(main..active banch name)
git checkout main
git pull origin main
git checkout <in active branch name>
git push origin main


GIT REBASE:

"""