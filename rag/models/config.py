import os


class Config:
    FOLDER_PATH = os.path.abspath("data/locations/antwerp")
    CHUNK_SIZE = 3500
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    FAISS_DIMENSION = 384
