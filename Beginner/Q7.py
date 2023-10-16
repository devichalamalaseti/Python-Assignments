'''Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", string2 = "silent"
Output: True'''

def strings(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
s1=input("Enter the string1")
s2=input("Enter the string2")

result = strings(s1,s2)
print(result)
