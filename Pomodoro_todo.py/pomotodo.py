BOLD = '\033[1m'
ITALIC = '\033[3m'
END = '\033[0m'

class ToDoList:
    def __init__(self):
        self.tasks = []
    def addTask(self, task,
        priority, due_date{
            "task": task,
            "done": False,
        "priority": priority,
        "due_date": due_date
    }
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
        priority_order = {"4high": 1, "medium": 2, "low": 3, }
        return sorted(self.tasks, key=lambda t: priority_order.get(t["priority"], 4))
    def sort_by_date(self):
        return sorted(self.tasks, key=lambda t: (t["due_date"] is None, t["due_date"] or datetime.max))
    def pomodoro_timer(work_minutes=10,
        def timer_thread(minutes, label):
            for i in range(minutes * 60, 0, -1):
                mins, secs = divmod(i, 60)
                print(f"\r{label}: {mins:02d}:{secs:02d}", end="", flush=True)
                time.sleep(1)
            print(f"\n{label} finished!")
    print("Starting Pomodoro: Work session")
    timer_thread(work_minutes, "Work")
    print("Starting break")
    timer_thread(break_minutes, "Break")
    print("Continue Pomodoro: Work session")
    timer_thread(work_minutes, "Work")
    print("Continue Pomodoro: Work session")
    timer_thread(work_minutes, "Work")