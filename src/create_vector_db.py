# ============================================
# File: create_vector_db.py
# Step 4: Create local ChromaDB vector database (with progress bar)
# ============================================

import os
import sys
import time
import pandas as pd
import chromadb
from tqdm import tqdm  # ✅ For progress visualization

# -------------------------------------------------
# 🧩 Disable Chroma Telemetry (to avoid warnings)
# -------------------------------------------------
os.environ["CHROMA_TELEMETRY_ENABLED"] = "false"

# -------------------------------------------------
# 1️⃣ Load Prepared CSV Data
# -------------------------------------------------
print("📥 Loading prepared datasets...")

qa_path = "../data/medical_q_n_a_prepared.csv"
device_path = "../data/medical_device_manuals_prepared.csv"

df_qa = pd.read_csv(qa_path)
df_device = pd.read_csv(device_path)

print(f"✅ Loaded Q&A dataset with {len(df_qa)} rows")
print(f"✅ Loaded Device Manual dataset with {len(df_device)} rows")

# -------------------------------------------------
# 2️⃣ Initialize ChromaDB Client
# -------------------------------------------------
print("\n⚙️ Initializing ChromaDB client...")
client = chromadb.PersistentClient(path="../chroma_db")

# -------------------------------------------------
# 3️⃣ Create Collections
# -------------------------------------------------
print("\n📚 Creating collections...")
qa_collection = client.get_or_create_collection(name="medical_q_n_a")
device_collection = client.get_or_create_collection(name="medical_device_manual")

# -------------------------------------------------
# 4️⃣ Add Data with Progress Feedback
# -------------------------------------------------
print("\n🧩 Adding data to collections... (this will take a few minutes)")
start_time = time.time()

# --- Helper function to process data in batches ---
def add_in_batches(collection, df, batch_size=100):
    total = len(df)
    for i in tqdm(range(0, total, batch_size), desc=f"→ {collection.name}", ncols=80):
        batch = df.iloc[i:i+batch_size]
        collection.add(
            documents=batch["combined_text"].tolist(),
            metadatas=batch.to_dict(orient="records"),
            ids=[str(j) for j in batch.index],
        )

# --- Q&A Dataset ---
add_in_batches(qa_collection, df_qa)

# --- Device Manual Dataset ---
add_in_batches(device_collection, df_device)

elapsed = time.time() - start_time
print(f"✅ Data added successfully in {elapsed/60:.2f} minutes")

# -------------------------------------------------
# 5️⃣ Quick Retrieval Test
# -------------------------------------------------
print("\n🔍 Testing a sample retrieval...")

sample_query = "What are the treatments for Kawasaki disease?"
results = qa_collection.query(query_texts=[sample_query], n_results=2)

print("\nTop 2 Retrieved Documents:")
for doc in results["documents"][0]:
    print("-", doc[:200], "...")

# -------------------------------------------------
# 6️⃣ Done
# -------------------------------------------------
print("\n🎯 ChromaDB setup complete! Collections are ready for use.")
sys.exit(0)
