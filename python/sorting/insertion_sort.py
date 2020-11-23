def insertion_sort(a):
    for i in range(len(a)-1):
        for j in range(0,i+1):
            if a[i+1]>a[j]:
                continue
            a[j],a[i+1] = a[i+1],a[j]
    return a

n =int(input())
a = list(map(int, input().strip().split()))
print(insertion_sort(a))
