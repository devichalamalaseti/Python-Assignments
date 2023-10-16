'''Write a program to construct a dictionary from the two lists
containing the names of students and their corresponding
subjects. The dictionary should map the students with their
respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]'''

students=["Sam", "Alice","Mona"]
subjects=["Commerce", "Science", "Computer"]
substud_dict={}
for i in range(len(students)):
    substud_dict[students[i]]=subjects[i]  
    #substud_dict.append(students[i]:subjects[i])
    #substud_dict[students[i]]=subjects[i]
#substud_dict={students[i]:subjects[i]}
print(substud_dict)