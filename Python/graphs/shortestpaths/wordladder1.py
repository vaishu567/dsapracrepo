def wordladder(begin,end,worddict):
    # Write your code here
    s = set(worddict)
    to_visit = []
    to_visit.append([begin, 1])
    s.discard(begin)
    while to_visit:
        word, d = to_visit.pop(0)
        if word == end:
            return d
        for i in range(len(word)):
            for j in range(ord('a'), ord('z') + 1):
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word in s:
                    s.discard(new_word)
                    to_visit.append([new_word, d + 1])
    
    return -1


                