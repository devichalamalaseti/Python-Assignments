'''Write a program to count the lines in a file “demo.txt”'''
with open("demo.txt",'w') as file:
    file.write("Hello I am the Mac\n")
    file.write("I am writing a file\n")
    file.write("I have the Mac OS.\n")
    file.write("Start working with me.\n")
def demo(filename):  
    with open(filename,'r') as file:
        linecount=sum(1 for line in file)
        return linecount
filename="demo.txt"
result=demo(filename)
print("No of lines :",result)