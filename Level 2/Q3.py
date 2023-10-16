'''Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2'''

def pairsum(arr,k):
    sum=0
    N=len(arr)
    for i in range(N):
        for j in range(i+1,N):
            if arr[i]+arr[j]==k:
                sum+=1
    return sum
arr=[1,2,3,4,5]
k=6
result=pairsum(arr,k)
print(result)