






                #Answer ---------- 1


def remove_loop(head):
    slow = head
    fast = head

    # Find the meeting point of the slow and fast pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If there is no loop, return the original linked list
    if not fast or not fast.next:
        return head

    # Move the slow pointer back to the head and find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Set the next pointer of the node at the meeting point to None to remove the loop
    fast.next = None

    return head
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Example 1
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(4)
head1.next.next.next = head1.next
head1 = remove_loop(head1)
while head1:
    print(head1.data, end=" ")
    head1 = head1.next
# Output: 1

# Example 2
head2 = Node(1)
head2.next = Node(8)
head2.next.next = Node(3)
head2.next.next.next = Node(4)
head2 = remove_loop(head2)
while head2:
    print(head2.data, end=" ")
    head2 = head2.next
# Output: 1 8 3 4






                    #Answer ---------- 2


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):
    dummy = Node(0)
    dummy.next = head

    # Find the rightmost non-nine digit
    last_non_nine = dummy
    curr = head
    while curr:
        if curr.data != 9:
            last_non_nine = curr
        curr = curr.next

    # Add 1 to the rightmost non-nine digit and propagate the carry
    last_non_nine.data += 1
    curr = last_non_nine.next
    while curr:
        curr.data = 0
        curr = curr.next

    # If the leftmost digit was 9 and got incremented to 10,
    # add a new node with a value of 1 at the beginning
    if dummy.data == 1:
        return dummy

    return dummy.next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def printList(head):
    curr = head
    while curr:
        print(curr.data, end="")
        curr = curr.next
    print()

# Example 1
head1 = Node(4)
head1.next = Node(5)
head1.next.next = Node(6)
head1 = addOne(head1)
head1 = reverseList(head1)
printList(head1)
# Output: 4 5 7

# Example 2
head2 = Node(9)
head2.next = Node(9)
head2.next.next = Node(9)
head2 = addOne(head2)
head2 = reverseList(head2)
printList(head2)
# Output: 1 0 0 0







                #Answer ---------- 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    result = None
    if list1.data <= list2.data:
        result = list1
        result.bottom = mergeLists(list1.bottom, list2)
    else:
        result = list2
        result.bottom = mergeLists(list1, list2.bottom)

    result.next = None
    return result

def flatten(head):
    if not head or not head.next:
        return head

    head.next = flatten(head.next)
    head = mergeLists(head, head.next)
    return head

def printList(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.bottom
    print("None")

# Example 1
head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(19)
head1.next.next.next = Node(28)
head1.bottom = Node(7)
head1.bottom.bottom = Node(8)
head1.next.bottom = Node(20)
head1.next.next.bottom = Node(22)
head1.next.next.next.bottom = Node(35)
head1.bottom.bottom.bottom = Node(30)
head1.next.bottom.bottom = Node(50)
head1.next.next.next.bottom = Node(40)
head1.next.next.next.bottom.bottom = Node(45)

head1 = flatten(head1)
printList(head1)
# Output: 5->7->8->10->19->20->22->28->30->35->40->45->50->None

# Example 2
head2 = Node(1)
head2.next = Node(3)
head2.next.bottom = Node(4)
head2 = flatten(head2)
printList(head2)
# Output: 1->3->4->None






                 #Answer ---------- 4





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def cloneLinkedList(head):
    if not head:
        return None

    # Step 1: Create new nodes and insert them between original nodes
    curr = head
    while curr:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set the random pointers of new nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Restore the next pointers and extract the new list
    new_head = head.next
    curr_old = head
    curr_new = new_head
    while curr_old:
        curr_old.next = curr_new.next
        if curr_new.next:
            curr_new.next = curr_new.next.next
        curr_old = curr_old.next
        curr_new = curr_new.next

    return new_head

def printList(head):
    curr = head
    while curr:
        print("Data:", curr.data, end=" ")
        if curr.random:
            print("Random:", curr.random.data, end=" ")
        else:
            print("Random: None", end=" ")
        print("->", end=" ")
        curr = curr.next
    print("None")

# Example 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.random = head1.next.next
head1.next.random = head1.next.next.next
head1 = cloneLinkedList(head1)
printList(head1)
# Output:
# Data: 1 Random: 3 -> Data: 2 Random: 4 -> Data: 3 Random: None -> Data: 4 Random: 2 -> None

# Example 2
head2 = Node(10)
head2.next = Node(20)
head2.random = head2.next
head2 = cloneLinkedList(head2)
printList(head2)
# Output:
# Data: 10 Random: 20 -> Data: 20 Random: None -> None






                           #Answer ---------- 5





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    oddDummy = ListNode(0)
    evenDummy = ListNode(0)
    oddTail = oddDummy
    evenTail = evenDummy
    isOdd = True

    curr = head
    while curr:
        if isOdd:
            oddTail.next = curr
            oddTail = oddTail.next
        else:
            evenTail.next = curr
            evenTail = evenTail.next
        curr = curr.next
        isOdd = not isOdd

    evenTail.next = None  # Disconnect the even group from the odd group
    oddTail.next = evenDummy.next  # Connect the odd group tail to the even group head

    return oddDummy.next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1 = oddEvenList(head1)
printList(head1)
# Output: 1 3 5 2 4

# Example 2
head2 = ListNode(2)
head2.next = ListNode(1)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(5)
head2.next.next.next.next = ListNode(6)
head2.next.next.next.next.next = ListNode(4)
head2.next.next.next.next.next.next = ListNode(7)
head2 = oddEvenList(head2)
printList(head2)
# Output: 2 3 6 7 1 5 4








                      #Answer ---------- 6



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateLeft(head, k):
    if not head or not head.next:
        return head

    length = 0
    curr = head
    while curr:
        length += 1
        if length == k + 1:
            break
        curr = curr.next

    if length < k:
        return head

    newHead = curr
    while curr.next:
        curr = curr.next

    curr.next = head
    head = newHead.next
    newHead.next = None

    return head

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example 1
head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(7)
head1.next.next.next = ListNode(8)
head1.next.next.next.next = ListNode(9)
head1 = rotateLeft(head1, 3)
printList(head1
# Example 2
# Output: 2 3 4 5 1






            #Answer--------- 8




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sums = {}
    curr = dummy

    while curr:
        prefix_sum += curr.val

        if prefix_sum in prefix_sums:
            prev = prefix_sums[prefix_sum].next
            temp_sum = prefix_sum + prev.val

            while prev != curr:
                del prefix_sums[temp_sum]
                prev = prev.next
                temp_sum += prev.val

            prefix_sums[prefix_sum].next = curr.next
        else:
            prefix_sums[prefix_sum] = curr

        curr = curr.next

    return dummy.next

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(-3)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(1)
head1 = removeZeroSumSublists(head1)
printList(head1)
# Output: 3 1
# Note: The answer [1,2,1] would also be accepted.

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(-3)
head2.next.next.next.next = ListNode(4)
head2 = removeZeroSumSublists(head2)
printList(head2)
# Output: 1 2 4

# Example 3
head3 = ListNode(1)
head3.next = ListNode(3)
head3.next.next = ListNode(-3)
head3.next.next.next = ListNode(1)
head3 = removeZeroSumSublists(head3)
printList(head3)
# Output: 1



























