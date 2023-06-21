

            #Answer ------- 1





def nearest_greater_frequency(arr):
    frequency = {}
    result = []
    n = len(arr)

    for i in range(n - 1, -1, -1):
        if arr[i] in frequency and frequency[arr[i]] > max(frequency.values()):
            result.append(arr[i])
        else:
            result.append(-1)
        frequency[arr[i]] = frequency.get(arr[i], 0) + 1

    return result[::-1]
arr = [1, 1, 2, 3, 4, 2, 1]
output = nearest_greater_frequency(arr)
print(output)

arr = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
output = nearest_greater_frequency(arr)
print(output)



             #Answer ------- 2




def sort_stack(stack):
    temp_stack = []

    while stack:
        current = stack.pop()

        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())

        temp_stack.append(current)

    while temp_stack:
        stack.append(temp_stack.pop())


    return stack
stack = [5, 2, 8, 1, 9]
output = sort_stack(stack)
print(output)
stack = [9, 3, 6, 2, 4, 1]
output = sort_stack(stack)
print(output)



                    
             #Answer ------- 3

def delete_middle(stack):
    size = len(stack)

    def delete_middle_helper(stack, mid_index):
        if mid_index == 0:
            stack.pop()
            return

        temp = stack.pop()
        delete_middle_helper(stack, mid_index - 1)
        stack.append(temp)

    mid_index = size // 2
    delete_middle_helper(stack, mid_index)

    return stack
stack = [1, 2, 3, 4, 5]
output = delete_middle(stack)
print(output)
stack = [1, 2, 3, 4, 5, 6]
output = delete_middle(stack)
print(output)



            
             #Answer ------- 4

def arrange_increasing_order(queue):
    stack = []
    new_queue = []
    expected = 1

    while queue:
        current = queue.pop(0)

        if current == expected:
            new_queue.append(current)
            expected += 1
        elif current > expected:
            if stack and stack[-1] == expected:
                new_queue.append(stack.pop())
                expected += 1
            else:
                stack.append(current)
        else:
            return "No"

    while stack:
        if stack[-1] == expected:
            new_queue.append(stack.pop())
            expected += 1
        else:
            return "No"

    return "Yes"
queue = [5, 1, 2, 3, 4]
output = arrange_increasing_order(queue)
print(output)
queue = [5, 1, 2, 6, 3, 4]
output = arrange_increasing_order(queue)
print(output)



             #Answer ------- 5

def reverse_number(number):
    stack = []
    number_str = str(number)

    for digit in number_str:
        stack.append(digit)

    reversed_number = ""
    while stack:
        reversed_number += stack.pop()

    return int(reversed_number)
number = 12345
output = reverse_number(number)
print(output)
number = 987654321
output = reverse_number(number)
print(output)




             #Answer ------- 6


from queue import Queue

def reverse_k_elements(queue, k):
    stack = []
    for _ in range(k):
        stack.append(queue.get())

    temp_queue = Queue()
    while stack:
        temp_queue.put(stack.pop())

    while not queue.empty():
        temp_queue.put(queue.get())

    return temp_queue
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3
reversed_queue = reverse_k_elements(queue, k)

while not reversed_queue.empty():
    print(reversed_queue.get(), end=" ")



             #Answer ------- 7

def count_remaining_words(sequence):
    word_stack = []

    for word in sequence:
        if not word_stack or word != word_stack[-1]:
            word_stack.append(word)
        else:
            word_stack.pop()

    return len(word_stack)
sequence = ["ab", "aa", "aa", "bcd", "ab"]
output = count_remaining_words(sequence)
print(output)
sequence = ["tom", "jerry", "jerry", "tom"]
output = count_remaining_words(sequence)
print(output)



             #Answer ------- 8



def max_absolute_difference(arr):
    n = len(arr)
    leftStack = []
    rightStack = []
    LS = [0] * n
    RS = [0] * n

    for i in range(n):
        while leftStack and leftStack[-1] >= arr[i]:
            leftStack.pop()

        if leftStack:
            LS[i] = leftStack[-1]

        leftStack.append(arr[i])

    for i in range(n-1, -1, -1):
        while rightStack and rightStack[-1] >= arr[i]:
            rightStack.pop()

        if rightStack:
            RS[i] = rightStack[-1]

        rightStack.append(arr[i])

    maxDiff = 0
    for i in range(n):
        diff = abs(LS[i] - RS[i])
        if diff > maxDiff:
            maxDiff = diff

    return maxDiff
arr = [2, 1, 8]
output = max_absolute_difference(arr)
print(output)
arr = [2, 4, 8, 7, 7, 9, 3]
output = max_absolute_difference(arr)
print(output)



