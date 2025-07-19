import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Set the title
st.title("🧠 Question Similarity Finder")
st.markdown("Welcome! This tool helps find questions similar to one you choose, based on tags/categories.")

# Load your questions dataset
try:
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("⚠️ data.csv not found. Please make sure the file is in the same directory.")
    st.stop()

# Show available questions to choose from
st.subheader("📋 Available Questions:")
st.dataframe(df[['Question']], use_container_width=True)

# Convert tags/categories into feature vectors
vectorizer = CountVectorizer()
tag_matrix = vectorizer.fit_transform(df['Category'])

# Compute cosine similarity between all questions
similarity = cosine_similarity(tag_matrix)

# Ask the user to pick a question index
st.subheader("🔍 Choose a Question to Find Similar Ones")
question_idx = st.number_input("Enter question ID:", min_value=0, max_value=len(df)-1, step=1)

st.markdown("---")
st.markdown(f"### 📝 Selected Question:")
st.markdown(f"**{df.iloc[question_idx]['Question']}**")

# Get similarity scores for the selected question
similar_scores = list(enumerate(similarity[question_idx]))
similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)

# Show top 5 similar questions (excluding itself)
st.subheader("📚 Similar Questions:")

results_shown = 0
for idx, score in similar_scores:
    if idx != question_idx and score > 0:
        st.markdown(f"- **Q{idx}:** {df.iloc[idx]['Question']} (Score: {score:.4f})")
        results_shown += 1
        if results_shown >= 5:
            break

if results_shown == 0:
    st.info("No similar questions found.")

st.markdown("---")
st.markdown("✅ Thank you for using the Question Similarity Finder!")
