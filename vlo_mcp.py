import pandas as pd
from vlo import query_vlo, parse_results

def vlo_search(query: str, rows: int = 5) -> dict:
    """
    Search CLARIN VLO for resources matching the query.
    Args:
        query (str): Search query, e.g. 'languageCode:code:deu availability:PUB'
        rows (int): Number of results to return
    Returns:
        dict: Results as a list of records
    """
    vlo_json = query_vlo(query, rows)
    df = parse_results(vlo_json)
    # Convert DataFrame to list of dicts for MCP
    return {
        "results": df.to_dict(orient="records"),
        "count": len(df)
    }

# MCP tool descriptor
MCP_TOOL = {
    "name": "vlo_search",
    "description": "Search CLARIN VLO for language resources. Use ISO language codes (e.g. code:deu for German).",
    "parameters": {
        "query": {
            "type": "string",
            "description": "VLO search query, e.g. 'parliamentary speeches languageCode:code:deu availability:PUB'"
        },
        "rows": {
            "type": "integer",
            "description": "Number of results to return",
            "default": 5
        }
    },
    "output": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string"},
                    "Description": {"type": "string"},
                    "Language": {"type": "string"},
                    "Availability": {"type": "string"},
                    "URL": {"type": "string"}
                }
            }
        },
        "count": {"type": "integer"}
    },
    "function": vlo_search
}

# If you want to expose this via MCP server, you would register MCP_TOOL in your agentic framework.