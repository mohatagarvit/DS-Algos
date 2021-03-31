def linear_search(a, key):
    for i in range(len(a)):
        if a[i]==key:
            return i
    if i==len(a):
        return None

def poly(a,x):
    n=len(a)
    import time
    t0=time.time()
    y=0
    for i in range(n-1,-1,-1):
        y=y*x+a[i]
    t1=time.time()
    print(t1-t0)
    print(y)
    t2=time.time()
    y=0
    for i in range(n):
        y+=a[i]*(x**i)
    t3=time.time()
    print(t3-t2)
    print(y)
n = int(input())
a = list(map(int, input().strip().split()))
v = int(input())
print(linear_search(a,v))
poly(a,2)