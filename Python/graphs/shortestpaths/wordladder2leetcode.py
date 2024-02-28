def dfs(begin,d,end,ans,seq):
    if end==begin:
        ans.append(list(seq[::-1]))
        return
    steps=d[end]
    sz=len(end)
    for i in range(sz):
        for j in range(ord('a'),ord('z')+1):
            new_word=end[:i]+chr(j)+end[i+1:]
            if new_word in d and (d[new_word]+1)==steps:
                seq.append(new_word)
                dfs(begin,d,new_word,ans,seq)
                seq.pop()
    return 


def wordladder2(begin, end, worddict):
    d = {}
    d[begin] = 1
    s = set(worddict)
    to_visit = []
    to_visit.append(begin)
    s.discard(begin)
    sz=len(begin)
    ans=[]
    while to_visit:
        word = to_visit.pop(0)
        if word==end:
            break
        for i in range(sz):
            for j in range(ord('a'), ord('z')+1):
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word != word and new_word in s:
                    to_visit.append(new_word)
                    s.discard(new_word)
                    if new_word not in d:
                        d[new_word] = d[word] + 1
    # step2: backtracking:
    if end in d:
        seq=[end]
        dfs(begin,d,end,ans,seq)
        return ans
    return []

begin="hit"
end="cog"
worddict=["hot","dot","dog","lot","log","cog"]
print(wordladder2(begin,end,worddict))



