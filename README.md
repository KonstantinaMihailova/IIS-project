# KG-RAG for Macedonian History

A simple Knowledge Graph–Enriched Question Answering project for the course **Intelligent Information Systems**.

This project builds a **Knowledge Graph (KG)** from a small corpus of Wikipedia texts related to **Macedonian history**, then uses the graph to improve question answering through **KG-based retrieval**.

## Project idea

Large Language Models often answer questions using only parametric knowledge, which can lead to incomplete or hallucinated answers. This project demonstrates a simpler alternative:

- build a small domain-specific Knowledge Graph,
- retrieve relevant entities and subgraphs,
- use them to enrich question answering.

The selected domain is **Macedonian history and geography**, including topics such as:
- North Macedonia
- Alexander the Great
- Skopje
- Ohrid
- Cyril and Methodius
- Samuel of Bulgaria
- Byzantine Empire

## Features

- Named Entity Recognition with **spaCy**
- Knowledge Graph construction with **NetworkX**
- Community-aware graph structure
- KG-based retrieval for question answering
- Baseline vs KG-RAG comparison
- Graph visualization
- Evaluation in CSV and chart form

## Project structure

```text
IIS_KG/
├── data/
│   └── corpus.json
├── output/
│   ├── knowledge_graph.gexf
│   ├── knowledge_graph.png
│   ├── evaluation.csv
│   └── evaluation_chart.png
├── src/
│   ├── kg_builder.py
│   ├── kg_retrieval.py
│   ├── llm_answer.py
│   ├── main.py
│   ├── evaluate.py
│   ├── visualize_graph.py
│   └── visualize_evaluation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies used

- Python
- spaCy
- NetworkX
- Matplotlib
- pandas
- python-louvain

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run the project

Go to the `src` folder and run:

```bash
python main.py
```

This will:
- build the Knowledge Graph,
- answer predefined questions,
- compare KG-RAG with a baseline approach,
- save the graph to `output/knowledge_graph.gexf`.

## Run evaluation

```bash
python evaluate.py
```

This creates:

- `output/evaluation.csv`

## Generate visualizations

### Graph visualization

```bash
python visualize_graph.py
```

Creates:

- `output/knowledge_graph.png`

### Evaluation chart

```bash
python visualize_evaluation.py
```

Creates:

- `output/evaluation_chart.png`

## Example questions

The system currently tests the following questions:

- Where was Alexander the Great born?
- What language do people speak in North Macedonia?
- What is the connection between Cyril and the Slavic alphabet?
- What happened at the Battle of Kleidion?
- What is the UNESCO World Heritage Site near Ohrid?

## Example output

Example console output:

```text
KG-RAG Question Answering Demo
Graph loaded: 62 nodes, 66 edges
```

Example evaluation result:

- Alexander birth: 87.5% entity coverage
- North Macedonia language: 62.5%
- Cyril and Slavic alphabet: 87.5%
- Battle of Kleidion: 62.5%
- UNESCO near Ohrid: 75.0%

## Methodology

1. A small corpus is prepared from Wikipedia summaries.
2. spaCy extracts named entities such as people, places, organizations, and nationalities.
3. A Knowledge Graph is built where:
   - nodes = entities
   - edges = co-occurrence relations inside sentences
4. For each query, the system retrieves relevant nodes from the graph.
5. KG-RAG ranks answer sentences using both:
   - keyword overlap
   - graph entity matches
6. A baseline method ranks sentences using only keyword overlap.

## Limitations

- The corpus is small.
- Relations are based on co-occurrence, not typed semantic relations.
- The system is extractive rather than fully generative.
- Some questions about specific events may still retrieve noisy context.

## Possible improvements

- Use a larger corpus
- Add relation extraction (`born_in`, `located_in`, `fought_at`, etc.)
- Integrate a local LLM for better answer generation
- Support Macedonian-language texts directly
- Add an interactive web interface

## Course context

This project was developed for the course **Intelligent Information Systems** under the topic:

**“Enriching LLM knowledge with Knowledge Graphs in a selected application domain.”**

## Author notes

This repository contains a simplified educational implementation designed to clearly demonstrate the core idea of **Knowledge Graph–Enhanced Retrieval-Augmented Question Answering**.

## License

This project is for educational use.