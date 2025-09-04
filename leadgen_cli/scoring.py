
from typing import Dict, Any

def lead_score(lead: Dict[str, Any]) -> int:
    score = 0
    # Basic completeness
    if lead.get("email"): score += 10
    if lead.get("company"): score += 5
    if lead.get("website"): score += 3

    # Business email preference
    if lead.get("is_business_email"):
        score += 15
    else:
        score -= 5

    # Seniority weighting
    s = (lead.get("seniority") or "").lower()
    if s == "c_level": score += 20
    elif s == "vp": score += 15
    elif s == "director": score += 12
    elif s == "manager": score += 8
    elif s == "ic": score += 3

    # Industry relevance bump (retail/hospitality/music/technology = closer to SoundMachine ICP)
    ind = (lead.get("industry_guess") or "").lower()
    if ind in {"retail","hospitality","music","technology"}:
        score += 7

    # Penalize poor data quality
    if not lead.get("first_name") and not lead.get("last_name"):
        score -= 3
    return score
