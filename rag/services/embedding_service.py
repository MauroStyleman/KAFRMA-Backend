import numpy as np

from sentence_transformers import SentenceTransformer
from rag.models.config import Config


class EmbeddingService:
    def __init__(self, model_name=Config.EMBEDDING_MODEL):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        return np.array(self.model.encode(texts, convert_to_numpy=True))
