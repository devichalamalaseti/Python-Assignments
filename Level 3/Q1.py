'''Read the doc.txt file using Python File handling concept and
return only the even length string from the file. Consider the
content of doc.txt as given below:
Hello I am a file
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present.'''

with open("doc.txt", "w") as file:
    file.write("Hello I am a file")
def readfile(filename):
    even_word=[]
    with open(filename,'r') as file:
        for line in file:
            words=line.split()
        for word in words:
            if len(word)%2==0:
                even_word.append(word)
                even_text=" ".join(even_word)
    return even_text
filename="doc.txt"
result=readfile(filename)
print(result)