import os
import json
import ast
import time

"""HAY QUE CAMBIAR TODA LA LOGICA Y AGREGARLE UN ID A CADA TASK
    QUE HAY EN EL DICCIONARIO, DE OTRA MANERA NO FUNCIONARA"""

#OPEN THE FILE AND LOAD THE DICTIONARY
with open("tasks.txt", "r") as f:
    file_content = f.read().strip()
    if not file_content:
        task_dict = {}
    else: 
        task_dict = ast.literal_eval(file_content)
        
"""CLEAR THE CLI"""
def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

"""ADD TASKS TO THE DICTIONARY"""
def add_task():
    #LET USER ADD TASKS AND DESCRIPTION 
    print("====ADD TASK====")
    id = 1
    while True:
        
        
        task = input("PLEASE ADD THE TASK: ")
        description = input("PLEASE ADD THE DESCRIPTION: ")
        
        #ADD TASKS AND DESCRIPTION TO DICTIONARY
        tasks = {"task" : task,
                "description": description,
                "status": False}
        task_dict[id] = tasks
        print(f"TASK: {task} - {description}")
        print("TASK ADDED SUCCESSFULLY")
        
        print(task_dict)
        #ASK USER IF THEY WANT TO ADD ANOTHER TASK
        add_another = input("DO YOU WANT TO ADD ANOTHER TASK? (Y/N): ")
        id += 1
    #IF USER WANTS TO ADD ANOTHER TASK, CALL THE FUNCTION AGAIN
        if add_another.upper() != "Y":
            print("TASKS SAVED SUCCESSFULLY")
            break
        else:
            continue

"""VIEW TASKS FROM THE DICTIONARY"""
def view_tasks():
    #PARSE THE TASKS FROM THE DICTIONARY
    clear_cli()
    print("====TASKS====")
    for index, value in enumerate(task_dict):
        if task_dict[value]["status"] == True:
            print(f"{index + 1}. [x] {task_dict[value]['task']} - {task_dict[value]['description']}")
        else:
            print(f"{index + 1}. [ ] {task_dict[value]['task']} - {task_dict[value]['description']}")
    time.sleep(15)


"""MARK TASKS AS COMPLETED"""
def mark_task():
    
    #PARSE THE TASKS FROM THE DICTIONARY
    print("====TASKS====")
    for index, value in enumerate(task_dict):
        if task_dict[value]["status"] == True:
            print(f"{index + 1}. [x] {task_dict[value]['task']}")
        else:
            print(f"{index + 1}. [ ] {task_dict[value]['task']}")
        
    #ASK USER WHICH TASK TO MARK AS COMPLETED
    task_to_mark = int(input("PLEASE ENTER THE TASK NUMBER TO MARK AS COMPLETED: "))
    task_dict[task_to_mark]["status"] = True
    print(f"TASK: {task_dict[task_to_mark]["task"]} - [X]")

"""DELETE TASKS FROM THE DICTIONARY"""
def delete_task():
    #PARSE THE TASKS FROM THE DICTIONARY
    print("====TASKS====")
    while True:
        for index, value in enumerate(task_dict):
            if task_dict[value]["status"] == True:
                print(f"{index + 1}. [x] {task_dict[value]['task']}")
            else:
                print(f"{index + 1}. [ ] {task_dict[value]['task']}")

        #ASK USER WHICH TASK TO DELETE
        task_to_delete = int(input("PLEASE ENTER THE TASK NUMBER TO DELETE: "))
        del task_dict[task_to_delete]
        print("TASK DELETED SUCCESSFULLY")
        
        del_another = input("DO YOU WANT TO DELETE ANOTHER TASK? (Y/N): ")
        
        if del_another.upper() != "Y":
            break
        else:
            continue
    
"""EXIT THE APPLICATION"""
def exit():
    print("THANK YOU FOR USING THE TO-DO APP/n EXITING...")
    
    #SAVE THE DICTIONARY TO A FILE
    with open("tasks.txt", "w") as f:
        f.write(str(task_dict))

"""MAIN FUNCTION"""
def main():
    clear_cli()
    print("====TO DO LIST====")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. MARK TASK AS COMPLETED")
    print("4. DELETE TASK")
    print("5. EXIT")
    choice = input("PLEASE ENTER YOUR CHOICE: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        exit()
        return True
    else:
        print("INVALID CHOICE")
    
if __name__ == "__main__":
    while True:
        if main():
            break


