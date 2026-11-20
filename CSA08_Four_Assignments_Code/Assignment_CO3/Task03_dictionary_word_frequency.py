from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

result = frequencies(calls, STOP)
print("Word Frequencies:", result)
print("Top 3 Words:", top(result, 3))

complaints = {
    "Chennai": ["Seeds delayed", "Fertiliser problem"],
    "Madurai": ["Water shortage", "Crop damage"],
    "Salem": ["Seeds not received"]
}
print("District Complaints:")
for district, messages in complaints.items():
    print(district, ":", messages)
print("Counter:", Counter(result))
