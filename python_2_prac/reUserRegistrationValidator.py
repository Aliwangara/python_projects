import re

email_input = input("Enter Email:  ")
phone_input = input("Enter phone number: ")
password_input = input("Enter password:  ")

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
phone_pattern = r'^(07|01)\d{8}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

valid = True


if not re.match(email_pattern,email_input):
    print("❌ Invalid email format.")
    valid = False
if not re.match(phone_pattern,phone_input):
    print("❌ Invalid phone number. Use format like 0712345678 or 0112345678.")
    valid = False
if not re.match(password_pattern,password_input):
    print("❌ Weak password! Must contain:")
    print("   - At least 8 characters")
    print("   - One uppercase, one lowercase, one number, one special character")
    valid = False
if valid:
    print("✅ Registration Successful!")
else:
    print("⚠️ Please correct the above errors.")
