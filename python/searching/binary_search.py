# def binary_search(a, p,r, key):
# wrong implementation
#     k=None
#     if p<r:
#         q = (p+r)//2
#         k=None
#         k = binary_search(a,p,q,key)
#         k = binary_search(a,q+1,r,key)
        
#     else:
#         if key==a[p]:
#             k=p
#     # print(k)
#     return k

# def binary_search(a,key):
#     n=len(a)
#     p=0
#     r=n
#     while p!=r: 
#         q=(p+r)//2
#         if a[q]>key:
#             r=q
#         elif a[q]<key:
#             p=q
#         else:
#             return q
#         print(p,q,r)
#     if p==r:
#         if a[p]==key:
#             return p
#         else:
#             return None
def binary_search(a,key):
    p=0
    r=len(a)
    q=(p+r)//2
    import math
    n=len(a)
    for i in range(int(math.log(n,2)+1)):
        q=(p+r)//2
        if a[q]==key:
            return q
        elif a[q]>key:
            r=q
        else:
            p=q
    return None

def pairSum_x(a,x):
    n=len(a)
    for i in range(n):
        k=binary_search(a,x-a[i])
        if k is not None:
            break
    if k is not None:
        return [i,k]
    else:
        return None 
    

a=list(range(10))
s=binary_search(a,0)
print(a)
print(s)
print(pairSum_x(a,16))
