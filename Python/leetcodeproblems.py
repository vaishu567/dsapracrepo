
# 1:
# You are given an integer n, the number of teams in a tournament that has strange rules:
# If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.
# Example 1:
# Input: n = 7
# Output: 6
# Explanation: Details of the tournament: 
# - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 3 + 2 + 1 = 6.
# Example 2:
# Input: n = 14
# Output: 13
# Explanation: Details of the tournament:
# - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
# - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 7 + 3 + 2 + 1 = 13.

# Constraints:
# 1 <= n <= 200
def recforeven(self,x:int)->int:
    matches=x//2
    advances=x//2
    return [advances,matches]


def recforodd(self,x:int)->int:
    matches=(x-1)//2
    advances=matches+1
    return [advances,matches]

def numberOf(self,countofmatches, n: int) -> int:
    if n==2:
        return 1

    if n%2==0:
        advances,matches=self.recforeven(n)
        countofmatches=self.numberOf(countofmatches,advances)
        countofmatches+=matches
    else:
        advances,matches=self.recforodd(n)
        countofmatches=self.numberOf(countofmatches,advances)
        countofmatches+=matches
    return countofmatches


def numberOfMatches(self, n: int) -> int:
    if n==1:
        return 0
    countofmatches=0
    counti=self.numberOf(countofmatches,n)
    return counti

# 2:
# 1716. Calculate Money in Leetcode Bank
# Solved
# Easy
# Topics
# Companies
# Hint
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

# Example 1:

# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# Example 2:

# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
# Example 3:

# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

# Constraints:

# 1 <= n <= 1000
def totalMoney(self, n: int) -> int:
    total=0
    if n<=7:
        total=(n*(n+1))//2
        return total
    loops=n//7
    extra=n%7
    for i in range(loops):
        num=i+7
        naturalsum=((num*(num+1))//2)-((i*(i+1))//2)
        total+=naturalsum
    ep=extra+loops
    sumloops=(loops*(loops+1))//2
    extrasum=((ep*(ep+1))//2)-sumloops
    return total+extrasum
#     Approach 2: Math
# Intuition

# The manner in which we add money is static. Each week we add:

# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
# 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
# 3 + 4 + 5 + 6 + 7 + 8 + 9 = 42
# and so on...
# As you can see, each week we add 7 more dollars than the previous week. Perhaps we can formulate a mathematical solution to this problem.

# We have k = n / 7 full weeks. Here, we are performing integer/floor division. These full weeks form an arithmetic sequence. An arithmetic sequence is a sequence of numbers such that the difference between every adjacent element is the same. Here, we have a common difference of 7.

# The sum of an arithmetic sequence can be found very quickly if we know the following information:

# The first element in the sequence FFF.
# The final element in the sequence LLL.
# The number of elements in the sequence kkk.
# Then, the sum is k⋅(F+L)2\dfrac{k \cdot (F + L)}{2} 
# 2
# k⋅(F+L)
# ​
#  .

# We know the first element in the sequence is 28 and that there are k elements in the sequence, since each element represents a week. What is the final element in the sequence? The final element in the sequence represents how much money we add in the final full week, and we know that the value must be 28 + (k - 1) * 7, since we add 28 dollars on the first week and 7 more dollars each additional week.

# Let F = 28, k = n / 7, L = 28 + (k - 1) * 7. We can then plug each of these values into the above equation to get the total money we deposit in all full weeks as arithmeticSum.

# What if n is not divisible by 7? Then, the final week will have less than 7 days. How do we calculate how much money we get from the final week? First, we need to know how many days are in the final week. We can obtain this by taking n modulo 7, i.e. n % 7.

# Note that we will have k full weeks before the final week, therefore, on the Monday of the final week, we will deposit 1 + k dollars. We can either form another arithmetic sequence for the final week (since we know its first value and how many elements there will be, we can deduce the final value and thus the overall sum), or we could simply iterate over the final week explicitly.

# For the sake of simplicity, we will iterate over the final week explicitly and calculate the money we deposit as finalWeek.

# Finally, the answer to the problem is arithmeticSum + finalWeek.

# Algorithm

# Set the following values:
# k = n / 7.
# F = 28.
# L = 28 + (k - 1) * 7.
# Calculate arithmeticSum = k * (F + L) / 2.
# Initialize monday = 1 + k and finalWeek = 0.
# Iterate day from 0 until n % 7:
# Add monday + day to finalWeek.
# Return arithmeticSum + finalWeek.

    # algo:
    # k = n // 7
    # F = 28
    # L = 28 + (k - 1) * 7
    # arithmetic_sum = k * (F + L) // 2
    
    # monday = 1 + k
    # final_week = 0
    # for day in range(n % 7):
    #     final_week += monday + day
    
    # return arithmetic_sum + final_week



# largest oddnumber in string:
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # ans=""
        # maxi=float('-inf')
        # new=0
        # # converting string to num:
        # for i in num:
        #     nu=(ord(i)-48)
        #     if nu%2!=0:
        #         maxi=max(maxi,nu)
        #     new=new*10+nu
        #     if new%2!=0:
        #         maxi=max(maxi,new)
        # if new%2!=0:
        #     maxi=max(maxi,new)
        #     return str(maxi)
        # if maxi!=float('-inf'):
        #     return str(maxi)
        # return ans
        n=len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2!=0:
                return num[0:i+1]
        return ""

def removeOuterParentheses(s):
    count=0
    for i in range(len(s)-1):
        if s[i]=="(" and s[i+1]==")":
            count+=1
    new=""
    for i in range(count):
        new+="()"
    return count
print(removeOuterParentheses("(()())(())"))