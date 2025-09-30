# CLARIN AgenticAI Tutorial

CLARIN ERIC offers access to a wide range of language resources (corpora, lexical databases, metadata, services like concordancers, etc.), and a tutorial should cover realistic use cases that demonstrate how an agent can:

1. Discover resources (metadata, search)
2. Access / retrieve data (e.g. corpora or dictionaries)
3. Process / analyze results

Here are three possible use cases, each as a separate scripts:

## 📓 Practice 1 – Discovering Corpora via the CLARIN Virtual Language Observatory (VLO)

**Objective**: Show how an agent can query the CLARIN VLO API for datasets on a given topic (e.g. "political speeches in German") and return metadata summaries.

1. User gives a natural language query ("Find corpora of spoken Dutch conversations").
1. Agent reformulates it into VLO API search queries.
1. Retrieves matching resources, summarizes metadata (title, description, license, access).
1. Ranks or filters according to user constraints (e.g. "freely available", "XML format").

## 📓 Practice 2 – Accessing and Querying a CLARIN Corpus via Federated Content Search (FCS)

**Objective**: Demonstrate how to use the CLARIN FCS API to retrieve concordances.

1. User gives a request ("Show me occurrences of the word migration in German parliamentary debates").
1. Agent translates it into an FCS query.
1. Queries FCS endpoints (e.g. ParlaMint corpora).
1. Returns KWIC (Keyword-in-Context) lines.
1. Optionally, aggregates frequencies or visualizes trends.

## 📓 Practice 3 – Integrating Lexical Resources (e.g. WordNet or MorphoLex) for Enrichment

**Objective**: Use CLARIN-provided lexical resources to enrich user queries.

1. User asks: "Find corpora where synonyms of democracy appear".
1. Agent queries lexical resources (WordNet, CLARIN lexicons) to expand the query.
1. Performs expanded search via VLO/FCS.
1. Demonstrates how agentic AI can chain tools: lexical resource → corpus search → visualization.

✨ Each pratice:

* Introduce the resource (VLO, FCS, lexicon).
* Explain the API endpoint.
* Show how an LLM-based agent can orchestrate the workflow.
* Include example code (Python, using requests, json, pandas, and possibly langchain or openai for the agentic part).
