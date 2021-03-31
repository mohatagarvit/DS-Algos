# class Solution:
#     # import List
#     def binary_search(self, a:List[int], key: int) -> List[int]:
#         p=0
#         r=len(a)-1
#         q=(p+r)//2
#         f=0
#         l=n-1
#         while p<r :
#             q=(p+r)//2
#             if a[q]==key:
#                 f,l=q,q
#                 break
# #                 if a[f]==key:
# #                     if q<f:
# #                         f=q
# #                         #sth p,r
                    
                        
# #                 elif a[l]==key and q>l:
# #                     l=q
#             elif a[q]>key:
#                 r=q
#             else:
#                 p=q
#         q1=q
#         q2=q
#         while p<q1:
#             q=(p+q1)//2
#             if a[q]==key:
#                 f=q
#             elif a[q]>key:
#                 q1=q
#             else:
#                 p=q
        
#         while q2<r:
#             q=(r+q2)//2
#             if a[q]==key:
#                 l=q
#             elif a[q]>key:
#                 r=q
#             else:
#                 q2=q
#         return [f,l]
                    
            
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         a=nums
#         key=target
#         print('aaya')
#         p=0
#         r=len(a)-1
#         q=(p+r)//2
#         f=0
#         l=len(a)-1
#         while p<r :
#             q=(p+r)//2
#             if a[q]==key:
#                 f,l=q,q
#                 break
# #                 if a[f]==key:
# #                     if q<f:
# #                         f=q
# #                         #sth p,r
                    
                        
# #                 elif a[l]==key and q>l:
# #                     l=q
#             elif a[q]>key:
#                 r=q
#             else:
#                 p=q
#         q1=q
#         q2=q
#         while p<q1:
#             q=(p+q1)//2
#             if a[q]==key:
#                 f=q
#             elif a[q]>key:
#                 q1=q
#             else:
#                 p=q
        
#         while q2<r:
#             q=(r+q2)//2
#             if a[q]==key:
#                 l=q
#             elif a[q]>key:
#                 r=q
#             else:
#                 q2=q
#         return [f,l]

def searchRange(nums, target):
    a=nums
    key=target
    p=0
    r=len(a)-1
    q=(p+r)//2
    f=0
    l=len(a)-1
    while p<r :
        q=(p+r)//2
        if a[q]==key:
            f,l=q,q
            break
#                 if a[f]==key:
#                     if q<f:
#                         f=q
#                         #sth p,r
                    
                        
#                 elif a[l]==key and q>l:
#                     l=q
        elif a[q]>key:
            r=q
        else:
            p=q
        print(p,q,r)
    q1=q
    q2=q
    import math
    for i in range(int(math.log(len(a),2))+1):
        q=(p+q1)//2
        if a[q]==key:
            f=q
            q1=q
            print(p,q,q1)
        elif a[q]>key:
            q1=q
        else:
            p=q
        
        
    for i in range(int(math.log(len(a),2))+1):
        q=(r+q2)//2
        if a[q]==key:
            l=q
            q2=l
        elif a[q]>key:
            r=q
        else:
            q2=q
        print(q2,q,r)
    return [f,l]

nums = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,8,8,8,8,8,8,8]
target = 8
print(searchRange(nums, target))