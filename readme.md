🧠 Question Similarity Finder

> An intelligent semantic search app that finds questions similar to yours using state-of-the-art NLP models.

📍 **Live Demo**: [https://question-similarity-finder.onrender.com](https://question-similarity-finder.onrender.com)

---

## ✨ What's New (v1.1)

🚀 Major update with smarter, faster, and more user-friendly features:

* ✅ **Free-form user question input**
* ✅ Upgraded to **semantic similarity** using `SentenceTransformer`
* ✅ Trained on **\~1000 questions**
* ✅ Added **automatic fallback tools**:

  * 📦 `Fetch_Data` → loads new data if missing
  * 🧹 `Clean_Data` → auto-fixes corrupted CSVs
* 🖥️ CLI support in progress for developer review & debugging
* 📂 Clean modular folder structure with reusable `Tools/`

---

## 🖼️ Preview

| 👇 Input your Question       | 📊 See Similar Questions       |
| ---------------------------- | ------------------------------ |
| ![input](./assets/image.png) | ![output](./assets/image1.png) |

---

## 🗂️ Project Structure

```
Question_Similarity_Finder/
├── main.py                     # Main Streamlit app
├── data/                       # Contains cleaned/fetched CSV
│   └── data.csv
├── Tools/                      # Utility modules
│   ├── Clean_data.py
│   └── Fetch_data.py
├── assets/                     # UI screenshots
├── requirements.txt
└── README.md
```

---

## 🔧 Tech Stack

* Python
* Streamlit
* pandas
* torch + sentence-transformers (`all-MiniLM-L6-v2`)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Question_Similarity_Finder.git
cd Question_Similarity_Finder
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 📁 Data Format

CSV file: `data/data.csv`

| Question                        | Category    | Difficulty | Answer       |
| ------------------------------- | ----------- | ---------- | ------------ |
| What is Python?                 | Programming | Easy       | Python is... |
| Difference between SQL & NoSQL? | Databases   | Medium     | SQL is...    |

---

## 🔍 How It Works

1. **Embeddings** are generated using `SentenceTransformer`
2. **Cosine similarity** compares your input with all questions
3. **Top 5 similar questions** are shown with scores and categories

---

## 🧪 CLI Mode (In Progress)

Developers can soon run:

```bash
python cli.py --question "What is backpropagation?"
```

To test model performance from the terminal.

---

## 🛠️ Future Work

* ✅ CLI Utilities for developers
* 🔍 Keyword highlighting in results
* 🌐 API backend for integration
* 📈 Model selection toggle
* 👤 User history & bookmarking

---

## 🙋‍♂️ Author

Made with ❤️ by **Akash**, a 3rd-year Data Science & AI student chasing GATE AIR 1.

🔗 [LinkedIn](https://www.linkedin.com/in/akash-ch/)