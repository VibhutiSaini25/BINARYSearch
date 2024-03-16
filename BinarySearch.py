#USING RECURSION

def BinarySearch(a,low,high,x):
    if(low>high):#BASE CONDITION
        return -1
    mid=int((low+high)/2)
    
    if(a[mid]==x):
        return mid
    elif(a[mid]<x):
        return BinarySearch(a,mid+1,high,x)
    elif(a[mid]>x):
        return BinarySearch(a,low,mid-1,x)


a = list(map(int,input().strip().split()))

l=0
h=len(a)-1
n=int(input())
print(BinarySearch(a,l,h,n))