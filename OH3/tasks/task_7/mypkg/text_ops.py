import re
from collections import Counter

def _tokenize(text):
    return re.findall(r"[a-z0-9']+", text.lower())
 
def word_count(text):
    return len(_tokenize(text))
 
def most_common_words(text, n):
    counts = Counter(_tokenize(text))
    return counts.most_common(n)