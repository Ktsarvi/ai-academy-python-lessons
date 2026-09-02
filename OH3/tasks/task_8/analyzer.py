import re
from collections import Counter
 
def word_frequency(text, n=5):
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(n)
 
def sentence_count(text):
    parts = re.split(r'[.!?]+', text)
    return len([p for p in parts if p.strip()])