import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class BaseFaissIndex:
    def __init__(self, similarity_threshold=0.9):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.dim = self.model.get_sentence_embedding_dimension()
        
        self.index = faiss.IndexFlatIP(self.dim)
        self.similarity_threshold = similarity_threshold
        
    def add_text(self, text):
        vec = self.model.encode([text], convert_to_numpy=True, normalize_embeddings=True).astype('float32')
        self.index.add(vec)
        
    def search_text(self, query, k=1):
        vec = self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True).astype('float32')
        D, I = self.index.search(vec, k)
        return np.any(D >= self.similarity_threshold)

    def save_index(self): 
        faiss.write_index(self.index, "vector_store.index")