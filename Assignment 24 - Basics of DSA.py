


#Answer ------ 1


def romanToInt(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = len(s)
    
    for i in range(n):
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
            result -= roman_values[s[i]]
        else:
            result += roman_values[s[i]]
    
    return result

print(romanToInt("III"))  # Output: 3
print(romanToInt("LVIII"))  # Output: 58





#Answer -------- 2


def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()
    n = len(s)
    
    while end < n:
        if s[end] not in seen:
            seen.add(s[end])
            current_length = end - start + 1
            max_length = max(max_length, current_length)
            end += 1
        else:
            seen.remove(s[start])
            start += 1
    
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))  # Output: 1
print(lengthOfLongestSubstring("pwwkew"))  # Output: 3






#Answer ---------- 3


def majorityElement(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verification
    count = nums.count(candidate)
    n = len(nums)
    if count > n // 2:
        return candidate
    else:
        return None
print(majorityElement([3, 2, 3]))  # Output: 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2




#Answer --------- 4



def groupAnagrams(strs):
    anagram_dict = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    
    return list(anagram_dict.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))





#Answer --------- 5


def nthUglyNumber(n):
    ugly = [1]  # Initialize with the first ugly number
    p2, p3, p5 = 0, 0, 0  # Pointers for multiples of 2, 3, and 5

    for i in range(1, n):
        next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        ugly.append(next_ugly)

        if next_ugly == ugly[p2] * 2:
            p2 += 1
        if next_ugly == ugly[p3] * 3:
            p3 += 1
        if next_ugly == ugly[p5] * 5:
            p5 += 1

    return ugly[-1]

print(nthUglyNumber(10))  # Output: 12
print(nthUglyNumber(1))  # Output: 1








#Answer --------- 6



import heapq
from collections import Counter

def topKFrequent(words, k):
    word_count = Counter(words)  # Count the frequency of each word
    pq = []

    for word, count in word_count.items():
        heapq.heappush(pq, (-count, word))  # Use negative count for max heap

    result = []
    for _ in range(k):
        result.append(heapq.heappop(pq)[1])

    return result

words1 = ["i", "love", "leetcode", "i", "love", "coding"]
k1 = 2
print(topKFrequent(words1, k1))  # Output: ["i", "love"]

words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k2 = 4
print(topKFrequent(words2, k2))  # Output: ["the", "is", "sunny", "day"]







#Answer --------- 7


from collections import deque

def maxSlidingWindow(nums, k):
    window = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside the current window
        if window and window[0] == i - k:
            window.popleft()
        
        # Remove smaller elements from the right
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        
        window.append(i)
        
        # Add maximum element to the result
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))







#Answer --------- 8




def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - 1

    while right - left + 1 > k:
        diff1 = abs(arr[left] - x)
        diff2 = abs(arr[right] - x)

        if diff1 >= diff2:
            left += 1
        else:
            right -= 1

    return arr[left:right+1]

arr1 = [1, 2, 3, 4, 5]
k1 = 4
x1 = 3
print(findClosestElements(arr1, k1, x1))  # Output: [1, 2, 3, 4]

arr2 = [1, 2, 3, 4, 5]
k2 = 4
x2 = -1
print(findClosestElements(arr2, k2, x2))  # Output: [1, 2, 3, 4]









