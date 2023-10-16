'''Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.'''

user={"daddy":"111","ammy":"777","santosh": "111"}
attempts=0
def login(userid,password):
    if userid in user and user[userid]==password:
        return True
    return False
while attempts<3:
        userid=input("Enter the user name")
        password=input("Enter the password")
        if login(userid,password):
            print("Login successful") 
        break
else:
        print("Incorrect id or password try again")
        attempts+=1
if attempts==3:
        print("Sorry, You have exceeded the limit")