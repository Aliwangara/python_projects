# Create a custom exception class called InvalidAgeError.

# Create a function register_user(name, age):

# If age < 18, raise InvalidAgeError("User must be 18 or older")

# Else print "User registered successfully!"
# Handle the exception with a friendly message.

class InvalidAgeError(Exception):
    pass

def register_user(name,age):
    if age < 18:
        raise InvalidAgeError("User must be 18 or older")
    else:
        print("User registered successfully!")

try:
    register_user("Ali",21)
except InvalidAgeError as e:
    print("⚠️", e)
else:
    print("user logged in")
finally:
    print("Thank you")