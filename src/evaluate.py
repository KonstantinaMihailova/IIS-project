import pandas as pd
from kg_builder import build_graph
from llm_answer import answer_with_kg, answer_without_kg


def entity_coverage(answer_text, kg_entities):
    answer_lower = answer_text.lower()
    hits = 0

    for ent in kg_entities:
        if ent.lower() in answer_lower:
            hits += 1

    if len(kg_entities) == 0:
        return 0

    return round((hits / len(kg_entities)) * 100, 2)


def main():
    corpus_path = "../data/corpus.json"
    G, corpus = build_graph(corpus_path)

    queries = [
        "Where was Alexander the Great born?",
        "What language do people speak in North Macedonia?",
        "What is the connection between Cyril and the Slavic alphabet?",
        "What happened at the Battle of Kleidion?",
        "What is the UNESCO World Heritage Site near Ohrid?"
    ]

    rows = []

    for q in queries:
        kg_ans = answer_with_kg(q, G, corpus)
        base_ans = answer_without_kg(q, corpus)

        rows.append({
            "Query": q,
            "KG Answer": kg_ans["answer_context"],
            "Baseline Answer": base_ans["answer_context"],
            "KG Relations": kg_ans["kg_relations_count"],
            "KG Entity Count": len(kg_ans["kg_entities"]),
            "KG Entity Coverage (%)": entity_coverage(kg_ans["answer_context"], kg_ans["kg_entities"])
        })

    df = pd.DataFrame(rows)
    df.to_csv("../output/evaluation.csv", index=False)

    print("=" * 70)
    print("Evaluation saved to output/evaluation.csv")
    print("=" * 70)
    print(df[["Query", "KG Relations", "KG Entity Count", "KG Entity Coverage (%)"]].to_string(index=False))


if __name__ == "__main__":
    main()