# chatbot/model.py

from sentence_transformers import SentenceTransformer
import numpy as np

# Load lightweight sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Labels for your chatbot intents
LABELS = ["greeting", "goodbye", "thanks", "hours", "services"]

def get_intent(user_input, labels=LABELS):
    """
    Returns the intent label with highest semantic similarity
    between user input and predefined labels.
    """
    # Get embeddings for user input + labels
    embeddings = model.encode([user_input] + labels)
    query_emb = embeddings[0]
    label_embs = embeddings[1:]

    # Compute cosine similarity
    sims = np.dot(label_embs, query_emb) / (np.linalg.norm(label_embs, axis=1) * np.linalg.norm(query_emb))

    # Return the label with highest similarity
    return labels[int(np.argmax(sims))]