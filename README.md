# KG-RAG for Macedonian History

A simple **Knowledge Graph–Enriched Question Answering** project developed for the course **Intelligent Information Systems**.

This project builds a small **Knowledge Graph (KG)** from Wikipedia-based texts related to **Macedonian history and geography**, then uses graph-based retrieval to improve question answering over the corpus.

## Project idea

Large Language Models can produce incomplete or hallucinated answers when they rely only on internal parametric knowledge. This project demonstrates a simpler and more controlled alternative:

- Build a small domain-specific Knowledge Graph
- Retrieve relevant entities and subgraphs
- Use them to improve question answering
- Compare the result with a text-only baseline

## Domain

The selected domain is **Macedonian history and geography**, including topics such as:

- Republic of North Macedonia
- Alexander the Great
- Skopje
- Ohrid
- Macedonian language
- Cyril and Methodius
- Samuel and the Macedonian medieval context
- Byzantine Empire

## Features

- Named Entity Recognition with **spaCy**
- Knowledge Graph construction with **NetworkX**
- Query-based node retrieval
- KG-RAG vs baseline comparison
- Graph visualization in PNG and GEXF format
- Evaluation output in CSV and chart form

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

Clone the repository and install the required dependencies:

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

- Build the Knowledge Graph
- Answer predefined questions
- Compare **KG-RAG** with a baseline method
- Save the graph to `output/knowledge_graph.gexf`

## Run evaluation

```bash
python evaluate.py
```

This creates:

- `output/evaluation.csv`

## Generate visualizations

### Knowledge Graph visualization

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
- Who was Samuel and what is his connection to Macedonia?
- What is the UNESCO World Heritage Site near Ohrid?

## Methodology

1. A small corpus is prepared from Wikipedia summaries.
2. **spaCy** extracts named entities such as people, places, organizations, and nationalities.
3. A **Knowledge Graph** is built where:
   - nodes represent entities
   - edges represent co-occurrence relations inside sentences
4. For each query, the system retrieves relevant nodes from the graph.
5. **KG-RAG** ranks supporting sentences using:
   - keyword overlap
   - graph entity matches
6. A baseline method ranks sentences using only keyword overlap.

## Results

The project generates:

- A domain-specific Knowledge Graph
- A `.gexf` graph file for further inspection
- A `.png` graph visualization
- A CSV file with evaluation metrics
- A bar chart for entity coverage across questions

Example evaluation results:

- Alexander birth: 87.5% entity coverage
- North Macedonia language: 62.5%
- Cyril and Slavic alphabet: 87.5%
- Samuel and Macedonia: 62.5%
- UNESCO near Ohrid: 75.0%

## Notes on the Samuel update

The corpus was refined to better reflect **Samuel in a Macedonian medieval context**, instead of keeping an overly direct connection to Bulgaria in the graph. This improved the thematic structure of the Knowledge Graph and produced a clearer historical cluster around **Samuel**, **Macedonian**, and **Slavic** entities.

## Limitations

- The corpus is relatively small
- Relations are based on **co-occurrence**, not typed semantic relations
- The system is **extractive**, not fully generative
- Some questions may still retrieve noisy context

## Possible improvements

- Use a larger corpus
- Add typed relation extraction such as `born_in`, `located_in`, or `fought_at`
- Integrate a local LLM for better answer generation
- Support Macedonian-language texts directly
- Add an interactive web interface

## Course context

This project was developed for the course **Intelligent Information Systems** under the topic:

**“Enriching LLM knowledge with Knowledge Graphs in a selected application domain.”**

## Author note

This repository contains a simplified educational implementation designed to clearly demonstrate the core idea of **Knowledge Graph–Enhanced Retrieval-Augmented Question Answering**.

## License

This project is intended for educational use.
