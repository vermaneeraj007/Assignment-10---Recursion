

                    #Answer -------- 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddleNode(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return head

# Create the linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Delete the middle node(s)
head = deleteMiddleNode(head)

# Print the modified linked list
current = head
while current:
    print(current.val, end=" ")
    current = current.next




                 #Answer -------- 2


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasLoop(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

# Create the linked list: 1->3->4->2 (loop at position 2)
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(2)
head.next.next.next.next = head.next

# Check if the linked list contains a loop
has_loop = hasLoop(head)

# Print the result
print(has_loop)  # Output: True





                    #Answer -------- 3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findNthFromEnd(head, N):
    if not head:
        return None

    fast = head
    slow = head

    # Move the fast pointer N nodes ahead
    for _ in range(N):
        if not fast:
            return None
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    return slow.val


# Create the linked list: 1->2->3->4->5->6->7->8->9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

# Find the 2nd node from the end
N = 2
result = findNthFromEnd(head, N)

# Print the result
print(result)  # Output: 8






                    #Answer -------- 4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    # Find the middle of the linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Compare the first half with the reversed second half
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    # Restore the original linked list by reversing the second half again
    prev = None
    curr = prev
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return True





                    #Answer -------- 5

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeLoop(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    # Find the meeting point of the slow and fast pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If there is no loop, return the original linked list
    if slow != fast:
        return head

    # Reset either the slow or fast pointer to the head of the list
    slow = head

    # Move both pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop by setting the next pointer of the node where the loop starts to None
    fast.next = None

    return head
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeLoop(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    # Find the meeting point of the slow and fast pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If there is no loop, return the original linked list
    if slow != fast:
        return head

    # Reset either the slow or fast pointer to the head of the list
    slow = head

    # Move both pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop by setting the next pointer of the node where the loop starts to None
    fast.next = None

    return head




                #Answer -------- 6


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverseAndDelete(head, M, N):
    if not head:
        return None

    current = head

    while current:
        # Traverse M nodes
        for _ in range(M-1):
            if current:
                current = current.next
            else:
                return head

        # If current pointer is None, there are no more nodes to retain
        if not current:
            return head

        # Delete N nodes
        temp = current.next
        for _ in range(N):
            if temp:
                temp = temp.next
            else:
                current.next = None
                return head

        # Update the next pointer of the Mth node
        current.next = temp

        # Move the current pointer to the next node
        current = temp

    return head

# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

M = 2
N = 1

new_head = traverseAndDelete(head, M, N)

# The modified linked list: 1 -> 2 -> 4 -> 5 -> None






                #Answer -------- 7




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertAlternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    curr1 = head1
    curr2 = head2
    next1 = None
    next2 = None

    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next

        curr1.next = curr2
        curr2.next = next1

        curr1 = next1
        curr2 = next2

    if curr2:
        curr1.next = curr2

    return head1


# Create the first linked list: 5 -> 7 -> 17 -> 13 -> 11 -> None
head1 = ListNode(5)
head1.next = ListNode(7)
head1.next.next = ListNode(17)
head1.next.next.next = ListNode(13)
head1.next.next.next.next = ListNode(11)

# Create the second linked list: 12 -> 10 -> 2 -> 4 -> 6 -> None
head2 = ListNode(12)
head2.next = ListNode(10)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(6)

new_head1 = insertAlternate(head1, head2)

# The modified first linked list: 5 -> 12 -> 7 -> 10 -> 17 -> 2 -> 13 -> 4 -> 11 -> 6 -> None
# The second linked list becomes empty: None































