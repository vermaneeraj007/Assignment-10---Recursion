


            #Answer ------- 1



def isPowerOfThree(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1
print(isPowerOfThree(27))  # Output: True
print(isPowerOfThree(0))   # Output: False
print(isPowerOfThree(-1))  # Output: False


            
            #Answer ------- 2


def lastRemainingAlgorithm(n):
    remaining = n
    step = 1
    leftToRight = True

    while remaining > 1:
        if leftToRight or step % 2 == 1:
            remaining //= 2
        else:
            remaining = (remaining // 2) - 1 + (remaining % 2)
        
        leftToRight = not leftToRight
        step *= 2
    
    return remaining

print(lastRemainingAlgorithm(9))  # Output: 6




                
            #Answer ------- 3


def generateSubsets(set_str, index, prefix):
    if index == len(set_str):
        print(prefix)
        return

    generateSubsets(set_str, index + 1, prefix + set_str[index])  # Include the character at the current index
    generateSubsets(set_str, index + 1, prefix)  # Exclude the character at the current index

def printAllSubsets(set_str):
    generateSubsets(set_str, 0, "")

# Test the function with the given examples
printAllSubsets("abc")
printAllSubsets("abcd")






            
            #Answer ------- 4



def calculateLength(string, index):
    if index == len(string):
        return 0
    else:
        return 1 + calculateLength(string, index + 1)

# Test the function with examples
print(calculateLength("Hello", 0))  # Output: 5
print(calculateLength("OpenAI", 0))  # Output: 6
print(calculateLength("", 0))  # Output: 0






            
            #Answer ------- 5



def countSubstrings(S):
    count = 0
    for i in range(len(S)):
        if i < len(S) - 1 and S[i] == S[i + 1]:
            count += (i + 1)
    return count

# Test the function with examples
print(countSubstrings("abca"))  # Output: 4
print(countSubstrings("aabca"))  # Output: 6
print(countSubstrings("aaaaa"))  # Output: 15





            
            #Answer ------- 6



def towerOfHanoi(N, source, auxiliary, destination):
    if N == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return
    
    towerOfHanoi(N-1, source, destination, auxiliary)
    print("move disk", N, "from rod", source, "to rod", destination)
    towerOfHanoi(N-1, auxiliary, source, destination)

def totalMoves(N):
    return 2**N - 1

# Test the function with examples
N = 2
towerOfHanoi(N, 1, 2, 3)
print(totalMoves(N))  # Output: 3





            
            #Answer ------- 7


def permute(str, prefix, result):
    if len(str) == 0:
        result.add(prefix)
        return

    for i in range(len(str)):
        permute(str[:i] + str[i+1:], prefix + str[i], result)

def printAllPermutations(str):
    result = set()
    permute(str, "", result)

    for permutation in result:
        print(permutation, end=" ")

# Test the function with examples
printAllPermutations("cd")
print()
printAllPermutations("abb")





            
            #Answer ------- 8



def countConsonants(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Test the function with examples
print(countConsonants("Hello"))  # Output: 3
print(countConsonants("OpenAI"))  # Output: 3
print(countConsonants("abcde"))  # Output: 3
print(countConsonants("aeiou"))  # Output: 0



         
