import streamlit as st
from task_manager import generate_tasks
from memory import store_memory
from self_improve import self_review

st.title("🧠 NeoMind AI Task Agent")

user_input = st.text_input("Enter your goal or task", "")

if st.button("Generate & Process Tasks"):
    if user_input.strip():
        tasks = generate_tasks(user_input)
        for task in tasks:
            st.markdown(f"### 🛠️ Task: {task}")
            result = f"Result of {task}"  # Simulated result
            store_memory(task, result)
            self_review(task, result)
            st.success(f"✅ {task} completed!")
    else:
        st.warning("Please enter a task.")
