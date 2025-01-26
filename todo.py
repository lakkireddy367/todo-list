class Tasks:
    def __init__(self):
        self.__tasks=[]
        self.progression=[]
    def add_tasks(self):
        print('====Add Tasks====')
        print("Enter 0 for exit or enter task name:\n")
        inp = input()
        while (inp!='0'):
            self.__tasks.append(inp)
            self.progression.append(0)
            inp = input()
        print("=== End of Add Tasks ===")

    def show_tasks(self, completed=None):
        print("===showing tasks=====")
        if (len(self.__tasks)==0):
            print("===No Tasks====")
            print("=== End of Showing Tasks ===")
            return
        print("S.No. Progress(\%)\tTask")
        for ind, task in enumerate(self.__tasks):
            print(f'{ind+1}.\t{self.progression[ind]}\t{task}')
        print("=== End of Showing Tasks ===")


    def edit_tasks(self):
        self.show_tasks()
        print("====Edit tasks====")
        ind = input("Enter the task number or 0 for exit:\n")
        while (ind != 0):
            if ind-1>len(self.__tasks):
                print('Number out of tasks')
            else :
                print(self.__tasks[ind-1])
                self.__tasks[ind-1]=input("Enter the task:\n")
                print(self.__tasks[ind-1])
            ind = input("Enter the task number or 0 for exit:\n")
        print("=== End of Edit tasks ===")

    def mark_task(self):
        self.show_tasks()
        print("=== Mark task as Done ===")
        ind = input("Enter the task number or 0 for exit:\n")
        while (ind!=0):
            if ind-1>len(self.__tasks):
                print('Number out of tasks')
            elif (self.progression[ind-1]=="Completed"):
                print("already marked", self.__tasks[ind-1])
            else :
                self.progression[ind-1]="Completed"
                print(self.__tasks[ind-1])
            ind = input("Enter the task number or 0 for exit:\n")
        self.show_tasks()
        print("=== End of Mark task as Done ===")
    
    def unmark_task(self):
        print("=== Unmark Tasks ===")
        self.show_tasks()
        ind = input("Enter the task number or 0 for exit:\n")
        while (ind!=0):
            if ind-1>len(self.__tasks):
                print('Number out of tasks')
            elif (self.progression[ind-1]=="Completed"):
                self.progression[ind-1]=0
            else :
                print(" already Not Marked")
                print(self.__tasks[ind-1])
            ind = input("Enter the task number or 0 for exit:\n")
        self.show_tasks()
        print("=== End of Mark task as Done ===")

    def update_progression(self):
        print("===Update Progress===")
        self.show_tasks()
        ind = input("Enter the task number or 0 for exit:\n")
        while (ind!=0):
            if ind-1>len(self.__tasks):
                print('Number out of tasks')
            else :
                print(self.__tasks[ind-1], self.progression[ind-1])
                self.progression[ind-1]=int(input("Enter progress:\n"))
                print(self.__tasks[ind-1], self.progression[ind-1])
            ind = input("Enter the task number or 0 for exit:\n")
        self.show_tasks()
        print("=== End of Update Progress ===")

    def remove_Task(self):
        print("=== Remove Tasks ===")
        self.show_tasks()
        ind = input("Enter the task number or 0 for exit:\n")
        while (ind!=0):
            if ind-1>len(self.__tasks):
                print('Number out of tasks')
            else :
                print(self.__tasks[ind-1], self.progression[ind-1])
                self.progression.pop([ind-1])
                self.__tasks.pop([ind-1])
                self.show_tasks()
            ind = input("Enter the task number or 0 for exit:\n")
        print("=== End of Update Progress ===")
    
    def remove_all_tasks(self):
        print("===removing tasks===")
        self.show_tasks()
        self.__tasks.clear()
        print("== removed tasks===")


