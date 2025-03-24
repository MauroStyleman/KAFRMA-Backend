from pydantic import BaseModel
import spacy


def load_words(filename="wordle/best_5_letter_words_from_context.txt"):
    with open(filename, "r") as file:
        words = [line.strip().lower() for line in file.readlines()]
    return words


nlp = spacy.load("nl_core_news_md")


# Preload word vectors to speed up comparison
def load_word_vectors(words):
    word_vectors = {}
    for word in words:
        word_vector = nlp(word)
        if word_vector.has_vector:  # Ensure it has a vector
            word_vectors[word] = word_vector
    return word_vectors


def find_best_context_match(user_text, words):
    doc = nlp(user_text)

    word_vectors = load_word_vectors(words)

    best_match = None
    highest_similarity = 0

    for word, word_vector in word_vectors.items():
        similarity = doc.similarity(word_vector)
        if similarity > highest_similarity:
            best_match = word
            highest_similarity = similarity

    return best_match if best_match else "Geen goede match gevonden"

import os

def is_word_valid(word: str) -> bool:
    try:
        file_path = os.path.join(os.path.dirname(__file__), "woorden_nl.txt")
        with open(file_path, "r") as file:
            word = word.lower().strip()
            for line in file:
                if line.strip().lower() == word:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: file not found at {file_path}.")
        return False



class WordleInput(BaseModel):
    text: str
