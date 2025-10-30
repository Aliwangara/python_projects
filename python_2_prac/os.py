import os

print("Working directory", os.getcwd())

# print("create directory: ", os.mkdir("test_folder"))

# print("Items: ", os.listdir())

print("Folder Exists: ", os.path.exists("test_folder"))


# os.rmdir("test_folder") 

file_path = os.path.join("test_folder", "test_file")

with open (file_path, "w",newline="") as f:
    f.write("This is the summary report.")

print("📝 summary.txt created successfully inside 'reports' folder!")

print(os.path.abspath("test_file"))

os.rmdir("test_folder")
os.remove("test_file")