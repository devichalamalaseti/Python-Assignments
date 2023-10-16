'''Given an input string, write a function that returns the run
length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1'''

def encoding(stri):
    enc_str=""
    count=1
    for i in range(1,len(stri)):
        if stri[i]==stri[i-1]:
            count+=1
        else:
            enc_str+=stri[i-1]+str(count)
            count=1
            enc_str+=stri[-1]+str(count)
    return enc_str
stri="wwwwaaadebbbbbw"
enc_str=encoding(stri)
print(enc_str)