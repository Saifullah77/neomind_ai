def self_review(task, result):
    if "error" in result.lower():
        feedback = f"⚠️ Hmm... The result for '{task}' seems to have an issue."
    else:
        feedback = f"✅ Good job! The result for '{task}' looks fine."

    print(f"[REVIEW] {feedback}")
    return feedback
