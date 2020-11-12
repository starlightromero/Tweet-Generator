"""Import rearrange_words."""
from quote import random_quote


def random_words(num_words, file):
    """Return a random sentence containing num_word from file."""
    word_set = set()
    with open(file, "r") as f:
        all_words = f.read().splitlines()
        while len(word_set) < int(num_words):
            new_word = random_quote(all_words)
            word_set.add(new_word)
    return " ".join(word_set)


if __name__ == "__main__":
    word_count = input("Enter the number of words you would like: ")
    words = random_words(word_count, "/usr/share/dict/words")
    print(words)
