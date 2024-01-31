# since they are asking palindromic substr we can approach it using lcs if we divide the array into half and then find for equal subsequences
# or if we reverse the strng and using original and reversed string if we do lcs then we can easily find the longest common palindrom subsequence len:
def longestPalindromeSubsequence(s):
    # Write your code here.
    n=len(s)
    s2=s[::-1]
    dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for j in range(n+1):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==s2[j-1]:
                dp[i][j]= 1+dp[i-1][j-1]
            else:
                dp[i][j]= 0+max(dp[i-1][j],dp[i][j-1])
    # return dp
    return dp[n][n]
s="bbabcbcab"
print(longestPalindromeSubsequence(s))


    
    

    