# for any character:
def noofchars(s,t):
    d=[0 for i in range(256)]
    for i in s:
        d[ord(i)]+=1
    return d[ord(t)]
s="vaishnavi$%%$@%%$^"
t='%'
print(noofchars(s,t))

# for lower case characters:
def nofchars(s,t):
    d=[0 for i in range(26)]
    for i in s:
        d[ord(i)-ord('a')]+=1
    return d[ord(t)-ord('a')]
s="vaishnavi"
t='v'
print(nofchars(s,t))