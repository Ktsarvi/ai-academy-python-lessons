def save_report(filename, title, results):
    lines = [title, "=" * len(title), ""]
    for label, value in results.items():
        lines.append(f"{label}: {value}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")