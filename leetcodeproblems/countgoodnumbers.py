# # Certainly! Let's break down the code:

# # The function countGoodNumbers takes an integer n as input and returns the count of good numbers of length n.

# # We start by defining a constant MOD as 10**9 + 7. This is because the result needs to be returned modulo 10**9 + 7 as mentioned in the problem statement.

# # We define a helper function pow_mod to perform modular exponentiation efficiently. This function calculates (base ** exp) % MOD using binary exponentiation. It iterates through the binary representation of exp and multiplies the base accordingly, reducing the time complexity significantly compared to traditional exponentiation.

# # Next, we count the number of even and prime digits needed for constructing the good numbers. Since even digits can be any of 0, 2, 4, 6, 8, and prime digits can be 2, 3, 5, or 7, we use (n + 1) // 2 to count the even digits and n // 2 to count the prime digits.

# # To calculate the count of good numbers, we use the formula (5 ** even_count * 4 ** prime_count) % MOD. This formula represents the count of good numbers because for each even index, there are 5 options (0, 2, 4, 6, 8), and for each odd index, there are 4 options (2, 3, 5, 7). We use modular exponentiation (pow_mod) to efficiently compute (5 ** even_count) and (4 ** prime_count).

# # Finally, we return the result modulo MOD.

# # This approach avoids iterating through all possible numbers, making it much more efficient and suitable for large values of n




# We can see it's fairly easy problem, hard step was calculating power efficently and using modulas

# Power functions full analysis
# Exponentiation is a mathematical operation that is expressed as x^n and computed as x^n = x.x.x....x(n times).
# We have two methods for calculating exponents, recursive and iterative.

# Here, I will talk about recursive approaches, you can try iterative this will be your homework ;P

# Basic method
# While calculating x^n, the most basic solution is broken down into x.x^(n-1). The new problem is x^(n-1), which is similar to the original problem. Therefore, like in original problem, it is further broken down to x.x.x^(n-2).

# This is the recursive approach to find x^n.
# Also we know base case will be, n == 0 here ans = 1

# int recursivePower(int x,int n) {
#     if(n == 0) return 1;
#     return x*recursivePower(x,n-1);
# }
# Time complexity:
# With respect to time complexity, it is a fairly efficient O(n) solution.
# However, when it comes to finding , where can be as large as 10^15 , this solution will not be suitable.


# Optimized method
# While calculating x^n, n can be odd or even.

# If n is even, then n can be broken down to (x^2)^(n/2). Finding x^2 is a one-step process.
# However, finding (A)^(n/2) will take some time here A = x^2.

# When x^n is odd, we can convert it into an even value. x^n can be written as x.x^(n-1).
# This ensures that (n-1) is even. So it can be again broken down to (n-1)/2 in next step.

# Notice how the computation steps were reduced from n to n/2 in just one step.
# You can continue to divide the power by 2 as long as it is even or if it's odd make it even.

# Approach has two steps:
# If n is even, replace x^n by (x^2)^(n/2).
# If n is odd, replace x^n by x.x^(n-1). n-1 becomes even and you can apply the relevant formula again.
# Example:
# We need to find 5^10

# Naive approach will be,

# 5^10 = 5.5^9
#      = 5.5.5^8
#      = 5.5.5^7
#      = 5.5.5.5^6
#      = 5.5.5.5.5^5
#      = 5.5.5.5.5.5^4
#      = 5.5.5.5.5.5.5^3
#      = 5.5.5.5.5.5.5.5^2
#      = 5.5.5.5.5.5.5.5.5^1
#      = 5.5.5.5.5.5.5.5.5.1
# We can see it took us n steps to find 5^n

# Optimal Approach

# 5^10 = (5^2)^5
#      = 25.25^4
#      = 25.(25^2)^2
#      = 25.(625)^2
#      = 25.625.625
# This is an efficient method and the ten-step process of determining 5^10 is reduced to a four-step process. At every step, n is divided by 2.

# Time Complexity
# Therefore, the time complexity is O(log N).

# int binaryExponentiation(int x,int n) {
#     if(n==0) return 1;
#     //n is even
#     else if(n%2 == 0)        
#         return binaryExponentiation(x*x,n/2);
#     //n is odd
#     else                             
#         return x*binaryExponentiation(x*x,(n-1)/2);
# }
# Modulo Exponetiation
# However, storing answers that are too large for their respective datatypes is an issue with this method.
# In such instances, you must use modulus (%). Instead of finding x^n, you must find (x^n) % M.
# For example, run the implementation of the method to find . The solution will timeout, while the solution will run in time but it will produce garbage values.

# If we needed to find 2^(10^5) or something big, then approach will run in O(logn) time, but produces garbage values as ans.

# int modularExponentiation(int x, int n, int M) {
#     if(n==0) return 1;
#     //n is even
#     else if(n%2 == 0)        
#         return modularExponentiation((x*x) % M, n/2, M);
#     //n is odd
#     else                             
#         return (x*modularExponentiation((x*x) % M, (n-1)/2, M)) % M;
# }
# Time complexity: O(log N)
# Memory complexity: O(log N) because a function call consumes memory and log N recursive function calls are made

# Note: Iterative ways more optimal, because recursive solutions require stack memory.
# Also sometimes, (x*x) even can run out of int limit


# Question Approach
# Now, we know we have 4 primes = {2, 3, 5, 7} and 5 evens = {0, 2, 4, 6, 8}

# if index == 0
# then there can be any of one evens at even position, so 5 ways
# ans = 5

# if index == 1
# then there was 1 even at index = 0, and at this odd index there can be one of 4 primes
# ans = 5* 4(this pos)

# if index == 2
# then at this even index there can be one of 5 evens
# ans = (5*4) * 5(this pos)

# so, continuing the pattern we can see, it's like, 5*4*5*4*5*4*5..... ans so on
# here no. of 4s = no. of odd positions = n/2
# no. of 5s = no. of even positions = (n-n/2)

# ans = pow(4,count4) * pow(5,count5)

# Solution:
# #define ll long long

# class Solution {
# public:
#     // evens  = 0, 2, 4, 6, 8  => 5 evens
#     // primes = 2, 3, 5, 7     => 4 primes
  
#     int p = 1e9 + 7;
    
#     // calculating x^y efficeiently
#     ll power(long long x, long long y) {
#       long long res = 1;    

#       x = x % p; // Update x if it is more than or equal to p
#       if (x == 0) return 0; 

#       while (y > 0) {
#         // If y is odd, multiply x with result
#         if (y & 1) res = (res*x) % p;
        
#         // we have did the odd step is it was odd, now do the even step
#         y = y>>1; // dividing y by 2, y>>1 is same as y/2
#         x = (x*x) % p;
#       }
#       return res;
#     }
  
#     int countGoodNumbers(long long n) {
#       ll count_of_4s = n/2;
#       ll count_of_5s = n - count_of_4s;
#       ll ans = ((power(4LL, count_of_4s) % p  * power(5LL, count_of_5s) % p) % p);
#       return (int)ans;
#     }
# };

def countGoodNumbers(self, n: int) -> int:
    MOD = 10 ** 9 + 7

    def pow_mod(base, exp):
        result = 1
        while exp:
            # if exp is odd, multipy base with result
            if exp & 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            # right shifting exp so that it gets halved every time:
            exp =exp>> 1
        return result

    # Count the number of even and prime digits
    even_count = (n + 1) // 2
    prime_count = n // 2

    # Calculate the number of good numbers
    result = (pow_mod(5, even_count) * pow_mod(4, prime_count)) % MOD
    return result