import spacy
import networkx as nx

nlp = spacy.load("en_core_web_sm")


def retrieve_relevant_nodes(G, query, top_k=10):
    query_doc = nlp(query.lower())
    query_tokens = set(
        token.lemma_ for token in query_doc if not token.is_stop and len(token.text) > 2
    )
    query_entities = set(ent.text.lower() for ent in query_doc.ents)

    scores = {}

    for node in G.nodes():
        node_lower = node.lower()
        score = 0

        if node_lower in query_entities:
            score += 5

        for token in query_tokens:
            if token in node_lower:
                score += 2

        score += G.degree(node) * 0.1

        if score > 0:
            scores[node] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    return [node for node, _ in ranked]


def get_subgraph_context(G, relevant_nodes):
    expanded = set(relevant_nodes)

    for node in relevant_nodes:
        neighbors = list(G.neighbors(node))
        expanded.update(neighbors[:5])

    return G.subgraph(expanded)


def subgraph_to_text(subgraph):
    lines = []
    node_types = nx.get_node_attributes(subgraph, "label")

    lines.append("=== Knowledge Graph Context ===")
    lines.append(f"Entities: {list(subgraph.nodes())[:20]}")
    lines.append("")
    lines.append("Relationships:")

    for u, v, data in subgraph.edges(data=True):
        weight = data.get("weight", 1)
        lines.append(
            f"[{node_types.get(u, '?')}] {u} <--> {v} [{node_types.get(v, '?')}] (strength={weight})"
        )

    return "\n".join(lines)