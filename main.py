# main.py
import openai
from data_preprocessing import preprocess_lecture_notes, preprocess_llm_table
from embedding_generation import generate_embeddings
from vector_indexing import index_embeddings
from query_handling import process_query
from citing_references import cite_references

def main():
    # Set API Key
    openai.api_key = "your-openai-api-key"
    
    # Preprocess data
    lecture_notes_path = "path_to_lecture_notes.txt"
    llm_table_path = "path_to_llm_table.csv"
    
    segmented_notes = preprocess_lecture_notes(lecture_notes_path)
    indexed_llm_table = preprocess_llm_table(llm_table_path)
    
    text_segments = segmented_notes + indexed_llm_table
    
    # Generate embeddings
    embeddings = generate_embeddings(text_segments)
    
    # Index embeddings
    index = index_embeddings(embeddings)
    
    # Handle query
    query = "What are some milestone model architectures and papers in the last few years?"
    answer = process_query(query, index, embeddings, text_segments)
    
    # Cite references
    relevant_segments = ["Some milestone model architectures include the Transformer (Vaswani et al., 2017) and BERT (Devlin et al., 2018)."]  # Example
    citations = cite_references(relevant_segments)
    
    # Print the answer and references
    print("Answer:", answer)
    print("References:", citations)

if __name__ == "__main__":
    main()
