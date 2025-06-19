def self_review(task, result):
    print(f"🤔 Reviewing: {task}")
    if "error" in result.lower():
        print("⚠️ Found issue, retrying or changing plan...")
