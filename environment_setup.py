# environment_setup.py

import openai
import faiss
import pinecone

# Set OpenAI API Key
openai.api_key = "your-openai-api-key"

# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key", environment="your-pinecone-environment")


