



            #Answer ---------- 1





class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root, values):
    if root is None:
        return

    inorder_traversal(root.left, values)
    values.append(root.val)
    inorder_traversal(root.right, values)

def construct_bst_from_sorted(values):
    if not values:
        return None

    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = construct_bst_from_sorted(values[:mid])
    root.right = construct_bst_from_sorted(values[mid+1:])

    return root

def convert_binary_tree_to_bst(root):
    # Perform inorder traversal to obtain sorted values
    values = []
    inorder_traversal(root, values)

    # Construct a new binary search tree from the sorted values
    new_root = construct_bst_from_sorted(values)

    return new_root

# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

# Convert the binary tree to a binary search tree
new_root = convert_binary_tree_to_bst(root)

# Output the binary search tree using inorder traversal
def inorder_print(root):
    if root is None:
        return

    inorder_print(root.left)
    print(root.val, end=" ")
    inorder_print(root.right)

print("Output (inorder traversal):")
inorder_print(new_root)




                #Answer ----------- 2


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None

    if root.val > node1 and root.val > node2:
        return find_lca(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return find_lca(root.right, node1, node2)
    else:
        return root

def find_distance(root, node, distance):
    if root is None:
        return -1

    if root.val == node:
        return distance

    left_distance = find_distance(root.left, node, distance + 1)
    if left_distance != -1:
        return left_distance

    right_distance = find_distance(root.right, node, distance + 1)
    if right_distance != -1:
        return right_distance

    return -1

def find_node_distance(root, node1, node2):
    lca = find_lca(root, node1, node2)

    distance1 = find_distance(lca, node1, 0)
    distance2 = find_distance(lca, node2, 0)

    return distance1 + distance2

# Create the binary search tree
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

# Example 1
node1_1 = 6
node2_1 = 14
distance1 = find_node_distance(root, node1_1, node2_1)
print("The distance between the two keys (Example 1):", distance1)

# Example 2
node1_2 = 3
node2_2 = 4
distance2 = find_node_distance(root, node1_2, node2_2)
print("The distance between the two keys (Example 2):", distance2)




                    #Answer ---------- 3



class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

def convert_binary_tree_to_dll(root):
    if root is None:
        return None

    # Create a dummy node to represent the head of the doubly linked list
    dummy = DoublyLinkedListNode(0)
    prev = dummy

    # Perform in-order traversal
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        # Create a new doubly linked list node
        new_node = DoublyLinkedListNode(current.val)
        prev.next = new_node
        new_node.prev = prev
        prev = new_node

        current = current.right

    # Adjust the pointers to form a circular doubly linked list
    head = dummy.next
    head.prev = None
    prev.next = None

    return head

# Create the binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Convert the binary tree to a doubly linked list
head = convert_binary_tree_to_dll(root)

# Print the doubly linked list
def print_dll(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next

print("Output:")
print_dll(head)





                #Answer ---------- 4



class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

def connect_nodes_at_same_level(root):
    if root is None:
        return root

    # Perform level order traversal using a queue
    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.pop(0)

            # Connect the current node to the next node in the same level
            if i < level_size - 1:
                current_node.next = queue[0]

            # Enqueue the left and right child nodes
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return root

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect nodes at the same level
connected_root = connect_nodes_at_same_level(root)

# Print the connections
def print_connections(root):
    current = root
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

print("Output:")
print_connections(root.left.left)   # 4 -> 5
print_connections(root.left)        # 2 -> 3
print_connections(root.right.left)  # 6 -> 7
print_connections(root.right)       # 3 -> -1
print_connections(root.left.right)  # 5 -> 6
print_connections(root.right.right) # 7 -> -1




