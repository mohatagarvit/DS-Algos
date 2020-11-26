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

n =int(input())
a = list(map(int, input().strip().split()))
print(insertion_sort(a))
print(insertion_sort(a, reverse =True))