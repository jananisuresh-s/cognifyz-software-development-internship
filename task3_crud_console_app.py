class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1 

    def create_task(self):
        task_id = self.next_id
        title = input("Enter Task Title: ")
        description = input("Enter Task Description: ")
        
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        
        self.next_id += 1 
        print(f"Task '{title}' added successfully with ID: {task_id}!")

    def read_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print("\n--- Current Task List ---")
        for t in self.tasks:
            print(f"ID: {t.task_id} | Title: {t.title} | Desc: {t.description}")

    def update_task(self):
        self.read_tasks()
        if self.tasks:
            try:
                t_id = int(input("\nEnter the Task ID to update: "))
                for t in self.tasks:
                    if t.task_id == t_id:
                        t.title = input("Enter new title: ")
                        t.description = input("Enter new description: ")
                        print("Task updated!")
                        return
                print("Task ID not found.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def delete_task(self):
        self.read_tasks()
        if self.tasks:
            try:
                t_id = int(input("\nEnter the Task ID to delete: "))
                for i, t in enumerate(self.tasks):
                    if t.task_id == t_id:
                        del self.tasks[i]
                        print(f"Task '{t.title}' (ID: {t.task_id}) deleted successfully.")
                        return
                print("Task ID not found.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    manager = TaskManager()
    while True:
        print("\n--- Task Management System ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            manager.create_task()
        elif choice == '2':
            manager.read_tasks()
        elif choice == '3':
            manager.update_task()
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()