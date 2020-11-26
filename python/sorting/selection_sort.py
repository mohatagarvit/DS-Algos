def selection_sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

n = int(input())
a = list(map(int, input().strip().split()))
print(selection_sort(a))