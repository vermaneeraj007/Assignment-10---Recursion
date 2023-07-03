



            #Answer --------- 1



class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def convert_bt_to_dll(root):
    if root is None:
        return None

    # Convert the left subtree
    if root.left:
        left_dll = convert_bt_to_dll(root.left)

        # Find the rightmost node of the left subtree
        while left_dll.right:
            left_dll = left_dll.right

        # Connect the rightmost node to the current node
        left_dll.right = root
        root.left = left_dll

    # Convert the right subtree
    if root.right:
        right_dll = convert_bt_to_dll(root.right)

        # Find the leftmost node of the right subtree
        while right_dll.left:
            right_dll = right_dll.left

        # Connect the leftmost node to the current node
        right_dll.left = root
        root.right = right_dll

    return root

# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

# Convert the binary tree to a DLL
head = convert_bt_to_dll(root)

# Print the DLL in inorder traversal order
def print_dll_inorder(head):
    if head is None:
        return

    current = head

    while current.left:
        current = current.left

    while current:
        print(current.val, end=" ")
        prev = current
        current = current.right

    print()

print("Output:")
print_dll_inorder(head)





            #Answer --------- 2




class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def flip_binary_tree(root):
    if root is None:
        return None

    # Base case: If the node is a leaf, return the node itself
    if root.left is None and root.right is None:
        return root

    # Recursively flip the left and right subtrees
    flipped_left = flip_binary_tree(root.left)
    flipped_right = flip_binary_tree(root.right)

    # Swap the left and right child nodes
    root.left = flipped_right
    root.right = flipped_left

    return root

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Flip the binary tree towards the right direction
flipped_root = flip_binary_tree(root)

# Print the flipped binary tree
def print_binary_tree(root):
    if root is None:
        return

    print(root.val, end=" ")
    print_binary_tree(root.left)
    print_binary_tree(root.right)

print("Output:")
print_binary_tree(flipped_root)





                #Answer --------- 3




class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def print_root_to_leaf_paths(root):
    if root is None:
        return

    # Create a stack to store nodes and their paths
    stack = [(root, str(root.val))]

    while stack:
        current_node, path = stack.pop()

        # If the current node is a leaf, print the path
        if current_node.left is None and current_node.right is None:
            print(path)

        # Push the right child to the stack
        if current_node.right:
            stack.append((current_node.right, path + "->" + str(current_node.right.val)))

        # Push the left child to the stack
        if current_node.left:
            stack.append((current_node.left, path + "->" + str(current_node.left.val)))

# Create the binary tree
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Print all root-to-leaf paths
print("Output:")
print_root_to_leaf_paths(root)



                #Answer -------- 4



def check_traversal_equality(inorder, preorder, postorder):
    # Base cases: If any of the traversals is empty, return True
    if len(inorder) == 0 or len(preorder) == 0 or len(postorder) == 0:
        return True

    # Base case: If the number of nodes in the traversals is different, return False
    if len(inorder) != len(preorder) or len(inorder) != len(postorder):
        return False

    # Base case: If there is only one node, return True
    if len(inorder) == 1 and len(preorder) == 1 and len(postorder) == 1:
        return inorder[0] == preorder[0] and inorder[0] == postorder[0]

    # Check if the first element of preorder and last element of postorder are the same
    if preorder[0] != postorder[-1]:
        return False

    # Find the root element in the inorder traversal
    root = inorder.index(preorder[0])

    # Recursively check the left and right subtrees
    left_inorder = inorder[:root]
    right_inorder = inorder[root + 1:]

    left_preorder = preorder[1:root + 1]
    right_preorder = preorder[root + 1:]

    left_postorder = postorder[:root]
    right_postorder = postorder[root:-1]

    # Return True if the traversals for both subtrees are equal
    return check_traversal_equality(left_inorder, left_preorder, left_postorder) and \
           check_traversal_equality(right_inorder, right_preorder, right_postorder)

# Test case 1
inorder1 = [4, 2, 5, 1, 3]
preorder1 = [1, 2, 4, 5, 3]
postorder1 = [4, 5, 2, 3, 1]
print("Output 1:", check_traversal_equality(inorder1, preorder1, postorder1))  # Output: True

# Test case 2
inorder2 = [4, 2, 5, 1, 3]
preorder2 = [1, 5, 4, 2, 3]
postorder2 = [4, 1, 2, 3, 5]
print("Output 2:", check_traversal_equality(inorder2, preorder2, postorder2))  # Output: False
