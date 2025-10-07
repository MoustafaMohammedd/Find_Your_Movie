# 🎬 Find Your Movie — AI-Powered Semantic Search for Netflix Titles

> **Find Your Movie** is an AI-powered semantic search engine that helps users discover Netflix shows and movies by **meaning**, not just keywords.
>
> Using **vector embeddings**, **FAISS**, and **FastAPI**, this project enables natural language queries such as:
> *“Show me a romantic movie about a couple fighting to stay together.”*
> — and retrieves the most semantically relevant titles from the Netflix catalog.

---

## 🧠 Features

* 🔍 **Semantic Search:** Retrieve titles by meaning using vector embeddings.
* ⚙️ **Vector Database:** Powered by **FAISS** for efficient similarity search.
* 🤖 **Transformer Embeddings:** Uses **Hugging Face** models for text representation.
* 🌐 **FastAPI Backend:** For easy integration.
* 📊 **Exploratory Data Analysis (EDA):** Jupyter notebook to understand and clean data.
* 🧪 **Tests:** Test search functionality for consistency and accuracy.

---

## 🗂️ Project Structure

```
Find_Your_Movie/
│
├── data/
│   │── netflix-tv-shows-and-movies/
│   │    ├── NetFlix.csv
│   │    └── cleaned_netflix.csv
│   └── load_data.py
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── main.py                         # FastAPI app entry point
│   │
│   ├── retrieval/
│   │   ├── relevance_ranking.py        # Retriever creation using FAISS
│   │   └── search.py                   # Core semantic search logic
│   │
│   ├── utils/
│   │   ├── config.py                   # Input/output paths
│   │   ├── data_loader.py              # Load and clean Netflix dataset
│   │   └── preprocessing.py            # Preprocessing pipeline
│   │
│   ├── vector_store/
│   │   ├── embedding_model.py          # Hugging Face embedding model
│   │   ├── create_vector_store.py      # Build FAISS index
│   │   └── load_vector_store.py        # Load FAISS index for retrieval
│   │
│   └── vector_database/
│       ├── index.faiss
│       └── index.pkl
│
├── tests/
│   └── test_search.py                  # Test vector search
│
├── .env.example                        # Example environment variables
├── requirements.txt                    # Project dependencies
└── README.md                           # Documentation
```

---

## 🧩 Setup and Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MoustafaMohammedd/Find_Your_Movie.git
cd Find_Your_Movie
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```
MODEL_NAME="sentence-transformers/all-MiniLM-L6-v2"
```

You can also duplicate `.env.example` and rename it to `.env`.

---

## 📥 Download the Dataset

`src/utils/load_data.py` uses **OpenDatasets** to download the Netflix dataset from Kaggle.

Run:

```bash
python data/load_data.py
```

This will download the dataset to:

```
data/netflix-tv-shows-and-movies/NetFlix.csv
```

---

## 🧹 Data Preprocessing

To clean and prepare the data:

```bash
python src/utils/data_loader.py
```

This script:

* Selects only the required columns (`title`, `description`)
* Converts columns to `string` type
* Saves cleaned data to `cleaned_netflix.csv`

---

## 🧠 Create the Vector Store

Build the FAISS index with embeddings:

```bash
python src/vector_store/create_vector_store.py
```

This will:

* Load the cleaned dataset
* Generate text embeddings using your chosen Hugging Face model
* Save the vector store in `src/vector_database/`

---

## 🔍 Search Movies with Semantic Similarity

Run the FastAPI backend:

```bash
uvicorn src.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

You can now:

* Access the `/search` endpoint
* Send a POST request like:

```json
{
  "query": "romantic love story between a couple fighting to live together",
  "search_method": "mmr",
  "n_movies": 3,
  "f_k": 10
}
```
---

## 🧪 Run Tests

```bash
pytest tests/test_search.py
```

This ensures your retriever and search pipeline are functioning properly.

---

## 🧠 How It Works (Under the Hood)

| Step                      | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| **1. Data Cleaning**      | Keep relevant columns (`title`, `description`)              |
| **2. Embedding Creation** | Convert descriptions to vectors using Sentence Transformers |
| **3. Vector Indexing**    | Store embeddings in FAISS for similarity search             |
| **4. Query Encoding**     | User query → vector embedding                               |
| **5. Retrieval**          | Retrieve top-K semantically similar items                   |
| **6. Display Results**    | Return movie titles + descriptions                          |

---
## 📊 EDA and Insights

The `notebooks/EDA.ipynb` includes:

* Data distribution by show type (Movies vs TV Shows)
* Common genres and keywords
* Missing values and cleaning process

---

## 🚀 Future Enhancements

* Add **LLM-powered Q&A** (e.g., “Which movies are similar to Inception?”)
* Integrate **UI** for interactive search
* Add **filtering by year, genre, or country**
* Support **multi-language search queries**

---
