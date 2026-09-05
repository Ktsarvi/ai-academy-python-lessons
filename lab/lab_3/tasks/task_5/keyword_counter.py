import os

os.makedirs("reports", exist_ok=True)

python_counts = 0
js_counts = 0
java_counts = 0

with open("hacker_news_sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        headline = line.lower()

        if "python" in headline:
            python_counts += 1
        if "javascript" in headline:
            js_counts += 1
        if "java" in headline and "javascript" not in headline:
            java_counts += 1

summary_path = os.path.join("reports", "summary.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write(f"Python mentions: {python_counts}\n")
    f.write(f"JavaScript mentions: {js_counts}\n")
    f.write(f"Java-only mentions: {java_counts}\n")

print("Saved reports")