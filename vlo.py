# Notebook 1 – Discovering Corpora via CLARIN Virtual Language Observatory (VLO)

# --- Introduction ---
# In this tutorial, we will demonstrate how to use an agentic AI workflow to discover language
# resources (corpora, lexical data, etc.) via the CLARIN VLO (Virtual Language Observatory).
#
# VLO exposes metadata for thousands of resources across CLARIN centres. We can access it
# programmatically via its search API.
#
# Workflow:
# 1. User provides a natural language query (e.g. "Find corpora of spoken Dutch conversations").
# 2. The agent interprets and reformulates it into VLO API parameters.
# 3. We query the API and retrieve matching resources.
# 4. Agent summarizes and filters results.

# --- Setup ---
import requests
import pandas as pd

# Define VLO API base
VLO_API = "https://beta-vlo.clarin.eu/api/records"

# --- Step 1: Define a helper for querying VLO ---
def query_vlo(query: str, rows: int = 10):
    """Query the CLARIN VLO API with a keyword search."""
    params = {
        "q": query,     # full-text search query
        "size": rows,   # number of results
        "fq": "title,collection,description,organisation,availability,languageName,landingPage"
    }
    r = requests.get(VLO_API, params=params)
    r.raise_for_status()
    return r.json()

# --- Step 2: Parse results into a DataFrame ---
def parse_results(vlo_json):
    records = vlo_json.get("records", [])
    data = []
    for rec in records:
        fields = rec.get("fields", {})
        data.append({
            "Name": fields.get("name", [""])[0] if fields.get("name") else "",
            "Description": fields.get("description", [""])[0] if fields.get("description") else "",
            "Language": fields.get("languageCode", [""])[0] if fields.get("languageCode") else "",
            "Availability": fields.get("availability", [""])[0] if fields.get("availability") else fields.get("licenseType", [""])[0] if fields.get("licenseType") else "",
            "URL": fields.get("_selfLink", [""])[0] if fields.get("_selfLink") else "",
        })
    return pd.DataFrame(data)

# --- Step 3: Example query ---
example_query = "spoken Dutch conversations"
vlo_json = query_vlo(example_query, rows=5)
df = parse_results(vlo_json)
print("VLO Search Results------------------:\n", df)

# import caas_jupyter_tools
# display = caas_jupyter_tools.display_dataframe_to_user
# display("VLO Search Results", df)
print(df.head())

# --- Step 4: Agentic AI layer (conceptual) ---
# In a real agentic workflow, an LLM could:
# - Take a natural query ("I want freely available corpora of political speeches in German").
# - Expand the search terms (synonyms, related keywords).
# - Add filters (availability = open access, language = German).
# - Call query_vlo() with refined parameters.
# - Summarize results for the user.

# Example of a refined search:
refined_query = "parliamentary speeches languageCode:code:deu availability:PUB"
vlo_json_refined = query_vlo(refined_query, rows=5)
df_refined = parse_results(vlo_json_refined)
print("Refined VLO Search Results:\n", df_refined)

# --- Next steps for the reader ---
# - Try different queries in your own language/topic of interest.
# - Add filters (e.g. specify "availability:public" for open access resources).
# - Integrate this workflow with an LLM (via OpenAI, LangChain, etc.) to build a true agent
#   that interprets user intent and reformulates queries automatically.

# This concludes Notebook 1.
