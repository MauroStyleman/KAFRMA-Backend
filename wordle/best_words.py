import os
import spacy


def load_words(filename="woorden_nl.txt"):
    with open(filename, "r") as file:
        words = [line.strip().lower() for line in file.readlines()]
    return words

nlp = spacy.load("nl_core_news_md")

def load_word_vectors(words):
    word_vectors = {}
    for word in words:
        word_vector = nlp(word)
        if word_vector.has_vector:
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

def process_wikipedia_texts(wikipedia_folder_path, words):
    texts = []
    for filename in os.listdir(wikipedia_folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(wikipedia_folder_path, filename), "r", encoding="utf-8") as file:
                texts.append(file.read())

    best_words = []
    for text in texts:
        best_match = find_best_context_match(text, words)
        best_words.append(best_match)

    return best_words

def save_best_words(best_words, output_file="best_5_letter_words_from_context.txt"):
    with open(output_file, 'w') as f:
        for word in best_words:
            f.write(f"{word}\n")
    print(f"Found and saved {len(best_words)} best words.")

if __name__ == "__main__":
    wikipedia_folder_path = "../data/locations/antwerp/wikipediaapi"

    words = load_words("woorden_nl.txt")

    best_words = process_wikipedia_texts(wikipedia_folder_path, words)

    save_best_words(best_words, "best_5_letter_words_from_context.txt")
