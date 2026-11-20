import re

POSITIVE = {"good", "clean", "healthy", "excellent", "improved", "safe"}
NEGATIVE = {"bad", "poor", "dirty", "unhealthy", "worse", "unsafe"}
NEGATORS = {"not", "never", "no"}

def sentiment_score(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    score = 0
    negate_next = False
    for word in words:
        if word in NEGATORS:
            negate_next = True
            continue
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if negate_next and value:
            value *= -1
            negate_next = False
        score += value
    label = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return score, label

def extractive_summary(text, k=2):
    sentences = [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]
    words = re.findall(r"[a-zA-Z]+", text.lower())
    stop = {"the", "a", "an", "and", "is", "are", "of", "to", "in", "for"}
    frequency = {}
    for word in words:
        if word not in stop:
            frequency[word] = frequency.get(word, 0) + 1
    ranked = sorted(
        enumerate(sentences),
        key=lambda item: (-sum(frequency.get(w, 0) for w in re.findall(r"[a-zA-Z]+", item[1].lower())), item[0])
    )
    chosen = sorted(index for index, _ in ranked[:k])
    return " ".join(sentences[index] for index in chosen)

def rule_chatbot(question):
    q = question.lower()
    if "pm2.5" in q or "pm25" in q:
        return "PM2.5 is a fine-particle air-quality measurement."
    if "station" in q:
        return "Please specify the monitoring station name."
    if "date" in q:
        return "Please provide a date in YYYY-MM-DD format."
    return "I can answer basic questions about PM2.5, stations, and dates."

sample = "The air quality is good and clean. The station recorded unhealthy pollution yesterday. Monitoring is important."
print("Sentiment:", sentiment_score(sample))
print("Summary:", extractive_summary(sample))
print("Chatbot:", rule_chatbot("What is PM2.5?"))
