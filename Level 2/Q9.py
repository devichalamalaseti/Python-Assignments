'''Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.'''
def indexerror(list,index,operation):
    try:
        result=operation(list[index])
        return result
        #print("Operation result:",result)
    except:
        print("Index is out of the valid range")

list=[2,4,6,8,10,12]
index=1
operation=lambda a:a*2
result=indexerror(list,index,operation)
print("Result of the operation",result)