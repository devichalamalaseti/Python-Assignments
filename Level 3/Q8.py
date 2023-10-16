'''You need to write a function that accepts an encoded string as a
parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The
id is a numeric value but will contain no zeros. The function should
parse the string and return a Python dictionary that contains the
first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }'''
import re
def encoded(string):
            parts=re.split('0+',string)
            parts=[part for part in parts if part]
            if len(parts)>=3:
                first_name=parts[0]
                last_name=parts[1]
                id=parts[-1]

                result={"firstname":first_name,
                        "lastname":last_name,
                        "id":id}
                return result
            else:
                return None
string="Robert000Smith000123"
result=encoded(string)
print(result)