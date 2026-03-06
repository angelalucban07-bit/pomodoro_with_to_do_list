import time
from datetime import datetime

BOLD = '\033[1m'
ITALIC = '\033[3m'
END = '\033[0m'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date):
        self.tasks.append({
            "task": task,
            "done": False,
            "priority": priority,
            "due_date": due_date
        })
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True

    def show_tasks(self, sorted_list=None):
        task_list = sorted_list if sorted_list else self.tasks
        for i, task in enumerate(task_list):
            status = "[DONE]" if task["done"] else "[PENDING]"
            due_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "No due date"
            print(f"{i}: {status} {task['task']} (Priority: {task['priority']}, Due: {due_str})")
    def get_pending_tasks(self):
        return [i for i, task in enumerate(self.tasks) if not task["done"]]
    def sort_by_priority(self):
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.tasks, key=lambda t: priority_order.get(t["priority"], 4))
    def sort_by_date(self):
        return sorted(self.tasks, key=lambda t: (t["due_date"] is None, t["due_date"] or datetime.max))
def pomodoro_timer(work_minutes=25, break_minutes=5): #itu rin po pwidi mo palitan if natatamad ka na sa 25 mins ok?
    def timer_thread(minutes, label):
        for i in range(minutes * 60, 0, -1):
            mins, secs = divmod(i, 60)
            print(f"\r{label}: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)
        print(f"\n{label} finished!")
        print("\a")
    print("Starting Pomodoro: Work session") #ikaw po bahala oki? dagdagan mo session if gustu mu pu matagal mag aral.
    timer_thread(work_minutes, "Work") #ito copy paste mo lang yan matik na yan ang layout niyan ay yung two lines ok? modify mo nalang if gustu mu
    print("Starting break")
    timer_thread(break_minutes, "Break")
    print("Continue Pomodoro: Work session")
    timer_thread(work_minutes, "Work")

def main():
    todo = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task done")
        print("3. Show tasks")
        print("4. Show tasks sorted by priority")
        print("5. Show tasks sorted by date")
        print("6. Start Pomodoro for a task")
        print("7. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            priority = input("Enter priority (high/medium/low): ").lower()
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ")
            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Using no due date.")
            todo.add_task(task, priority, due_date)
        elif choice == "2":
            todo.show_tasks()
            index = int(input("Enter task index to mark done: "))
            todo.mark_done(index)
        elif choice == "3":
            todo.show_tasks()
        elif choice == "4":
            sorted_tasks = todo.sort_by_priority()
            print("Tasks sorted by priority (high to low):")
            todo.show_tasks(sorted_tasks)
        elif choice == "5":
            sorted_tasks = todo.sort_by_date()
            print("Tasks sorted by due date (earliest first):")
            todo.show_tasks(sorted_tasks)
        elif choice == "6":
            pending = todo.get_pending_tasks()
            if not pending:
                print("No pending tasks.")
                continue
            print("Pending tasks:")
            for i in pending:
                task = todo.tasks[i]
                due_str = task["due_date"].strftime("%Y-%m-%d") if task["due_date"] else "No due date"
                print(f"{i}: {task['task']} (Priority: {task['priority']}, Due: {due_str})")
            index = int(input("Enter task index to start Pomodoro: "))
            if index in pending:
                pomodoro_timer()
            else:
                print("Invalid task.")
        elif choice == "7":
            print("Exiting... Thank you for using this system!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()