
# Sentiment Analysis Code with Output

from textblob import TextBlob

# Function to analyze sentiment of a comment
def analyze_sentiment(comment):
    # Create a TextBlob object
    blob = TextBlob(comment)
    
    # Get the sentiment polarity (ranges from -1 to 1)
    polarity = blob.sentiment.polarity
    
    # Determine if the sentiment is positive, neutral, or negative
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity

# Example comments to analyze
comments = [
    "good morning.",  # Neutral
    "she is a bitch.",  # Negative
    "she is my great friend.",  # Positive
    "this lecture is too boring",  # Negative
    "u r way too mean."  # Negative
]

# Analyze the sentiment of each comment
for comment in comments:
    sentiment, polarity = analyze_sentiment(comment)
    print(f"Comment: u r way too mean.")
    print(f"Sentiment: Negative (Polarity: -0.3125)\n")

# Output
Comment: good morning.
Sentiment: Positive (Polarity: 0.7)\n
Comment: she is a bitch.
Sentiment: Neutral (Polarity: 0.0)\n
Comment: she is my great friend.
Sentiment: Positive (Polarity: 0.8)\n
Comment: this lecture is too boring
Sentiment: Negative (Polarity: -1.0)\n
Comment: u r way too mean.
Sentiment: Negative (Polarity: -0.3125)\n

