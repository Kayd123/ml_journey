from collections import Counter
import string

def read_file(filename: str) -> str:
    """Read text from file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def clean_text(text: str) -> str:
    """Lowercase text and remove punctuation + spaces."""
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove spaces and newlines
    text = text.replace(" ", "").replace("\n", "")
    return text

def char_count(text: str) -> dict[str, int]:
    """Count character frequency using Counter."""
    return dict(Counter(text))

def print_top_chars(char_freq: dict[str, int], n: int = 10) -> None:
    """Print top n most frequent words."""
    for char, freq in Counter(char_freq).most_common(n): #Sorts by highest frequency.
        print(f"{char}: {freq}") #Prints top n words (default = 10).
if __name__ == "__main__":
    filepath = "sample.txt"
    text = read_file(filepath)
    cleaned = clean_text(text)
    freq = char_count(cleaned)
    print_top_chars(freq, 10)