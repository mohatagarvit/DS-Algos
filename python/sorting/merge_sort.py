def merge_sort(a, start, end):
    if start < end:
        mid = (start + end)//2
        merge_sort(a, start, mid)
        merge_sort(a, mid+1, end)
        merge(a, start, mid, end)
    return

def merge(a,p,q,r):
    l = a[p:q+1]
    m = a[q+1:r+1]
    l.append(float('inf'))
    m.append(float('inf'))
    i,j = 0,0
    for s in range(r-p+1):
        if l[i] > m[j]:
            a[p+s] = m[j]
            j+=1
        else:
            a[p+s] = l[i]
            i+=1
    return

n = int(input())
a = list(map(int, input().strip().split()))
merge_sort(a,0,len(a)-1)
print(a)
