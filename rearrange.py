"""Import libraries."""
import re
import random


def rearrange_words(sentence):
    """Return setence in a random order."""
    sentence_list = re.sub(r"[^\w\s]", "", sentence).lower().split(" ")
    random.shuffle(sentence_list)
    return " ".join(sentence_list)


if __name__ == "__main__":
    user_sentence = input("Enter a sentence to randomize: ")
    print(rearrange_words(user_sentence))
