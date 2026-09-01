from pathlib import Path
import text_utils

file_path = Path(__file__).parent / "sample_speech.txt"

words = text_utils.count_words(file_path)
lines = text_utils.count_lines(file_path)
top5 = text_utils.most_common_words(file_path, 5)

print(f"Words: {words}")
print(f"Lines: {lines}")
print(f"Top 5: {top5}")