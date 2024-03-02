# A binary string is odd if and only if the last bit (i.e. the one's place) equals 1. Consider an integer in its base-2 representation. Most of its bits will not affect the integer's divisibility by 222 since 2b2^b2 
# b
#   is always even for any b≥1b \geq 1b≥1. Therefore, it is required that the bit corresponding to 202^02 
# 0
#   (the rightmost bit) is equal to 1 in any odd number, and equal to 0 in any even number.

# To rearrange bits in such a way as to maximize the value of the binary number, we should opt to swap as many 1 bits to the left as we can. This is because the more left a digit is, the more value it holds. A similar conclusion can be reached if we think about how the base-10 number system works.

# We can combine these ideas into a strategy for building the maximum odd binary number! Place all but one 1 bit to the most significant places (i.e. leftmost bits), place a 1 in the one's place, and fill the rest of the string with 000 bits (if any). Note that at least one 1 is guaranteed to be present in the string, which ensures that the resulting number is always odd.

# The maximum odd binary number will have this format: "111...111000...0001".

# Approach 1: Greedy Bit Manipulation (Sorting and Swapping)
# Intuition
# One approach for implementing the above strategy is to sort all the bits first, and then reverse the elements from the first index to the second to last index. This works because the initial sort will guarantee the resulting string is odd, and reversing the rest of the characters will maximize the string's value.

# Algorithm
# Sort the input string s in ascending order.
# Reverse the bits in substring [0,N−2][0, N-2][0,N−2].
# Return the resulting string.

# Complexity Analysis
# Time complexity: O(nlog⁡n)O(n \log n)O(nlogn).
# Sorting input string s takes O(nlog⁡n)O(n \log n)O(nlogn). We also iterate through sss which takes O(n)O(n)O(n). O(nlog⁡n)O(n \log n)O(nlogn) is the dominating term, which is the final time complexity.

# Space complexity: O(n)O(n)O(n)
# We create an auxillary array to process the string, requiring O(n)O(n)O(n) space.
# Some extra space is used when we sort sss in place. The space complexity of the sorting algorithm depends on the programming language.
# In Python, the sort method sorts a list using the Timesort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n)O(n)O(n) additional space. No additional space is needed for the algorithm.
# In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(log⁡n)O(\log n)O(logn) for sorting two arrays.
# In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(log⁡n)O(\log n )O(logn).
# The space required for the array is the dominating term, so the overall space complexity is O(n)O(n)O(n).

def maximumOddBinaryNumber(s):

    arr = sorted(s)

    # Reverse order for the first N - 1 elements of the array
    # Because we want to keep a 1 at the last index
    # The last element of the array is index N - 1, the second the last is at N - 2
    secondLast = len(arr) - 2
    for i in range(len(arr) // 2):
        arr[i], arr[secondLast - i] = arr[secondLast - i], arr[i]

    # Return result
    return "".join(arr)

# Approach 2: Greedy Bit Manipulation (Counting Ones)
# Intuition
# The answer depends only on the length of the input nnn and the number of times 1 appears in the input. This means we can construct the answer directly by counting the number of ones and building a string with ones_cnt - 1 occurrences of 1, followed by n - ones_cnt occurrences of 0, and a single occurrence of 1 at the end to ensure the final string is odd.

# Algorithm
# Count the number of occurrences of 1 in input s; let this count be ones_cnt.
# Take bit 1 and append it ones_cnt - 1 times. This ensures we maximize the value of the result, but we save a bit at the end to ensure the result is odd.
# Take bit 0 and append it n - ones_cnt times. These are the 0 bits that we must include.
# Append a single 1 bit. This keeps the result string an odd number.
# Return the resulting string.

def maximumOddBinaryNumber(s):
    n=len(s)
    countofones=s.count('1')
    return '1'*(countofones-1)+'0'*(n-countofones)+'1'


    # def maximumOddBinaryNumber(self, s: str) -> str:
    #     # Get n and char array
    #     N = len(s)
    #     arr = [char for char in s]

    #     left = 0
    #     right = N - 1
    #     while left <= right:
            
    #         # Increment left if equals 1
    #         if arr[left] == '1':
    #             left += 1
    #         # Decrement right if equals 0
    #         if arr[right] == '0':
    #             right -= 1
    #         # Swap if neither pointer can be iterated
    #         if left <= right and arr[left] == '0' and arr[right] == '1':
    #             arr[left] = '1'
    #             arr[right] = '0'
        
    #     # Swap rightmost 1 bit to the end
    #     arr[left - 1] = '0'
    #     arr[N - 1] = '1'

    #     return "".join(arr)