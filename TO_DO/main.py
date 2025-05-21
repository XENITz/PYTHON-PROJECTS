import os
#OPEN THE FILE AND LOAD THE DICTIONARY
with open("tasks.txt", "r") as f:
    file_content = f.read().strip()
    if not file_content:
        task_dict = {}
    else: 
        task_dict = eval(file_content)

"""CLEAR THE CLI"""
def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

"""ADD TASKS TO THE DICTIONARY"""
def add_task():
    print("====ADD TASK====")
   #LET USER ADD TASKS AND DESCRIPTION 
    while True:
        task = input("PLEASE ADD THE TASK: ")
        description = input("PLEASE ADD THE DESCRIPTION: ")
    
        #ADD TASKS AND DESCRIPTION TO DICTIONARY
        tasks = {"description": description,
                 "status": False}
        task_dict[task] = tasks
        print(f"TASK: {task} - {description}")
        print("TASK ADDED SUCCESSFULLY")
    
        #ASK USER IF THEY WANT TO ADD ANOTHER TASK
        add_another = input("DO YOU WANT TO ADD ANOTHER TASK? (Y/N): ")

    #IF USER WANTS TO ADD ANOTHER TASK, CALL THE FUNCTION AGAIN
        if add_another.upper() != "Y":
            print("TASKS SAVED SUCCESSFULLY")
            break
        else:
            continue

"""VIEW TASKS FROM THE DICTIONARY"""
def view_tasks():
    #PARSE THE TASKS FROM THE DICTIONARY
    print("====TASKS====")
    for index, value in enumerate(task_dict):
        if task_dict[value]["status"] == True:
            print(f"{index + 1}. [x] {value} - {task_dict[value]['description']}")
        else:
            print(f"{index + 1}. [ ] {value} - {task_dict[value]['description']}")

"""MARK TASKS AS COMPLETED"""
def mark_task():
    
    #PARSE THE TASKS FROM THE DICTIONARY
    print("====TASKS====")
    for index, value in enumerate(task_dict):
        if task_dict[value]["status"] == True:
            print(f"{index + 1}. [X] {value}")
        else:
            print(f"{index + 1}. [ ] {value}")
        
    #ASK USER WHICH TASK TO MARK AS COMPLETED
    task_to_mark = int(input("PLEASE ENTER THE TASK NUMBER TO MARK AS COMPLETED: "))
    task_dict[task_to_mark - 1]["status"] = True
    print(f"TASK: {task_to_mark} - [X]")

"""DELETE TASKS FROM THE DICTIONARY"""
def delete_task(task):
    #PARSE THE TASKS FROM THE DICTIONARY
    print("====TASKS====")
    for index, value in enumarate(task_dict):
        if task_dict[value]["status"] == True:
            print(f"{index + 1}. [X] {value}")
        else:
            print(f"{index + 1}. [ ] {value}")

    #ASK USER WHICH TASK TO DELETE
    task_to_delete = int(input("PLEASE ENTER THE TASK NUMBER TO DELETE: "))
    del task_dict[task_to_delete - 1]
    print("TASK DELETED SUCCESSFULLY")

                  
"""EXIT THE APPLICATION"""
def exit():
    print("THANK YOU FOR USING THE TO-DO APP/n EXITING...")
    
    #SAVE THE DICTIONARY TO A FILE
    with open("tasks.txt", "w") as f:
        f.write(str(task_dict))

"""MAIN FUNCTION"""
def main():
    print("====TO DO LIST====")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. MARK TASK AS COMPLETED")
    print("4. DELETE TASK")
    print("5. EXIT")
    choice = input("PLEASE ENTER YOUR CHOICE: ")
    
    clear_cli()
    
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


