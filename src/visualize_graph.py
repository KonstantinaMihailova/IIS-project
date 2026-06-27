import json
import networkx as nx
import matplotlib.pyplot as plt
from kg_builder import build_graph


def main():
    corpus_path = "../data/corpus.json"
    G, corpus = build_graph(corpus_path)

    plt.figure(figsize=(16, 10))

    # Top nodes only for cleaner visualization
    top_nodes = [node for node, degree in sorted(G.degree(), key=lambda x: x[1], reverse=True)[:25]]
    subgraph = G.subgraph(top_nodes)

    pos = nx.spring_layout(subgraph, seed=42, k=0.8)

    node_sizes = [800 + subgraph.degree(node) * 250 for node in subgraph.nodes()]
    node_colors = []

    for node in subgraph.nodes():
        label = subgraph.nodes[node].get("label", "")
        if label == "PERSON":
            node_colors.append("lightcoral")
        elif label in ["GPE", "LOC"]:
            node_colors.append("lightblue")
        elif label == "ORG":
            node_colors.append("lightgreen")
        elif label == "NORP":
            node_colors.append("gold")
        else:
            node_colors.append("lightgray")

    nx.draw_networkx_nodes(
        subgraph,
        pos,
        node_size=node_sizes,
        node_color=node_colors,
        alpha=0.9
    )

    nx.draw_networkx_edges(
        subgraph,
        pos,
        width=1.5,
        alpha=0.5,
        edge_color="gray"
    )

    nx.draw_networkx_labels(
        subgraph,
        pos,
        font_size=8,
        font_weight="bold"
    )

    plt.title("Knowledge Graph Visualization - Macedonian History Domain", fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("../output/knowledge_graph.png", dpi=300)
    plt.show()

    print("Graph visualization saved to output/knowledge_graph.png")


if __name__ == "__main__":
    main()