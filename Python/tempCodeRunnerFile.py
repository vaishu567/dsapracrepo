def noofchars(s,t):
    d=[0 for i in range(256)]
    for i in s:
        d[ord(i)]+=1
    return d[ord(t)]
s="vaishnavi$%%$@%%$^"
t='%'
print(noofchars(s,t))