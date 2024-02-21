# Approach
# To compute the bitwise AND of all numbers in the range [left, right], you can iterate through the range and perform bitwise AND operation on all the numbers. However, there's a more efficient solution.

# The bitwise AND operation between two numbers results in a number where each bit is 1 if and only if the corresponding bits of both numbers are 1. When you're considering a range [left, right], if the two numbers have different bits in any position, then the result of the AND operation will have a 0 in that position. So, you only need to find the common prefix of the binary representation of left and right.

# The approach used in the code is to find the common prefix of the binary representations of left and right. Since we're performing a bitwise AND operation, any bits that differ between left and right will be set to 0 in the result.

# Here's how the code works with an example:

# Let's take left = 5 and right = 7.

# Convert left and right to binary:

# left = 5 in binary is 101.
# right = 7 in binary is 111.
# Now, we iterate through a loop until left becomes greater than or equal to right.

# In the first iteration:
# left = 101 >> 1 becomes 10 (which is 2 in decimal).
# right = 111 >> 1 becomes 11 (which is 3 in decimal).
# shift becomes 1.
# In the second iteration:
# left = 10 >> 1 becomes 1 (which is 1 in decimal).
# right = 11 >> 1 becomes 1 (which is 1 in decimal).
# shift becomes 2.
# Now, left is equal to right and we exit the loop.

# Finally, we left-shift left by shift bits and return the result:

# left << shift becomes 1 << 2 which is 100 (which is 4 in decimal).
# So, the bitwise AND of all numbers in the range [5, 7] is 4.
# here if we write numbers in their binary form we are performing right shifts on both numbers till they get equal and when they get equal that is considered to be common prefix rest of the numbers which are not equal will obviously canceled when we perform and operation
# hence we are considering common prefix and for that we perform back left shifts with no.of shifts we got
def bitwiserange(left,right):
    shifts=0
    while left < right:
        left>>=1
        right>>=1
        shifts+=1
    return (left<<shifts)
print(bitwiserange(4,7))
