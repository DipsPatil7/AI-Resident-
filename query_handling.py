# query_handling.py

import openai
import numpy as np

def process_query(query, index, embeddings, text_segments):
    
    # Generate embedding for the query
    query_embedding = OpenAIEmbeddings.create_embedding(query)
    
    # Search for similar embeddings in the index
    query_embedding_np = np.array([query_embedding]).astype('float32')
    distances, indices = index.search(query_embedding_np, k=5)
    
    # Retrieve the most relevant text segments
    relevant_segments = [text_segments[i] for i in indices[0]]
    
    # Generate the answer using the relevant text segments
    answer = generate_answer(relevant_segments)
    return answer

def generate_answer(relevant_segments):
    
    context = " ".join(relevant_segments)
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=context,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    openai.api_key = "your-openai-api-key"
    text_segments = ["This is a test segment.", "Another test segment."]
    embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    index = index_embeddings(embeddings)
    query = "What is a test segment?"
    answer = process_query(query, index, embeddings, text_segments)
    print("Answer:", answer)
