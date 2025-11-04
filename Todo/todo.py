import sys

class todoList():
    def __init__(self):
        self.task={}

    def addTask(self):
      i=1
      while True:
        print("Please enter the task")
        taskName=str(input()).strip()
        if taskName=="":
            print("Task name cannot be empty. Please try again.")
            sys.exit()
        self.task[i]=taskName
        i+=1
        print("Task added successfully.")
        print("Do you want to add another task? (y/n)")
        choice=str(input()).strip().lower()
        if choice=='n':
            print()
            self.viewTasks()
            print()
            break

    def viewTasks(self):
      if not self.task:
        print("No tasks found.")
        sys.exit()
      else:
        print("Your tasks are:")
        for index, fruit in enumerate(self.task.values(),start=1):
          print(f"{index}.{fruit}")
        print()
    
    def deleteTask(self):
      print("Enter the task number you want to delete:")
      taskToDelete=int(input())
      if taskToDelete in self.task:
        del self.task[taskToDelete]
        print("Task deleted successfully.")
        self.reorder()
      else:
        print("Task not found.")

    def reorder(self):
      self.task = {i + 1: task for i, task in enumerate(self.task.values())}
      print("Tasks reordered.")


if __name__ == "__main__":
    print("Todo List")
    todo=todoList()
    while True:
      print("1.Add Task")
      print("2.View Tasks")
      print("3.Delete Task")
      print("4.Exit")
      no=int(input("Enter your choice: "))
      if no==4:
          sys.exit()
      elif no==1:
          todo.addTask()
      elif no==2:
          todo.viewTasks()
      elif no==3:
          todo.deleteTask()
      else:
          print("Invalid choice. Please try again.")