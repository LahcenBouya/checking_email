import time



#checking the email
def check_email(user_email):
    """this function take the email and check it """
    if "@" and "." in user_email:
        return True
    else:
        return False

def answer_user(user_name, user_email):
    """this fuction take the validation and print it to user"""
    if check_email(user_email):
        print(f"User {user_name} with email '{user_email}' successfully added.")
    else:       
        print("invalid email format registration failed.")


#ask user 
user_name = input("Enter a user name: ")
user_email = input("Enter your email: ")

#user experience
time.sleep(2)
print("checking user name ......please wait")
time.sleep(3)
print("validating email adress ........please wait")
time.sleep(3)
answer_user(user_name, user_email)