import json
import os

def store_memory(task, result):
    memory_file = "memory.log"
    data = {"task": task, "result": result}
    with open(memory_file, "a") as f:
        f.write(json.dumps(data) + "\n")

def get_memory():
    memory_file = "memory.log"
    if not os.path.exists(memory_file):
        return []
    with open(memory_file, "r") as f:
        lines = f.readlines()
        return [json.loads(line) for line in lines if line.strip()]
