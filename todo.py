import os

class Task:
    def __init__(self, title, urgent, important):
        self.title = title
        self.urgent = urgent
        self.important = important
        self.completed = False

    def get_quadrant(self):
        if self.urgent and self.important:
            return "🔥 Q1: DO FIRST (Urgent & Important)"
        elif not self.urgent and self.important:
            return "📅 Q2: SCHEDULE (Important, Not Urgent)"
        elif self.urgent and not self.important:
            return "🤝 Q3: DELEGATE (Urgent, Not Important)"
        else:
            return "🗑️ Q4: ELIMINATE (Neither)"

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        print("\n--- Add New Task ---")
        title = input("What is the task? ")
        
        # Convert user input (y/n) to Boolean
        urgent = input("Is it urgent? (y/n): ").lower() == 'y'
        important = input("Is it important? (y/n): ").lower() == 'y'
        
        new_task = Task(title, urgent, important)
        self.tasks.append(new_task)
        print(f"✅ Task '{title}' added to {new_task.get_quadrant()}")

    def show_tasks(self):
        if not self.tasks:
            print("\nYour list is empty!")
            return

        print("\n--- YOUR SMART TO-DO LIST ---")
        # Sort tasks by quadrant before displaying
        for task in self.tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{status} {task.title}")
            print(f"    Priority: {task.get_quadrant()}")
        print("----------------------------")

def main():
    manager = TodoManager()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.show_tasks()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()