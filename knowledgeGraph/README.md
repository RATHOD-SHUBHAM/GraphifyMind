# GraphifyMind

**GraphifyMind** is a Streamlit application that transforms plain text or PDF documents into interactive knowledge graphs, powered by Large Language Models (LLMs), graph databases, and AI-driven visualization.

---

## 🚀 Features

- **Text & PDF Input**: Paste text or upload PDF documents for processing.
- **Entity Filtering**: Optionally specify *allowed nodes* (e.g., Person, Place) to focus the graph.
- **Interactive Visualization**: Generates a web-based graph (HTML) showing entities and relationships.
- **Docker Support**: Run the app in a container for easy deployment.

---

## 📂 Folder Structure

```
GraphifyMind/
├── graph/                 # Generated HTML graphs
├── input/                 # Uploaded PDF files
├── src/                   # Python source code
│   └── knowledgeGraph.py  # Core graph-generation logic
├── icon.jpg               # App icon
├── main.py                # Streamlit application script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container build instructions
└── README.md              # This file
```

---

## ⚙️ Prerequisites

- **Python 3.10+**
- **OpenAI API Key** (set at runtime via the sidebar)
- **Docker** (optional, for containerized deployment)

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/GraphifyMind.git
   cd GraphifyMind
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # on macOS/Linux
   .\.venv\Scripts\activate   # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🚗 Running Locally

1. **Start Streamlit**

   ```bash
   streamlit run main.py
   or 
   uv add -r requirements.txt
   uv pip install -r requirements.txt
   uv run streamlit run main.py
   ```

2. **Open your browser** at `http://localhost:8501`.

3. **Enter your OpenAI API key** in the sidebar.

4. **Select input mode** (Text or PDF), provide content, optionally add nodes, and click **Visualize Graph**.

---

## 🐳 Running with Docker

Instead of building locally, you can pull the pre-built image directly from Docker Hub:

1. **Pull the image**

   ```bash
   docker pull your-dockerhub-username/graphifymind:latest
   ```

2. **Run the container**, mounting local folders for persistence:

   ```bash
   docker run -d \
     -p 8501:8501 \
     -v $(pwd)/input:/app/input \
     -v $(pwd)/graph:/app/graph \
     your-dockerhub-username/graphifymind:latest
   ```
   or
   ```
   docker run -p 8501:8501 knowledgegraph
   ```

3. **Visit** `http://localhost:8501` in your browser.

## ⚙️ Configuration

- **OpenAI API Key**: Entered in the sidebar at runtime—no need to set env vars manually.
- **Input & Output Directories**: `input/` and `graph/` are created automatically; you can also pre-populate or inspect them.

---

## 💡 Usage Tips

- For long documents, use the PDF upload for best formatting.
- Define only the nodes you care about (e.g., `Person`, `Organization`) to reduce clutter.
- The generated graph HTML is saved in `graph/knowledge_graph.html` and can be shared.

---

