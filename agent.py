from task_manager import generate_tasks
from memory import store_memory
from self_improve import self_review
from tools.web_reader import search_web

def main():
    print("🧠 NeoMind AI Starting...")
    tasks = generate_tasks("Learn about Langchain and make a simple agent")
    for task in tasks:
        print(f"🛠️ Task: {task}")
        result_list = search_web(task)
        result = "\n".join(result_list)
        store_memory(task, result)
        self_review(task, result)
