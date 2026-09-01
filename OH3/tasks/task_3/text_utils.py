import re
from collections import Counter

def extract_words(text):
    return re.findall(r"[A-Za-z']+", text.lower())

def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = extract_words(text)

    return len(words)

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return len(lines)

def most_common_words(filename, n):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = extract_words(text)
    return Counter(words).most_common(n)