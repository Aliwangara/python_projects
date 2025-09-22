

todo = []

def todo_list():
    todo_input = input("What do you want to do? ").capitalize()
    todo.append(todo_input)
    print(todo)
todo_list()