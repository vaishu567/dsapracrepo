def wordladder2(begin,end,worddict):
    s=set(worddict)
    to_visit=[[begin]]
    # for every level we will keep how many strings has been used:
    usedOnlevel=[begin]
    level=0
    ans=[]
    while to_visit:
        vec=to_visit.pop(0)
        # erase all the words that have been previously used:
        if len(vec)>level:
            level+=1
            for it in usedOnlevel:
                s.discard(it)
        word=vec[-1]
        if word==end:
            if not ans:
                ans.append(list(vec))
            elif len(ans[0])==len(vec):
                ans.append(list(vec))
        for i in range(len(word)):
            for j in range(ord('a'), ord('z') + 1):
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word in s:
                    vec.append(new_word)
                    to_visit.append(list(vec))
                    usedOnlevel.append(new_word)
                    vec.pop()
    return ans

startWord = "der"
targetWord = "dfs"
wordList = ["des","der","dfr","dgt","dfs"]
print(wordladder2(startWord, targetWord, wordList))



# from collections import deque

# class Solution:
#     def findSequences(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         # Push all values of wordList into a set
#         # to make deletion from it easier and in less time complexity.
#         st = set(wordList)
        
#         # Creating a queue ds which stores the words in a sequence which is
#         # required to reach the targetWord after successive transformations.
#         q = deque()

#         # BFS traversal with pushing the new formed sequence in queue 
#         # when after a transformation, a word is found in wordList.

#         q.append([beginWord])

#         # A list defined to store the words being currently used
#         # on a level during BFS.
#         used_on_level = [beginWord]
#         level = 0
       
#         # A list to store the resultant transformation sequence.
#         ans = []
#         while q:
#             vec = q.popleft()

#             # Now, erase all words that have been
#             # used in the previous levels to transform
#             if len(vec) > level:
#                 level += 1
#                 for it in used_on_level:
#                     st.discard(it)

#             word = vec[-1]

#             # store the answers if the end word matches with targetWord.
#             if word == endWord:
#                 # the first sequence where we reached end
#                 if not ans:
#                     ans.append(vec)
#                 elif len(ans[0]) == len(vec):
#                     ans.append(vec)

#             for i in range(len(word)):
#                 # Now, replace each character of ‘word’ with char
#                 # from a-z then check if ‘word’ exists in wordList.
#                 original = word[i]
#                 for c in 'abcdefghijklmnopqrstuvwxyz':
#                     word = word[:i] + c + word[i+1:]
#                     if word in st:
#                         # Check if the word is present in the wordList and
#                         # push the word along with the new sequence in the queue.
#                         vec.append(word)
#                         q.append(vec.copy())
#                         # mark as visited on the level
#                         used_on_level.append(word)
#                         vec.pop()

#                 word = word[:i] + original + word[i+1:]

#         return ans
