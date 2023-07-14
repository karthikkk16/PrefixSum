def prefixsum(arr):
    sum1=0
    i=0
    while i<len(arr):
        sum1=sum1+arr[i]
        arr[i]=sum1
        i+=1
        
    return arr
arr=list(map(int,input().split()))
print(prefixsum(arr))
