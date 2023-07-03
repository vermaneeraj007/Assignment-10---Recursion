

            #Answer --------- 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max_subtree_sum(root):
    # Base case: if the root is None, return 0
    if root is None:
        return 0

    # Recursive calls to find the sum of left and right subtrees
    left_sum = find_max_subtree_sum(root.left)
    right_sum = find_max_subtree_sum(root.right)

    # Calculate the sum of the current subtree
    subtree_sum = left_sum + right_sum + root.data

    # Update the maximum sum if necessary
    if find_max_subtree_sum.max_sum < subtree_sum:
        find_max_subtree_sum.max_sum = subtree_sum

    # Return the sum of the current subtree
    return subtree_sum

# Main function to find the subtree with maximum sum
def find_maximum_subtree_sum(root):
    # Initialize the maximum sum to negative infinity
    find_max_subtree_sum.max_sum = float('-inf')

    # Call the recursive function to find the maximum sum
    find_max_subtree_sum(root)

    # Return the maximum sum
    return find_max_subtree_sum.max_sum

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Find the subtree with the maximum sum
max_sum = find_maximum_subtree_sum(root)

print("Maximum subtree sum:", max_sum)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max_subtree_sum(root):
    if root is None:
        return 0

    left_sum = find_max_subtree_sum(root.left)
    right_sum = find_max_subtree_sum(root.right)

    subtree_sum = left_sum + right_sum + root.data

    if find_max_subtree_sum.max_sum < subtree_sum:
        find_max_subtree_sum.max_sum = subtree_sum

    return subtree_sum

def find_maximum_subtree_sum(root):
    find_max_subtree_sum.max_sum = float('-inf')
    find_max_subtree_sum(root)
    return find_max_subtree_sum.max_sum

# Create the binary tree
root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(-6)
root.right.right = Node(2)

# Find the subtree with the maximum sum
max_sum = find_maximum_subtree_sum(root)

print("Maximum subtree sum:", max_sum)




            #Answer --------- 2


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_bst(level_order):
    if not level_order:
        return None

    root = Node(level_order[0])
    queue = [root]
    i = 1

    while queue and i < len(level_order):
        current = queue.pop(0)

        left_value = level_order[i]
        if left_value != -1:
            current.left = Node(left_value)
            queue.append(current.left)
        i += 1

        if i < len(level_order):
            right_value = level_order[i]
            if right_value != -1:
                current.right = Node(right_value)
                queue.append(current.right)
            i += 1

    return root

def inorder_traversal(root):
    if root is None:
        return []

    result = []
    result += inorder_traversal(root.left)
    result.append(root.data)
    result += inorder_traversal(root.right)

    return result

# Level order traversal of the BST
level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]

# Construct the BST
root = construct_bst(level_order)

# Print the inorder traversal of the constructed BST
inorder = inorder_traversal(root)
print("BST (inorder traversal):", inorder)



                #Answer --------- 3



def can_represent_bst_level_order(arr):
    n = len(arr)

    # Empty array or single element array is a valid BST
    if n == 0 or n == 1:
        return True

    # Find the index of the first element greater than the root
    i = 1
    while i < n and arr[i] < arr[0]:
        i += 1

    # Check if all elements after the root are greater
    j = i
    while j < n:
        if arr[j] < arr[0]:
            return False
        j += 1

    # Recursive calls to check left and right subtrees
    left_subtree = True
    if i > 1:
        left_subtree = can_represent_bst_level_order(arr[1:i])

    right_subtree = True
    if i < n:
        right_subtree = can_represent_bst_level_order(arr[i:])

    # Return True if both subtrees are valid BSTs
    return left_subtree and right_subtree

# Example 1
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
result1 = can_represent_bst_level_order(arr1)
print("Can represent BST (Example 1):", result1)

# Example 2
arr2 = [11, 6, 13, 5, 12, 10]
result2 = can_represent_bst_level_order(arr2)
print("Can represent BST (Example 2):", result2)








