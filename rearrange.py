"""Import libraries."""
import re
import random


def rearrange_words():
    """Return user entered words in a random order."""
    user_sentence = input("Enter a sentence to randomize: ")
    sentence_list = re.sub(r"[^\w\s]", "", user_sentence).lower().split(" ")
    random.shuffle(sentence_list)
    return " ".join(sentence_list)


if __name__ == "__main__":
    print(rearrange_words())
