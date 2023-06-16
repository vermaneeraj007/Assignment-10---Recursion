





                      #Answer --------- 1

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def create_new_linked_list(list1, list2):
    # Create a dummy node for the new list
    dummy = Node()
    newList = dummy

    # Traverse the linked lists
    while list1 is not None and list2 is not None:
        # Compare the values of nodes
        if list1.value >= list2.value:
            # Add the greater value node to the new list
            newList.next = Node(list1.value)
            list1 = list1.next
        else:
            newList.next = Node(list2.value)
            list2 = list2.next

        newList = newList.next

    # Add the remaining nodes from list1 or list2, if any
    if list1 is not None:
        newList.next = list1
    if list2 is not None:
        newList.next = list2

    # Exclude the dummy node and return the new list
    return dummy.next
# Example 1
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

newList = create_new_linked_list(list1, list2)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 5 7 4 8

# Example 2
list1 = Node(2)
list1.next = Node(8)
list1.next.next = Node(9)
list1.next.next.next = Node(3)

list2 = Node(5)
list2.next = Node(3)
list2.next.next = Node(6)
list2.next.next.next = Node(4)

newList = create_new_linked_list(list1, list2)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 5 8 9 4





                      #Answer --------- 2




class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    current = head
    while current.next is not None:
        if current.value == current.next.value:
            # Skip all duplicate nodes
            next_distinct = current.next.next
            while next_distinct is not None and next_distinct.value == current.value:
                next_distinct = next_distinct.next
            current.next = next_distinct
        else:
            current = current.next

    return head
# Example
list1 = Node(11)
list1.next = Node(11)
list1.next.next = Node(11)
list1.next.next.next = Node(21)
list1.next.next.next.next = Node(43)
list1.next.next.next.next.next = Node(43)
list1.next.next.next.next.next.next = Node(60)

newList = remove_duplicates(list1)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 11 21 43 60





                      #Answer --------- 3



class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def reverse_k_nodes(head, k):
    if head is None:
        return None

    prev = None
    curr = head
    next_node = None
    count = 0

    # Reverse k nodes
    while curr is not None and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    # Recursively reverse the remaining nodes
    if next_node is not None:
        head.next = reverse_k_nodes(next_node, k)

    return prev
# Example
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(2)
list1.next.next.next = Node(4)
list1.next.next.next.next = Node(5)
list1.next.next.next.next.next = Node(6)
list1.next.next.next.next.next.next = Node(7)
list1.next.next.next.next.next.next.next = Node(8)

k = 4

newList = reverse_k_nodes(list1, k)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 4 2 2 1 8 7 6 5






                      #Answer --------- 4


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def reverse_alternate_k_nodes(head, k, is_alternate=True):
    if head is None:
        return None

    prev = None
    curr = head
    next_node = None
    count = 0

    # Reverse alternate k nodes
    while curr is not None and count < k:
        if is_alternate:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        else:
            prev = curr
            curr = curr.next
        count += 1

    # Recursively reverse the remaining nodes
    if is_alternate:
        head.next = reverse_alternate_k_nodes(curr, k, not is_alternate)
    else:
        head.next = reverse_alternate_k_nodes(curr, k, is_alternate)

    return prev
# Example
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(4)
list1.next.next.next.next = Node(5)
list1.next.next.next.next.next = Node(6)
list1.next.next.next.next.next.next = Node(7)
list1.next.next.next.next.next.next.next = Node(8)

k = 3

newList = reverse_alternate_k_nodes(list1, k)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 3 2 1 4 5 6 8 7




                      #Answer --------- 5



class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def delete_last_occurrence(head, key):
    if head is None:
        return None

    prev = None
    curr = head
    last = None

    # Traverse the linked list
    while curr is not None:
        if curr.value == key:
            last = curr
        prev = curr
        curr = curr.next

    # Delete the last occurrence
    if last is not None:
        if prev is None:
            # If the last occurrence is the head node
            head = head.next
        else:
            prev.next = last.next

    return head
# Example 1
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(2)
list1.next.next.next.next = Node(4)
list1.next.next.next.next.next = Node(2)
list1.next.next.next.next.next.next = Node(5)

key = 2

newList = delete_last_occurrence(list1, key)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 1 2 3 2 4 5

# Example 2
list2 = Node(1)
list2.next = Node(2)
list2.next.next = Node(3)
list2.next.next.next = Node(4)
list2.next.next.next.next = Node(5)
list2.next.next.next.next.next = Node(5)

key = 5

newList = delete_last_occurrence(list2, key)

# Print the new list
while newList is not None:
    print(newList.value, end=" ")
    newList = newList.next
# Output: 1 2 3 4 5





                  #Answer --------- 6


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def merge_sorted_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.value <= b.value:
        head = a
        curr_a = a.next
        curr_b = b
    else:
        head = b
        curr_a = a
        curr_b = b.next

    prev = head

    while curr_a is not None and curr_b is not None:
        if curr_a.value <= curr_b.value:
            prev.next = curr_a
            curr_a = curr_a.next
        else:
            prev.next = curr_b
            curr_b = curr_b.next
        prev = prev.next

    if curr_a is not None:
        prev.next = curr_a
    if curr_b is not None:
        prev.next = curr_b

    return head
# Example 1
list_a = Node(5)
list_a.next = Node(10)
list_a.next.next = Node(15)

list_b = Node(2)
list_b.next = Node(3)
list_b.next.next = Node(20)

merged_list = merge_sorted_lists(list_a, list_b)

# Print the merged list
while merged_list is not None:
    print(merged_list.value, end=" ")
    merged_list = merged_list.next
# Output: 2 3 5 10 15 20

# Example 2
list_a = Node(1)
list_a.next = Node(1)

list_b = Node(2)
list_b.next = Node(4)

merged_list = merge_sorted_lists(list_a, list_b)

# Print the merged list
while merged_list is not None:
    print(merged_list.value, end=" ")
    merged_list = merged_list.next
# Output: 1 1 2 4






                #Answer --------- 7

class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    if head is None:
        return None

    curr = head
    prev = None

    while curr is not None:
        # Swap prev and next pointers
        next_node = curr.next
        curr.next = prev
        curr.prev = next_node

        # Move prev and curr pointers
        prev = curr
        curr = next_node

    # Update the head of the reversed list
    head = prev

    return head
# Example
list1 = Node(1)
list1.next = Node(2)
list1.next.prev = list1
list1.next.next = Node(3)
list1.next.next.prev = list1.next
list1.next.next.next = Node(4)
list1.next.next.next.prev = list1.next.next

reversed_list = reverse_doubly_linked_list(list1)

# Print the reversed list
while reversed_list is not None:
    print(reversed_list.value, end=" ")
    reversed_list = reversed_list.next
# Output: 4 3 2 1
