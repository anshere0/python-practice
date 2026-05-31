#todo program written in python
import os
import pickle
from datetime import datetime

#initialize an empty list to store our items
todo=[]
#defining the filenameto store todo
todo_file= "todo.pkl"
#define a class to represent each todo item

class task():
    def __init__(self, title, created_at, is_completed=False):
        self.title= title
        self.created_at= created_at
        self.is_completed= is_completed

#function to save todo to our pickle file
def save_to_file():
    with open(todo_file, "wb") as file:
        pickle.dump(todo, file)
    

#function to read todo from the picle file
def read_from_file():
    global todo
    try:
        with open(todo_file, "rb") as file:
            todo= pickle.load(file)
    except FileNotFoundError:
        todo=[]


#function to add a new todo
def add_todo():
    #prompt the user to enter a task
    title=input('type your todo: ')
    #formatting the date and time
    created_at= datetime.now().strftime("%d/%m %H:%M")
    #create the todo object
    new_todo=task(title, created_at)
    #add a new todo to list
    todo.append(new_todo)
    #this is to reserved to add the pickle item
    save_to_file()

#function to print all todo
def print_all_todo():
    print("+---+--------------------------------------+------------+-------------------+")
    print("|ID |          TODO TITLE                  | Created at |     Completed     | ")
    print("+---+--------------------------------------+------------+-------------------+")

    #iterate through todos and print each todo item
    for i, todo in enumerate(todo):
        print(f"|{i+1:2} | {todo.title:35} | {todo.created_at:12} | {'✅' if todo.is_completed else '❌ ' :^11} |")

#function to mark todo as complete
def mark_as_complete():
    try:
        print_all_todo()
        todo_id= input ('enter the id to the todo:')-1
        todo[todo_id].is_completed= True

#save to pickle file
        save_to_file()
    except IndexError:
        print("Invalid todo ID")
    except ValueError:
        print("Invalid input. Please enter a number.")

#function that deletes a todo
def delete_todo():
    try:
        print_all_todo()
        todo_id= int(input('enter the id to delete the todo: '))-1
        del todo[todo_id]
    except IndexError:
        print("Invalid todo ID")
    except ValueError:
        print("Invalid input. Please enter a number.")

#function to show options to the user
def show_options():
    while True:
        print ("welcome to taskmaster!")
        user_choice= input("type 'A' to add, 'D' to delete, 'C'to mark as complete, 'V'to view all todos, 'Q'to quit: ").upper()
        if user_choice== 'A' :
            add_todo()
        elif user_choice== 'D':
            delete_todo()  
        elif user_choice== 'C':
            mark_as_complete()     
        elif user_choice== 'Q':
            print("thank you for using taskmaster.")
            break 
        else: 
            print("command not found")
        print_all_todo()


#function to check if this is the first time the program is run
def is_this_your_first_time():
    if os.path.exists(todo_file):
        read_from_file()
        print_all_todo()
    else:
        print("welcome to taskmaster!")
        add_todo()
        print_all_todo()


if __name__== "__main__":
 #clearing the console
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\003[32;1m") #green text]")
    is_this_your_first_time() 
    show_options()



