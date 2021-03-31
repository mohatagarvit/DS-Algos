def insertion_sort(a, reverse=False):
    for i in range(len(a)-1):
        for j in range(0,i+1):
            if a[i+1]>a[j] and not reverse:
                continue
            a[j],a[i+1] = a[i+1],a[j]
    return a

def insertion_reverse_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1):
            if a[i+1]>a[j]:
                a[i+1], a[j] = a[j],a[i+1]
    return a

def insertion_sort_recursive(a, n):
    """
    Insert Reecursively through linear or binary search
    """

    if n==0:
        return
    insertion_sort_recursive(a, n-1)
    # insert(a,n)
    binary_search_insert(a,n,a[n-1])
    return

def insert(a,n):
    for i in range(n-1):
        if a[n-1]<a[i]:
            a[n-1],a[i]=a[i],a[n-1]
    return    

def binary_search_insert(a,n,key):
    import math
    p=0
    r=n-1
    ind=None
    q=(p+r)//2
    # for i in range(int(math.log(n,2))+1):
    while p!=r: 
        q=(p+r)//2
        if a[q]==key:
            ind=q
            break
        elif a[q]<key:
            p=q#+1
        else:
            r=q
    if a[q]>=key:
        ind=q
    elif a[q]<key:
        ind=q+1
    for i in range(ind,len(a)):
        a[i],a[n-1]=a[n-1],a[i]



n =int(input())
a = list(map(int, input().strip().split()))
print(insertion_sort(a))
print('a',a)
print(insertion_sort(a, reverse =True))
print('a',a)
print(insertion_sort_recursive(a, n))
print('a',a)