#password strength checker
#conditions: 8 digit (min), digit, uppercase, lowercase, special character

# re- module. belongs to pythons standard library
# a module is a single python file containing code/functiond whereas a library is a collection of modules


import re #regular expression (regex) module- used to search patterns inside text

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    # len is an inbuilt func that returns the lenth of the string
    

    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    # here any checks for ATLEAST one number. 
    # char.isdigit checks for number through the loop: "for char in password"- iterates one by one
    # not- bcs we only return weak pass if theres no digit in this case
    

    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    # isupper() checks if the character is in uppercase or not 
    # therefore if NONE is in uppercase- return weak
    

    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    # islower() checks for lowercase letters
    # there must be one in uppercase asw as lowercase. if not- weak.
    
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    # syntax: re.search(pattern, text)
    # if pattern found- true else false
    # [abc] means match either a, b or c. so above we have mentioned all the special characters and the RE checks for only one
    # r before the square bracket stands for RAW STRING- python leaves backslashes alone
    # common regex expressions: (when using raw string)
    #  | Regex | Meaning         |
    #  | ----- | --------------- |
    #  | `\d`  | digit           |
    #  | `\w`  | word character  |
    #  | `\s`  | whitespace      |
    #  | `.`   | any character   |
    #  | `*`   | repeat          |
    #  | `+`   | one or more     |
    #  | `[]`  | character group |

    
    return "Strong: Your password is secure!"




def password_checker():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        
        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break
        
        result = check_password_strength(password)
        print(result)




# Run the password checker
if __name__ == "__main__":
    password_checker()

# if __name__ == "__main__" is used to ensure that certain code runs only when the Python file is executed directly, and not when it is imported as a module into another file.