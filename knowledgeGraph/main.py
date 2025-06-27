import os
import re
from pathlib import Path
import streamlit as st
from src.knowledgeGraph import KnowledgeGraph
import streamlit.components.v1 as components  # For embedding custom HTML
from langchain_community.document_loaders import PyPDFLoader

import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="GraphifyMind",
    page_icon="🧠",
)

# Hide hamburger menu and customize footer
hide_menu = """
    <style>
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: visible;
    }
    footer:after {
        content: 'With 🫶️ from Shubham Shankar.';
        display: block;
        position: relative;
        color: grey;
        padding: 5px;
        top: 3px;
    }
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Branding
st.image("icon.jpg", width=85)
st.title("🦜GraphifyMind")
st.subheader("Turn your documents into beautiful knowledge graphs 🕸️")
st.write("Powered by LLMs, Graph Databases & AI Visualization.")

# Intro
st.write(
    """
    Welcome to **:green[GraphifyMind]** by **:red[Shubham Shankar]**! 🚀

    This app helps you **visualize your data** like never before.  
    Upload a **PDF** or paste any **text**, and watch it turn into a **beautiful knowledge graph** that captures **key entities** and their **relationships**.

    ---
    ### 🧠 Why Use This?

    In many real-world scenarios — whether it's **research**, **reports**, or **business documents** — we're often asked:

    - *"What does this document talk about?"*
    - *"Who are the key people, places, and things mentioned?"*
    - *"How are these elements connected?"*

    Instead of manually reading and highlighting, **GraphifyMind** lets AI do the heavy lifting — it extracts important concepts and links them together so you can **see the structure of your data** at a glance.

    Great for:
    - 📄 Report breakdowns
    - 🧾 Meeting notes understanding
    - 🧬 Research mapping
    - 📚 Learning complex topics visually

    ---
    Powered by advanced **:orange[LLMs]**, **Graph Databases**, and **AI-driven Visualization**.
    """
)


st.markdown('---')

# Instructions
st.write(
    """
    ### 🧭 How to Use:

    📝 **Input Your Data**
    - Enter plain text in the text box, or upload a `.pdf` file.

    🧠 **Select Graph Options**
    - Choose node types to focus on (e.g., Person, Place, Concept).

    🌐 **Visualize**
    - Click the button to generate and explore your personalized knowledge graph.

    """
)

st.markdown('---')

# Footer
st.error(
    """
    Connect with me on [**Github**](https://github.com/RATHOD-SHUBHAM) and [**LinkedIn**](https://www.linkedin.com/in/shubhamshankar/). 🧠✨
    """,
    icon="🧑‍💻",
)
st.markdown('---')


# Directories - Use absolute paths for Docker compatibility
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
GRAPH_DIR = BASE_DIR / "graph"
INPUT_DIR.mkdir(exist_ok=True)
GRAPH_DIR.mkdir(exist_ok=True)

# Utility to sanitize filenames
def sanitize_filename(filename: str) -> str:
    return re.sub(r'[^A-Za-z0-9_.-]', '_', filename)

# streamlit code for viewing document
def main():
    st.sidebar.header("🔧 Configuration")

    # API Key input (mandatory)
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password", key="api_key_input")
    if not api_key:
        st.sidebar.warning("API key is required to generate the graph.")

    # Instantiate KnowledgeGraph once key is provided
    ob = None
    if api_key:
        ob = KnowledgeGraph(api_key=api_key)

    # Input mode selection
    input_mode = st.sidebar.radio("Select input mode:", ("Text", "File"), key="input_mode_radio")

    # Text input or file uploader
    text_input = ""
    if input_mode == "Text":
        text_input = st.sidebar.text_area("Enter text here:", height=200, key="text_input_area")
    else:
        uploaded_file = st.sidebar.file_uploader("Upload a PDF file:", type=['pdf'], key="pdf_file_uploader")
        if uploaded_file:
            filename = sanitize_filename(uploaded_file.name)
            save_path = INPUT_DIR / filename
            try:
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.sidebar.success(f"Saved to {save_path}")
                loader = PyPDFLoader(str(save_path))
                docs = loader.load()
                text_input = "\n".join(doc.page_content for doc in docs)
            except Exception as e:
                st.sidebar.error(f"Failed to save or read PDF: {e}")


    # --- Allowed Nodes Definition ---
    st.sidebar.markdown("---")
    st.sidebar.header("Allowed Nodes (optional)")
    if "allowed_nodes" not in st.session_state:
        st.session_state.allowed_nodes = []

    new_node = st.sidebar.text_input("Enter node name:", key="new_node_input")
    if st.sidebar.button("Add node", key="add_node_button"):
        if new_node.strip():
            st.session_state.allowed_nodes.append(new_node.strip())
            st.sidebar.success(f"Added node: {new_node.strip()}")
        else:
            st.sidebar.warning("Node name cannot be empty.")

    if st.session_state.allowed_nodes:
        st.sidebar.markdown("**Current Allowed Nodes:**")
        st.sidebar.write(st.session_state.allowed_nodes)

    # --- Visualization Trigger ---
    st.sidebar.markdown("---")
    st.sidebar.header("🖼️ Visualization")
    visualize = st.sidebar.button("Visualize Graph", key="visualize_button")

    # --- Main Area: Graph Display ---
    if visualize:
            with st.spinner("Generating knowledge graph..."):
                # Input validation
                if not text_input:
                    st.warning("Please provide some text or upload a valid file first.")
                else:
                    # Generate and render HTML graph
                    # Branch based on allowed_nodes presence
                    if st.session_state.allowed_nodes:
                        net = ob.generate_graph_data_with_nodes(text_input, st.session_state.allowed_nodes)
                        st.success("Knowledge graph generated successfully!")
                
                        # Save the graph to an HTML file
                        output_file = GRAPH_DIR / "knowledge_graph.html"

                        # Open the HTML file and display it within the Streamlit app
                        try:
                            with open(output_file, 'r', encoding='utf-8') as HtmlFile:
                                components.html(HtmlFile.read(), height=1000)
                        except FileNotFoundError:
                            st.error(f"Graph file not found at {output_file}")
                    else:
                        net = ob.generate_graph_data(text_input)
                        st.success("Knowledge graph generated successfully!")
                
                        # Save the graph to an HTML file
                        output_file = GRAPH_DIR / "knowledge_graph.html"

                        # Open the HTML file and display it within the Streamlit app
                        try:
                            with open(output_file, 'r', encoding='utf-8') as HtmlFile:
                                components.html(HtmlFile.read(), height=1000)
                        except FileNotFoundError:
                            st.error(f"Graph file not found at {output_file}")



if __name__ == "__main__":
    main()