from kg_retrieval import retrieve_relevant_nodes, get_subgraph_context


def split_sentences(text):
    sentences = []
    for s in text.replace("\n", " ").split("."):
        s = s.strip()
        if len(s) > 25:
            sentences.append(s)
    return sentences


def normalize_tokens(text):
    text = text.lower().replace("?", "").replace(",", "").replace(":", "")
    return set(text.split())


def score_sentence_baseline(sentence, query_tokens):
    sent_tokens = normalize_tokens(sentence)
    overlap = len(query_tokens & sent_tokens)
    return overlap


def score_sentence_with_kg(sentence, query_tokens, kg_entities):
    sent_tokens = normalize_tokens(sentence)
    sentence_lower = sentence.lower()

    score = 0

    keyword_overlap = len(query_tokens & sent_tokens)
    score += keyword_overlap * 2

    entity_hits = 0
    for ent in kg_entities:
        if ent.lower() in sentence_lower:
            entity_hits += 1

    score += entity_hits * 3

    if keyword_overlap > 0 and entity_hits > 0:
        score += 4

    return score


def answer_with_kg(query, G, corpus, top_k=8):
    relevant_nodes = retrieve_relevant_nodes(G, query, top_k=top_k)
    subgraph = get_subgraph_context(G, relevant_nodes)

    query_tokens = normalize_tokens(query)
    all_sentences = []

    for _, text in corpus.items():
        all_sentences.extend(split_sentences(text))

    scored_sentences = []
    for sent in all_sentences:
        score = score_sentence_with_kg(sent, query_tokens, relevant_nodes)
        if score > 0:
            scored_sentences.append((score, sent))

    scored_sentences.sort(key=lambda x: x[0], reverse=True)

    top_sentences = []
    seen = set()
    for score, sent in scored_sentences:
        if sent not in seen:
            top_sentences.append(sent)
            seen.add(sent)
        if len(top_sentences) == 3:
            break

    return {
        "query": query,
        "kg_entities": relevant_nodes,
        "kg_relations_count": subgraph.number_of_edges(),
        "supporting_sentences": top_sentences,
        "answer_context": ". ".join(top_sentences) + "." if top_sentences else "No answer found."
    }


def answer_without_kg(query, corpus):
    query_tokens = normalize_tokens(query)
    all_sentences = []

    for _, text in corpus.items():
        all_sentences.extend(split_sentences(text))

    scored_sentences = []
    for sent in all_sentences:
        score = score_sentence_baseline(sent, query_tokens)
        if score > 0:
            scored_sentences.append((score, sent))

    scored_sentences.sort(key=lambda x: x[0], reverse=True)

    top_sentences = []
    seen = set()
    for score, sent in scored_sentences:
        if sent not in seen:
            top_sentences.append(sent)
            seen.add(sent)
        if len(top_sentences) == 3:
            break

    return {
        "query": query,
        "answer_context": ". ".join(top_sentences) + "." if top_sentences else "No answer found."
    }