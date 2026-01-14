import os

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def to_string(self):
        return f"{self.task_id}|{self.title}|{self.description}"

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.next_id = 1
        self.load_from_file()

    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                for t in self.tasks:
                    f.write(t.to_string() + "\n")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        t_id, title, desc = parts
                        self.tasks.append(Task(int(t_id), title, desc))
                        if int(t_id) >= self.next_id:
                            self.next_id = int(t_id) + 1
        except Exception as e:
            print(f"Error loading file: {e}")

    def create_task(self):
        task_id = self.next_id
        title = input("Enter Task Title: ")
        description = input("Enter Task Description: ")
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        self.next_id += 1
        self.save_to_file()
        print(f"Task added and saved with ID: {task_id}!")

    def read_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print("\n--- Current Task List (Loaded from File) ---")
        for t in self.tasks:
            print(f"ID: {t.task_id} | Title: {t.title} | Desc: {t.description}")

    def update_task(self):
        self.read_tasks()
        if self.tasks:
            try:
                t_id = int(input("\nEnter Task ID to update: "))
                for t in self.tasks:
                    if t.task_id == t_id:
                        t.title = input("Enter new title: ")
                        t.description = input("Enter new description: ")
                        self.save_to_file()
                        print("Task updated and saved!")
                        return
                print("Task ID not found.")
            except ValueError:
                print("Invalid input.")

    def delete_task(self):
        self.read_tasks()
        if self.tasks:
            try:
                t_id = int(input("\nEnter Task ID to delete: "))
                for i, t in enumerate(self.tasks):
                    if t.task_id == t_id:
                        del self.tasks[i]
                        self.save_to_file()
                        print("Task deleted from file.")
                        return
                print("Task ID not found.")
            except ValueError:
                print("Invalid input.")

def main():
    manager = TaskManager()
    while True:
        print("\n--- Advanced Task Manager (Persistent) ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose (1-5): ")
        if choice == '1': manager.create_task()
        elif choice == '2': manager.read_tasks()
        elif choice == '3': manager.update_task()
        elif choice == '4': manager.delete_task()
        elif choice == '5': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()