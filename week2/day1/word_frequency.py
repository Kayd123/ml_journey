from collections import Counter #count like words
import string #access all punctuation

def read_file(filename:str)->str:  #opens the file sample.txt
    """Read text from a file and return it as a string"""
    with open(filename, "r", encoding="utf-8") as f:#reads the entire content as a string
        return f.read() #returns the text

def clean_text(text: str) -> list[str]:
    """Lowercase text, remove punctuation, and split into words."""
    text = text.lower()  #makes every text lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  #removes punctuation
    words = text.split()  #splits into words
    return words
def word_count(words: list[str]) -> dict[str, int]: #Takes the list of words.
    """Count word frequency using Counter."""
    return dict(Counter(words)) #Uses Counter to count each word’s frequency. Converts result to a dictionary.
def print_top_words(word_freq: dict[str, int], n: int = 10) -> None:
    """Print top n most frequent words."""
    for word, freq in Counter(word_freq).most_common(n): #Sorts by highest frequency.
        print(f"{word}: {freq}") #Prints top n words (default = 10).
if __name__ == "__main__":
    filepath = "sample.txt"
    text = read_file(filepath)
    words = clean_text(text)
    freq = word_count(words)
    print_top_words(freq, 10)

