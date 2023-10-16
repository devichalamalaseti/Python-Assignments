'''Aditi has used text editing software to type some text. After
saving the article as words.txt, she realized that she had wrongly
typed the alphabet “J" instead of “I" everywhere in the article.
Write a function definition for JtoI() in Python that would display
the corrected version of the entire content of the file WORDS.TXT
with all the alphabet "J" to be displayed as an alphabet "I" on the
screen.
Note: Assume that words.txt does not contain any J alphabet
otherwise.'''
with open("words.txt",'w')as file:
    file.write("Hi I ate bread and Jam in Jamaica")
def JtoI(filename):
    with open(filename,'r') as file:
        text=file.read()
        correcttxt=text.replace('J','I')
        return correcttxt
result=JtoI('words.txt')
print(result)