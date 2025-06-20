from task_manager import generate_tasks
from memory import store_memory
from self_improve import self_review

def process_input(user_input):
    tasks = generate_tasks(user_input)
    full_result = ""

    for task in tasks:
        result = f"Simulated result of '{task}'"
        feedback = self_review(task, result)
        store_memory(task, result)

        full_result += f"🛠️ {task}\n📌 {result}\n💬 {feedback}\n\n"

    return full_result
