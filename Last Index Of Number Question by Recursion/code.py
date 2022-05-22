N = int(input())
arr = [int(i) for i in input().split()]
x = int(input())
def last_index(arr,x,si):
    if si== len(arr):
        return -1

    index = last_index(arr,x,si+1)
	
    if index == -1:
        if arr[si] ==x:
            return si
    return index
    
print(last_index(arr,x,0))