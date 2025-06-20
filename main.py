from task_manager import generate_tasks
from memory import store_memory, get_memory
from self_improve import self_review
import gradio as gr

# 🔹 Input process function
def process_input(goal):
    output = f"🎯 Goal: {goal}\n"
    tasks = generate_tasks(goal)

    for task in tasks:
        output += f"\n🛠️ Task: {task}"
        result = f"✅ Simulated result of '{task}'"
        output += f"\n{result}"

        store_memory(task, result)
        self_review(task, result)

    return output

# 🔹 Memory view function
def show_memory():
    memories = get_memory()
    if not memories:
        return "📭 No memory yet."
    return "\n\n".join([f"🧠 Task: {m['task']}\n✅ Result: {m['result']}" for m in memories])

# 🔹 Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 NeoMind: AI Task Agent")

    with gr.Row():
        user_input = gr.Textbox(label="Enter your Goal", placeholder="What should the agent do?")
        run_button = gr.Button("🚀 Process")

    output_box = gr.Textbox(label="AI Output", lines=10)

    run_button.click(fn=process_input, inputs=user_input, outputs=output_box)

    with gr.Row():
        show_mem_button = gr.Button("📂 Show Memory")
        mem_output = gr.Textbox(label="Memory", lines=10)

    show_mem_button.click(fn=show_memory, outputs=mem_output)

# 🔹 Launch
if __name__ == "__main__":
    demo.launch()
