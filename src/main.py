import networkx as nx
import community as community_louvain
from kg_builder import build_graph
from llm_answer import answer_with_kg, answer_without_kg


def main():
    corpus_path = "../data/corpus.json"
    G, corpus = build_graph(corpus_path)

    print("=" * 70)
    print("KG-RAG Question Answering Demo")
    print("=" * 70)
    print(f"Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    partition = community_louvain.best_partition(G)
    nx.set_node_attributes(G, partition, "community")

    queries = [
        "Where was Alexander the Great born?",
        "What language do people speak in North Macedonia?",
        "What is the connection between Cyril and the Slavic alphabet?",
        "What happened at the Battle of Kleidion?",
        "What is the UNESCO World Heritage Site near Ohrid?"
    ]

    results = []

    for i, q in enumerate(queries, 1):
        kg_ans = answer_with_kg(q, G, corpus)
        base_ans = answer_without_kg(q, corpus)

        results.append({
            "query": q,
            "kg_answer": kg_ans["answer_context"],
            "baseline_answer": base_ans["answer_context"],
            "kg_entities": kg_ans["kg_entities"],
            "kg_relations": kg_ans["kg_relations_count"]
        })

        print("\n" + "-" * 70)
        print(f"Q{i}: {q}")

        print("\n[KG-RAG]")
        print("Entities used:", kg_ans["kg_entities"][:5])
        print("Relations used:", kg_ans["kg_relations_count"])
        print("Answer:", kg_ans["answer_context"])

        print("\n[Baseline]")
        print("Answer:", base_ans["answer_context"])

    nx.write_gexf(G, "../output/knowledge_graph.gexf")
    print("\nGraph saved to output/knowledge_graph.gexf")

    return results


if __name__ == "__main__":
    main()