def prefixsum(arr):
    s=0
    i=0
    '''Input
A = [1, 2, 3, 4, 5]

Output
[1, 3, 6, 10, 15]'''
    
    while i<len(arr):
        s=s+arr[i]
        arr[i]=s
        i+=1
        
    return arr

arr=list(map(int,input().split()))
print(prefixsum(arr))
