#

def index_embeddings(embeddings):
    # Use FAISS or Pinecone to store embeddings
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index


if __name__ == "__main__":
    embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    index = index_embeddings(embeddings)
    print("FAISS Index:", index)