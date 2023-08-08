from sys import stdin, setrecursionlimit
import queue



class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def isSymmetric(root):
    # If the root is null, then the binary tree is symmetric
    if not root:
        return True
     
    # Create a stack to store the left and right subtrees of the root
    stack = []
    stack.append(root.left)
    stack.append(root.right)
     
    # Continue the loop until the stack is empty
    while stack:
        # Pop the left and right subtrees from the stack
        node1 = stack.pop()
        node2 = stack.pop()
         
        # If both nodes are null, continue the loop
        if not node1 and not node2:
            continue
         
        # If one of the nodes is null, the binary tree is not symmetric
        if not node1 or not node2:
            return False
         
        # If the values of the nodes are not equal, the binary tree is not symmetric
        if node1.data != node2.data:
            return False
         
        # Push the left and right subtrees of the left and right nodes onto the stack in the opposite order
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
     
    # If the loop completes, the binary tree is symmetric
    return True
 
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

	

# Main
root = takeInput()
 
if isSymmetric(root):
    print("true")
else:
    print("false")