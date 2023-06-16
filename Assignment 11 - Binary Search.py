




                 #Answer ------- 1


def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    return right
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
print(mySqrt(9))  # Output: 3
print(mySqrt(16)) # Output: 4




                 #Answer ------- 2

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


print(findPeakElement([1, 2, 3, 1]))   # Output: 2
print(findPeakElement([1, 2, 1, 3, 5]))   # Output: 4
print(findPeakElement([1, 2, 3, 4, 5]))   # Output: 4




                     #Answer ------- 3

def missingNumber(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(missingNumber([3, 0, 1]))   # Output: 2
print(missingNumber([0, 1]))      # Output: 2





                 #Answer ------- 4

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

  
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2




                     #Answer ------- 5

def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)

print(intersection([1, 2, 2, 1], [2, 2]))   # Output: [2]





                 #Answer ------- 6


def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

print(findMin([3, 4, 5, 1, 2]))   # Output: 1
print(findMin([4, 5, 6, 7, 0, 1, 2]))   # Output: 0





                     #Answer ------- 7

def searchRange(nums, target):
    def findLeftmost(nums, target):
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                index = mid

        return index

    def findRightmost(nums, target):
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                index = mid

        return index

    leftmost = findLeftmost(nums, target)
    rightmost = findRightmost(nums, target)

    return [leftmost, rightmost]

print(searchRange([5, 7, 7, 8, 8, 10], 8))   # Output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))   # Output: [-1, -1]





                #Answer ------- 8

from collections import Counter

def intersect(nums1, nums2):
    count1 = Counter(nums1)
    result = []

    for num in nums2:
        if num in count1 and count1[num] > 0:
            result.append(num)
            count1[num] -= 1

    return result

print(intersect([1, 2, 2, 1], [2, 2]))   # Output: [2, 2]



















