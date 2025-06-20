import openai

def process_task(task):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # বা gpt-4 যদি থাকে
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": f"Complete this task: {task}"}
        ]
    )
    return response.choices[0].message["content"]
