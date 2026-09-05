from mypkg import file_ops
from mypkg.text_ops import word_count
from mypkg import text_ops

text = file_ops.read_file('sample_speech.txt')
count = word_count(text)
top3 = text_ops.most_common_words(text, 3)

print(f"Word count: {count}")
print(f"Top 3 words: {top3}")

file_ops.write_file('summary.txt', f"Word count: {count}\nTop 3 words: {top3}\n")