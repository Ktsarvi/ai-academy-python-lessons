
import text_utils

words = text_utils.count_words("sample_speech.txt")
lines = text_utils.count_lines("sample_speech.txt")
top5 = text_utils.most_common_words("sample_speech.txt", 5)

print(f"Words: {words}")
print(f"Lines: {lines}")
print(f"Top 5: {top5}")