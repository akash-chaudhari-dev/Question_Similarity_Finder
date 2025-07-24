import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
from pathlib import Path
from Tools.Clean_data import Clean_Data
from Tools.Fetch_data import Fetch_Data

def load_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df
    except pd.errors.EmptyDataError:
        st.error("❌ CSV file is empty. Please check the file.")
        st.stop()
    except pd.errors.ParserError:
        st.warning("⚠️ CSV format issue detected. Attempting to clean the data...")
        cleaned_path = Clean_Data(csv_path)
        return load_data(cleaned_path)
    except Exception as e:
        st.error(f"🚨 Unexpected error: {str(e)}")
        st.stop()

# Getting the Path to CSV
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data" / "data.csv"

# Download Data If Not Exist
if not csv_path.exists():
    csv_path = Fetch_Data(QUESTIONS=100,BATCH_SIZE=10)

# Initialize the SentenceTransformer model
# model for non CUDA based PC's
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

# for Cuda based PC
model = SentenceTransformer('all-MiniLM-L6-v2')

# Set the title
st.title("🧠 Question Similarity Finder")
st.markdown("Welcome! This tool helps find questions similar to one you choose, based on tags/categories.")

# Load your questions dataset
df = load_data(csv_path)

# Show available questions to choose from
st.subheader("📋 Available questions:")
st.dataframe(df[['Question']], use_container_width=True)

# Convert all dataset questions to embeddings once
question_embeddings = model.encode(df['Question'].tolist(), convert_to_tensor=True)

# Ask the user to pick a question index
st.subheader("🔍 Write a Question")
user_question = st.text_input("Enter question :", placeholder="e.g., Who is the CEO of Apple?", value="Who is the CEO of Apple?")

if not user_question:
    user_question = "Who is the CEO of Apple?"

if user_question:
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, question_embeddings)[0]

st.markdown("---")

# Show top 5 similar questions (excluding itself)
st.subheader("📚 Similar questions:")

top_results = torch.topk(similarity_scores, k=5)

# Get the index of the most similar question
top_idx = top_results.indices[0].item()
top_category = df.iloc[top_idx]['Category']

if top_results.values[0] < 0.3:
    st.warning("🤔 No confident match found. Try rephrasing your question.")
else:
    st.markdown(f"Most Likely The Question is from **{top_category}**")
    st.subheader("📚 Similar questions:")
    for score, idx in zip(top_results.values, top_results.indices):
        score_val = score.item()
        index_val = idx.item()
        question = df.iloc[index_val]['Question']
        st.markdown(f"- **Q{index_val}:** {question} (Score: {score_val:.4f})")

st.markdown("---")
st.markdown("✅ Thank you for using the Question Similarity Finder!")

# Branding Custom Showcase
Branding = '''
    <style>
        .floating-footer {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #000000;
            padding: 12px 16px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            z-index: 100;
            font-size: 14px;
        }
        .floating-footer a {
            text-decoration: none;
            color: #0A66C2;
            font-weight: bold;
        }
    </style>

    <div class="floating-footer">
        🚀 Built with 💻 by <strong>Akash</strong> |
        <a href="https://www.linkedin.com/in/akash-ch/" target="_blank">LinkedIn</a>
    </div>
    '''
st.markdown(Branding, unsafe_allow_html=True)