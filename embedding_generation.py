

from langchain.embeddings import OpenAIEmbeddings

def generate_embeddings(text_segments):
    # Use OpenAI's GPT-3 to generate embeddings for text segments
    embeddings = []
    for segment in text_segments:
        embedding = OpenAIEmbeddings.create_embedding(segment)
        embeddings.append(embedding)
    return embeddings
if __name__ == "__main__":
    text_segments = ["This is a test segment.", "Another test segment."]
    embeddings = generate_embeddings(text_segments)
    print("Generated Embeddings:", embeddings)