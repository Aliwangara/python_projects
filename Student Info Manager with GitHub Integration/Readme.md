Project: Student Info Manager with GitHub Integration
🎯 Goal:

Build a console-based program that manages student records locally (using files + JSON) and can fetch GitHub info for each student.

🧱 Functional Requirements (step-by-step clues)
1️⃣ Data structure & input

Ask the user how many students they want to register.

For each student, collect:

Full name

Age

Email

GitHub username

Skills (comma-separated string → convert to list)

Store each student as a dictionary, and all of them in a list.

2️⃣ File handling (JSON)

Save all student records to a JSON file named students.json.

Load and display the data neatly after saving.

3️⃣ Object-Oriented Programming

Create a class Student with attributes: name, age, email, skills, github_username.

Include methods:

display_info() → prints formatted info

to_dict() → returns dictionary version for JSON storage

4️⃣ Exception Handling

Handle invalid input (like non-numeric age or blank name).

Handle JSON file errors (file missing, decoding issues).

Handle network errors when fetching GitHub data.

5️⃣ Using Built-in Modules

Use:

datetime → show when data was saved.

os → check if students.json exists before reading/writing.

6️⃣ API Integration

For each student with a GitHub username:

Fetch their name, public repos, followers, and profile URL from the GitHub API.

Merge this info into their record.

Save the updated data back to students.json.

7️⃣ Program Structure (Modularization)

Organize your code:

project/
    main.py
    student.py
    utils/
        __init__.py
        file_tools.py
        github_tools.py


student.py → define the Student class

file_tools.py → handle saving/loading JSON

github_tools.py → fetch GitHub data

main.py → orchestrates everything (user input, display, etc.)

8️⃣ Final Output

When run, the program should:

Ask for student data.

Save to JSON.

Load and display all data (including GitHub details).

Print "Data saved on <date/time>".

🌟 Bonus ideas (optional, for extra challenge)

Add a search feature: enter a name → display that student’s info.

Sort students by number of GitHub followers (use sorted()).

Allow deleting a student and updating their info.