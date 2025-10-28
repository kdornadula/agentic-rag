# src/vectorstore.py

import os
import chromadb
import pandas as pd

# === Initialize ChromaDB persistent client ===
client = chromadb.PersistentClient(path="./chroma_db")

def create_collection_from_csv(csv_path: str, collection_name: str, text_column: str = None):
    """
    Create a ChromaDB collection from a CSV file.
    Args:
        csv_path: Path to CSV file
        collection_name: Name for the collection
        text_column: Column name containing combined text
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # Automatically combine columns if no combined text column given
    if text_column is None or text_column not in df.columns:
        df["combined_text"] = df.astype(str).agg(". ".join, axis=1)
        text_column = "combined_text"

    collection = client.get_or_create_collection(name=collection_name)

    collection.add(
        documents=df[text_column].tolist(),
        metadatas=df.to_dict(orient="records"),
        ids=df.index.astype(str).tolist()
    )

    print(f"✅ Added {len(df)} rows to collection: {collection_name}")
    return collection


def get_collection(name: str):
    """Retrieve an existing ChromaDB collection."""
    return client.get_or_create_collection(name=name)
