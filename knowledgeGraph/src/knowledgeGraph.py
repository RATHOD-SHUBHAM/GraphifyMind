import os
from dotenv import load_dotenv
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from pyvis.network import Network
import asyncio
from pathlib import Path

# Loading Environment Variables



class KnowledgeGraph:
    def __init__(self, api_key: str):
        os.environ["OPENAI_API_KEY"] = api_key
        self.llm = ChatOpenAI(temperature=0, model_name = "gpt-4o")
        
    def visualize_graph(self, graph_documents):
        """
        Visualizes a knowledge graph using PyVis based on the extracted graph documents.

        Args:
            graph_documents (list): A list of GraphDocument objects with nodes and relationships.

        Returns:
            pyvis.network.Network: The visualized network graph object.
        """
        # Create network
        net = Network(height="1200px", width="100%", directed=True,
                        notebook=False, bgcolor="#222222", font_color="white", filter_menu=True, cdn_resources='remote') 

        nodes = graph_documents[0].nodes
        relationships = graph_documents[0].relationships

        # Build lookup for valid nodes
        node_dict = {node.id: node for node in nodes}
        
        # Filter out invalid edges and collect valid node IDs
        valid_edges = []
        valid_node_ids = set()
        for rel in relationships:
            if rel.source.id in node_dict and rel.target.id in node_dict:
                valid_edges.append(rel)
                valid_node_ids.update([rel.source.id, rel.target.id])

        # Track which nodes are part of any relationship
        connected_node_ids = set()
        for rel in relationships:
            connected_node_ids.add(rel.source.id)
            connected_node_ids.add(rel.target.id)

        # Add valid nodes to the graph
        for node_id in valid_node_ids:
            node = node_dict[node_id]
            try:
                net.add_node(node.id, label=node.id, title=node.type, group=node.type)
            except:
                continue  # Skip node if error occurs

        # Add valid edges to the graph
        for rel in valid_edges:
            try:
                net.add_edge(rel.source.id, rel.target.id, label=rel.type.lower())
            except:
                continue  # Skip edge if error occurs

        # Configure graph layout and physics
        net.set_options("""
            {
                "physics": {
                    "forceAtlas2Based": {
                        "gravitationalConstant": -100,
                        "centralGravity": 0.01,
                        "springLength": 200,
                        "springConstant": 0.08
                    },
                    "minVelocity": 0.75,
                    "solver": "forceAtlas2Based"
                }
            }
        """)

        # Use absolute path for Docker compatibility
        base_dir = Path(__file__).resolve().parent.parent
        output_file = base_dir / "graph" / "knowledge_graph.html"
        
        # Ensure the graph directory exists
        output_file.parent.mkdir(exist_ok=True)
        
        try:
            net.save_graph(str(output_file))
            print(f"Graph saved to {output_file}")
            return net
        except Exception as e:
            print(f"Error saving graph: {e}")
            return None
    
    async def extract_graph_data(self, text):
        """
        Asynchronously extracts graph data from input text using a graph transformer.

        Args:
            text (str): Input text to be processed into graph format.

        Returns:
            list: A list of GraphDocument objects containing nodes and relationships.
        """
        graph_transformer = LLMGraphTransformer(llm=self.llm)
        documents = [Document(page_content=text)]
        graph_documents = await graph_transformer.aconvert_to_graph_documents(documents)

        return graph_documents

    async def extract_graph_data_with_nodes(self, text, allowed_nodes):
        """
        Asynchronously extracts graph data from input text using a graph transformer.

        Args:
            text (str): Input text to be processed into graph format.

        Returns:
            list: A list of GraphDocument objects containing nodes and relationships.
        """
        graph_transformer = LLMGraphTransformer(llm=self.llm, allowed_nodes=allowed_nodes)
        documents = [Document(page_content=text)]
        graph_documents = await graph_transformer.aconvert_to_graph_documents(documents)

        return graph_documents


    def generate_graph_data(self, text):
        """
        Generates and visualizes a knowledge graph from input text.

        This function runs the graph extraction asynchronously and then visualizes
        the resulting graph using PyVis.

        Args:
            text (str): Input text to convert into a knowledge graph.

        Returns:
            pyvis.network.Network: The visualized network graph object.
        """
        graph_documents = asyncio.run(self.extract_graph_data(text))
        net = self.visualize_graph(graph_documents)
        return net


    def generate_graph_data_with_nodes(self, text, allowed_nodes):
        """
        Generates and visualizes a knowledge graph from input text.

        This function runs the graph extraction asynchronously and then visualizes
        the resulting graph using PyVis.

        Args:
            text (str): Input text to convert into a knowledge graph.
            allowed_nodes List[str] : Define specific types of nodes

        Returns:
            pyvis.network.Network: The visualized network graph object.
        """
        graph_documents = asyncio.run(self.extract_graph_data_with_nodes(text, allowed_nodes))
        net = self.visualize_graph(graph_documents)
        return net