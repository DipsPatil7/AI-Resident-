

import pandas as pd
import re

def preprocess_lecture_notes(file_path):
    
    with open(file_path, 'r') as file:
        content = file.read()

    # Split content into sections based on headings (e.g., "1. Introduction")
    sections = re.split(r'\n\d+\.\s', content)
    segmented_notes = []
    
    for section in sections:
        if section.strip():
            # Further split sections into subsections if needed
            subsections = re.split(r'\n\d+\.\d+\.\s', section)
            segmented_notes.extend(subsections)
    
    # Clean and filter out any empty sections
    segmented_notes = [note.strip() for note in segmented_notes if note.strip()]
    
    return segmented_notes

def preprocess_llm_table(file_path):
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Ensure the table is well-structured and indexed
    # Example structure: [Name, Year, Description]
    indexed_llm_table = []
    
    for _, row in df.iterrows():
        description = f"{row['Name']} ({row['Year']}): {row['Description']}"
        indexed_llm_table.append(description)
    
    return indexed_llm_table

# Example usage
if __name__ == "__main__":
    lecture_notes_path = "path_to_lecture_notes.txt"
    llm_table_path = "path_to_llm_table.csv"
    
    segmented_notes = preprocess_lecture_notes(lecture_notes_path)
    indexed_llm_table = preprocess_llm_table(llm_table_path)
    
    print("Segmented Lecture Notes:")
    for note in segmented_notes:
        print(note)
    
    print("\nIndexed LLM Table:")
    for llm in indexed_llm_table:
        print(llm)
