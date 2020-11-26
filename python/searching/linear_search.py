def linear_search(a, key):
    for i in range(len(a)):
        if a[i]==key:
            return i
    if i==len(a):
        return None

n = int(input())
a = list(map(int, input().strip().split()))
v = int(input())
print(linear_search(a,v))