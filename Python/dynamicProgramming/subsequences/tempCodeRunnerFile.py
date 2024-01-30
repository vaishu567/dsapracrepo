def imposter(n, arr):
    sumi=sum(arr)
    s=set(arr)
    ss=sum(s)
    return sumi-ss
print(imposter(8,[9,9,919,9,9,9,9,9]))