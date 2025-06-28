# GraphifyMind

**GraphifyMind** is a Streamlit application that transforms plain text or PDF documents into interactive knowledge graphs, powered by Large Language Models (LLMs), graph databases, and AI-driven visualization.

Docker Image: [Link](https://hub.docker.com/r/gibbo96/knowledgegraph)

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

<img width="1052" alt="Image" src="https://github.com/user-attachments/assets/5b4da3cb-2155-4458-8235-d14467761acd" />

<img width="1037" alt="Image" src="https://github.com/user-attachments/assets/29716218-e57d-462a-9086-ea41d66927c3" />


<img width="2276" alt="Image" src="https://github.com/user-attachments/assets/b831574f-6bee-415e-839a-bd352cea0fbe" />

---

Folder Structure

<img width="308" alt="Image" src="https://github.com/user-attachments/assets/f03e82a7-5541-40c4-8664-25b9b2a67d26" />

