'''Create a function that takes a list and returns a new list with
unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]'''

def newlist(list1):
    l2=[]
    for element in list1:
        if element not in l2:
            l2.append(element)
    return l2
l1=[1,1, 2, 2, 3, 4, 4, 5, 5]
result= newlist(l1)
print(result)