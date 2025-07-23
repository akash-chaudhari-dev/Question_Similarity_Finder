import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Goes from cli/ → dir/
location = os.path.join(BASE_DIR, 'data', 'data.csv')

print(BASE_DIR,location)

# Later we will first dowload dataset form kaggle then store and then load it
# For now, we will assume the dataset is already available as 'data.csv'
def load_data(location=r'../data/data.csv'):
    try:
        data = pd.read_csv(location)
        df = pd.DataFrame(data)
        return df
    except FileNotFoundError:
        print("⚠️ data.csv not found. Please make sure the file is in the same directory.")
        exit()

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your questions dataset

df = load_data()

# Convert all dataset questions to embeddings once
question_embeddings = model.encode(df['Question'].tolist(), convert_to_tensor=True)
# torch.save(question_embeddings, '../data/embeddings.pt')
# take user input
user_question = input("Enter question: ")

if user_question:
    user_embedding = model.encode(user_question, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, question_embeddings)[0]

# Get top 5 similar questions
top_results = torch.topk(similarity_scores, k=5)

if top_results.values[0] < 0.3:
    print("🤔 No confident match found. Try rephrasing your question.")
else:
    print("📚 Similar Questions:")
    for score, idx in zip(top_results.values, top_results.indices):
        print(f"- **Q{idx.item()}:** {df.iloc[idx.item()]['Question']} (Score: {score.item():.4f})")
