'''Write a Python program to find the common elements between
two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
Sample output: [4, 5]'''
l1=[1,2,3,4]
l2=[2,3]
l3=[]
common_elements=[element for element in l1 if element in l2]
print(common_elements)