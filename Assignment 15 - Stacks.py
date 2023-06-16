




                          #Answer --------- 1


def find_next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result[::-1]
# Example 1
arr1 = [1, 3, 2, 4]
result1 = find_next_greater_elements(arr1)
print(result1)
# Output: [3, 4, 4, -1]

# Example 2
arr2 = [5, 4, 3, 2, 1]
result2 = find_next_greater_elements(arr2)
print(result2)
# Output: [-1, -1, -1, -1, -1]






                      #Answer --------- 2


def find_nearest_smaller_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result
# Example 1
arr1 = [1, 6, 2]
result1 = find_nearest_smaller_elements(arr1)
print(result1)
# Output: [-1, 1, 1]

# Example 2
arr2 = [5, 4, 9, 7, 2, 6]
result2 = find_nearest_smaller_elements(arr2)
print(result2)
# Output: [-1, -1, 4, 4, -1, 2]





                      #Answer --------- 3



class StackUsingQueues:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.q1 and not self.q2:
            return "Error: Stack is empty"

        if not self.q2:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))

        return self.q1.pop(0)

    def top(self):
        if not self.q1 and not self.q2:
            return "Error: Stack is empty"

        if not self.q2:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))

        return self.q1[0]
stack = StackUsingQueues()

stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
stack.push(4)
print(stack.pop())  # Output: 4







                  #Answer --------- 4



def reverse_stack(stack):
    if len(stack) <= 1:
        return stack

    top_element = stack.pop()
    reversed_stack = reverse_stack(stack)
    reversed_stack.append(top_element)
    return reversed_stack
stack = [3, 2, 1, 7, 6]
reversed_stack = reverse_stack(stack)
print(reversed_stack)
# Output: [6, 7, 1, 2, 3]





                          #Answer --------- 5


def reverse_stack(stack):
    if len(stack) <= 1:
        return stack

    top_element = stack.pop()
    reversed_stack = reverse_stack(stack)
    reversed_stack.append(top_element)
    return reversed_stack
stack = [3, 2, 1, 7, 6]
reversed_stack = reverse_stack(stack)
print(reversed_stack)
# Output: [6, 7, 1, 2, 3]






                  #Answer --------- 6


def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)
# Output: "!dlroW ,olleH"






                  #Answer --------- 7


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            popped_val = self.stack.pop()
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

print(min_stack.getMin())  # Output: -3
print(min_stack.top())  # Output: -3

min_stack.pop()

print(min_stack.getMin())  # Output: -2
print(min_stack.top())  # Output: 0







                        #Answer --------- 8



def trap_water(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left <= right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
water_trapped = trap_water(height)
print(water_trapped)
# Output: 6
