import spacy
import networkx as nx
import json
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

KEEP_LABELS = {"PERSON", "ORG", "GPE", "LOC", "NORP", "EVENT", "DATE", "WORK_OF_ART"}


def extract_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        if ent.label_ in KEEP_LABELS:
            clean = ent.text.strip().strip("'\"()[]")
            if len(clean) > 2:
                entities.append((clean, ent.label_))

    return entities


def extract_relations(text, window=2):
    doc = nlp(text)
    relations = []

    for sent in doc.sents:
        sent_entities = []

        for ent in sent.ents:
            if ent.label_ in KEEP_LABELS:
                clean = ent.text.strip().strip("'\"()[]")
                if len(clean) > 2:
                    sent_entities.append((clean, ent.label_))

        for i in range(len(sent_entities)):
            for j in range(i + 1, min(i + window + 1, len(sent_entities))):
                a, la = sent_entities[i]
                b, lb = sent_entities[j]
                if a != b:
                    relations.append((a, b, la, lb))

    return relations


def build_graph(corpus_path):
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    G = nx.Graph()
    edge_weights = defaultdict(int)

    for topic, text in corpus.items():
        entities = extract_entities(text)

        for name, label in entities:
            if name not in G:
                G.add_node(name, label=label, source=topic)

        relations = extract_relations(text)

        for a, b, la, lb in relations:
            edge_weights[(a, b)] += 1

    for (a, b), weight in edge_weights.items():
        if G.has_node(a) and G.has_node(b):
            G.add_edge(a, b, weight=weight)

    return G, corpus