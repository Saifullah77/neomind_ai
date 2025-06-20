def self_review(task, result):
    print(f"🤖 Self-reviewing task: {task}")
    
    if "error" in result.lower() or "fail" in result.lower():
        print("⚠️ Improvement needed! Something might have gone wrong.")
    else:
        print("✅ Task looks good. No major issues found.")
