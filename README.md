# GraphifyMind
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


