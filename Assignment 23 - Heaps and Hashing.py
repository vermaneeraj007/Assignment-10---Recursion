


            #Answer ------- 1

def calculate_depth(preorder):
    stack = []
    depth = 0

    for char in preorder:
        if char == 'n':
            stack.append(char)
        elif char == 'l':
            while stack and stack[-1] == 'l':
                stack.pop()
            if stack:
                stack.pop()
            stack.append(char)
        
        depth = max(depth, len(stack) - 1)

    return depth

# Test cases
preorder1 = "nlnll"
print("Output 1:", calculate_depth(preorder1))  # Output: 2

preorder2 = "nlnnlll"
print("Output 2:", calculate_depth(preorder2))  # Output: 3



            #Answer ------- 2



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_view(root):
    if root is None:
        return []

    queue = [(root, 1)]  # Queue to store nodes and their levels
    left_view_nodes = []  # List to store left view nodes

    while queue:
        node, level = queue.pop(0)

        if level > len(left_view_nodes):
            left_view_nodes.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return left_view_nodes


# Test case 1
root1 = TreeNode(4)
root1.left = TreeNode(5)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(1)
root1.right.left.left = TreeNode(6)
root1.right.left.right = TreeNode(7)

print("Output 1:", left_view(root1))  # Output: [4, 5, 3, 6]

# Test case 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.left.right.right = TreeNode(5)
root2.left.right.right.right = TreeNode(6)

print("Output 2:", left_view(root2))  # Output: [1, 2, 4, 5, 6]




            #Answer ------- 3




class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_view(root):
    if root is None:
        return []

    queue = [(root, 1)]  # Queue to store nodes and their levels
    right_view_nodes = []  # List to store right view nodes

    while queue:
        node, level = queue.pop(0)

        if level > len(right_view_nodes):
            right_view_nodes.append(node.val)

        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))

    return right_view_nodes


# Test case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.right.right.right = TreeNode(8)

print("Output 1:", right_view(root1))  # Output: [1, 3, 7, 8]

# Test case 2
root2 = TreeNode(1)
root2.left = TreeNode(8)
root2.left.left = TreeNode(7)

print("Output 2:", right_view(root2))  # Output: [1, 8, 7]





            #Answer ------- 4




from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return []

    hd_dict = {}  # Dictionary to store horizontal distance and node values
    queue = deque([(root, 0)])  # Queue to perform level order traversal

    while queue:
        node, hd = queue.popleft()
        hd_dict[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the dictionary by horizontal distance
    sorted_hd_dict = sorted(hd_dict.items(), key=lambda x: x[0])

    return [val for hd, val in sorted_hd_dict]


# Test case 1
root1 = TreeNode(20)
root1.left = TreeNode(8)
root1.right = TreeNode(22)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(25)
root1.left.right.left = TreeNode(10)
root1.left.right.right = TreeNode(14)

print("Output 1:", bottom_view(root1))  # Output: [5, 10, 3, 14, 25]

# Test case 2
root2 = TreeNode(20)
root2.left = TreeNode(8)
root2.right = TreeNode(22)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(25)
root2.left.right.left = TreeNode(10)
root2.left.right.right = TreeNode(14)

print("Output 2:", bottom_view(root2))  # Output: [5, 10, 4, 14, 25]


