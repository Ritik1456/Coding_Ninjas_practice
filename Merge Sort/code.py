def mergeSort(arr):
    l = len(arr)
    if l==0 or l ==1:
        return arr
    
    mid = l//2
    S1 = mergeSort(arr[:mid])
    S2 = mergeSort(arr[mid:])
    i,j,k = 0,0,0
    while i < len(S1) and j <len(S2):
        if S1[i]<S2[j]:
            arr[k] = S1[i]
            i+=1
            k+=1
        else:
            arr[k] = S2[j]
            j+=1
            k+=1
    # print(len(arr),i,j)
    while i <len(S1):
        arr[k:] = S1[i:]
        i+=1
        k+=1

    while j <len(S2):
        arr[k:] = S2[j:]
        j+=1
        k+=1
    return arr

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)