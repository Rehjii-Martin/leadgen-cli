
from typing import Dict, Any

def segment_bucket(lead: Dict[str, Any]) -> str:
    # Example segments by region + industry + seniority
    country = (lead.get("country") or "").upper()
    seniority = (lead.get("seniority") or "unknown").lower()
    industry = (lead.get("industry_guess") or "other").lower()

    # Region
    region = "NA" if country in {"US","CA"} else ("EU" if country in {"GB","DE","FR","ES","IT","NL"} else "ROW")

    # Compose
    return f"{region}:{industry}:{seniority}"
