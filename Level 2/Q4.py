'''Given an array of size N. The task is to rotate array by D elements
towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]'''

def rotateright(arr,k):
    A=len(arr)
    arr1=arr[A-k:]
    arr2=arr[:A-k]
    Ar=arr1+arr2
    return Ar
arr= [1,2,3,4,5]
k=2   
result=rotateright(arr,k)
print(result)