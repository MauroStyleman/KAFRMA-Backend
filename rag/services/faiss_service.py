import numpy as np
import faiss

from rag.models.config import Config


class FAISSService:
    def __init__(self, embedding_service, dimension=Config.FAISS_DIMENSION):
        self.embedding_service = embedding_service
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def build_index(self, chunks):
        self.chunks = chunks
        for chunk in chunks:
            embedding = self.embedding_service.embed_texts([chunk])[0]
            self.index.add(np.array([embedding]))

    def search(self, query, top_k=15):
        query_embedding = self.embedding_service.embed_texts([query])[0].reshape(1, -1)
        distances, ids = self.index.search(query_embedding, top_k)
        return [(self.chunks[i], distances[0][idx]) for idx, i in enumerate(ids[0])]
