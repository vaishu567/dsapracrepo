def wordladder2(begin,end,worddict):
    d={}
    d[begin]=1
    s=set(worddict)
    to_visit=[]
    to_visit.append(begin)
    while to_visit:
        word=to_visit.pop(0)
        for i in range(len(word)):
            for j in range(ord('a'),ord('z')+1):
                new_word=word[:i]+chr(j)+word[i+1:]
                if new_word in s and new_word!=word:
                    to_visit.append(new_word)
                    if new_word not in d:
                        d[new_word]=d[word]+1
    return d
begin="hit"
end="cog"
worddict=["hot","dot","dog","lot","log","cog"]
print(wordladder2(begin,end,worddict))