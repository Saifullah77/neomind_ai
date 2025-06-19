def store_memory(task, result):
    with open("memory.log", "a", encoding="utf-8") as f:
        f.write(f"Task: {task} → Result: {result}\n")
