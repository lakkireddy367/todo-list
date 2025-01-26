def main():
    import todo, sys
print("hi")

obj = todo.Tasks()
options = [sys.exit, obj.add_tasks, obj.show_tasks, obj.edit_tasks, obj.mark_task, obj.unmark_task, obj.update_progression, obj.remove_Task, obj.remove_all_tasks]
main_display = '''
======Welcome to To-Do list=======
0. Exit
1. Add Tasks
2. Show Tasks
3. Edit Tasks
4. Mark Task as Completed
5. Unmark Task as Completed
6. Update Progression
7. Remove Task
8. Remove All Tasks
'''
option = 123
while (option!=0):
    print(main_display)
    option = int(input("Enter the option that you would like to perform:\n"))
    if option>=len(options) :
        print("Invalid option, Kindly retry.")
    else :
        options[option]()