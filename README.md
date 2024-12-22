
# Sentiment Analysis Project

This project demonstrates a simple sentiment analysis using Python and the TextBlob library.

## Overview

The script analyzes the sentiment of given comments and categorizes them as Positive, Neutral, or Negative based on their sentiment polarity. Polarity ranges from -1 to 1:
- **Positive**: Polarity > 0
- **Neutral**: Polarity = 0
- **Negative**: Polarity < 0

## Features

- Sentiment analysis with sentiment polarity calculation.
- Easy-to-understand implementation using the TextBlob library.
- Example comments analyzed with output showcasing the results.

## Requirements

- Python 3.x
- `TextBlob` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Install the required dependencies:
   ```bash
   pip install textblob
   ```

3. Download the necessary corpora for TextBlob (if not already installed):
   ```bash
   python -m textblob.download_corpora
   ```

## Usage

1. Run the Python script:
   ```bash
   python sentiment_analysis_with_output.py
   ```

2. The script will output the sentiment and polarity for each comment.

## Example Output

```plaintext
Comment: good morning.
Sentiment: Neutral (Polarity: 0.0)

Comment: she is a bitch.
Sentiment: Negative (Polarity: -0.5)

Comment: she is my great friend.
Sentiment: Positive (Polarity: 0.4)

Comment: this lecture is too boring
Sentiment: Negative (Polarity: -0.6)

Comment: u r way too mean.
Sentiment: Negative (Polarity: -0.3)
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

Feel free to contribute to this project by submitting issues or pull requests!
