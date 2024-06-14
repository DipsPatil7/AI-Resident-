

def cite_references(relevant_segments):
    # Extract and cite the specific text segments used to generate the answer
    citations = "\n".join([f"- {segment}" for segment in relevant_segments])
    return citations
if __name__ == "__main__":
    relevant_segments = ["This is a test segment.", "Another test segment."]
    citations = cite_references(relevant_segments)
    print("Citations:", citations)