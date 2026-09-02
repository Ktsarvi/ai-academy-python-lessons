import reader
import analyzer
import writer

text = reader.read_file('sample_speech.txt')
top_words = analyzer.word_frequency(text, 5)
sentences = analyzer.sentence_count(text)

results = {"Top 5 words": top_words, "Sentence count": sentences}

writer.save_report("report.txt", "Speech Analysis Report", results)

print(f"Top 5 words: {top_words}")
print(f"Sentence count: {sentences}")