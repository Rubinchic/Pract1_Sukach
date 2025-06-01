from collections import Counter

class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split()
        return len(words)

    def most_common_letter(self):
        letters = [c.lower() for c in self.text if c.isalpha()]
        if not letters:
            return None
        counter = Counter(letters)
        most_common = counter.most_common(1)[0]
        return most_common[0], most_common[1]
