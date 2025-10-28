"""
prepare_data.py
----------------
This script loads the two medical datasets, prepares them by combining columns
into a single 'combined_text' field, and saves cleaned versions for later use
in the Agentic RAG pipeline.
"""

# ======== Import necessary libraries ========
import pandas as pd
import os

# ======== Define file paths ========
# Use relative paths to ensure flexibility
data_dir = os.path.join("..", "data")
qa_file = os.path.join(data_dir, "medical_q_n_a.csv")
device_file = os.path.join(data_dir, "medical_device_manuals_dataset.csv")

# ======== Step 1: Load both datasets ========
print("Loading datasets...")

df_qa = pd.read_csv(qa_file)
df_device = pd.read_csv(device_file)

print(f"✅ Q&A dataset loaded with shape: {df_qa.shape}")
print(f"✅ Device dataset loaded with shape: {df_device.shape}")

# ======== Step 2: Prepare the Q&A Dataset ========
print("\nPreparing the Medical Q&A dataset...")

# Combine the Question, Answer, and qtype columns into one text field
# Example output: "Question: What is diabetes? Answer: It is a metabolic disorder. Type: disease."
df_qa["combined_text"] = (
    "Question: " + df_qa["Question"].astype(str) + ". "
    + "Answer: " + df_qa["Answer"].astype(str) + ". "
    + "Type: " + df_qa["qtype"].astype(str) + "."
)

# Check the first 2 combined rows
print("\nSample Q&A combined text:")
print(df_qa["combined_text"].head(2).to_string(index=False))

# ======== Step 3: Prepare the Medical Device Manual Dataset ========
print("\nPreparing the Medical Device Manual dataset...")

# Combine relevant columns into one field.
# Example output:
# "Device Name: Pacemaker. Model: J123. Manufacturer: Medtronic. Indications: ... Contraindications: ..."
df_device["Contraindications"] = df_device["Contraindications"].fillna("None")

df_device["combined_text"] = (
    "Device Name: " + df_device["Device_Name"].astype(str) + ". "
    + "Model: " + df_device["Model_Number"].astype(str) + ". "
    + "Manufacturer: " + df_device["Manufacturer"].astype(str) + ". "
    + "Indications: " + df_device["Indications_for_Use"].astype(str) + ". "
    + "Contraindications: " + df_device["Contraindications"].astype(str) + "."
)

print("\nSample Device combined text:")
print(df_device["combined_text"].head(2).to_string(index=False))

# ======== Step 4: Save the cleaned versions ========
print("\nSaving prepared datasets...")

prepared_qa_path = os.path.join(data_dir, "medical_q_n_a_prepared.csv")
prepared_device_path = os.path.join(data_dir, "medical_device_manuals_prepared.csv")

df_qa.to_csv(prepared_qa_path, index=False)
df_device.to_csv(prepared_device_path, index=False)

print(f"✅ Saved: {prepared_qa_path}")
print(f"✅ Saved: {prepared_device_path}")

print("\n🎯 Data preparation completed successfully!")
