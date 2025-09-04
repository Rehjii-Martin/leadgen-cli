
"""
"Enrichers" are modular functions that augment a lead dict.
In production scenario, API might be better suited.
"""
from typing import Dict, Any, Optional
from .utils import domain_from_email, business_email_domain

SENIORITY_KEYWORDS = {
    "c_level": ["chief","ceo","cto","cfo","coo","cio","cmo","cso","cpo"],
    "vp": ["vp","vice president"],
    "director": ["director","head"],
    "manager": ["manager","lead"],
    "ic": ["engineer","specialist","analyst","associate","developer","designer","intern"]
}

INDUSTRY_GUESS = {
    "retail": ["retail","shop","store","boutique","ecommerce"],
    "hospitality": ["hotel","hostel","inn","hospitality","resort","bar","restaurant","cafe"],
    "music": ["studio","music","sound","audio","dj","venue"],
    "technology": ["tech","software","cloud","saas","data","ai"]
}

def guess_seniority(title: Optional[str]) -> str:
    if not title: return "unknown"
    t = title.lower()
    for k, kws in SENIORITY_KEYWORDS.items():
        for kw in kws:
            if kw in t:
                return k
    return "other"

def guess_industry(company: Optional[str], website: Optional[str]) -> str:
    hay = " ".join([x for x in [company, website] if x]).lower()
    for ind, kws in INDUSTRY_GUESS.items():
        if any(kw in hay for kw in kws):
            return ind
    return "other"

def enrich_lead(lead: Dict[str, Any]) -> Dict[str, Any]:
    # Add derived fields: email_domain, is_business_email, seniority, industry_guess
    email = lead.get("email","")
    domain = domain_from_email(email) or ""
    lead["email_domain"] = domain
    lead["is_business_email"] = business_email_domain(domain)
    lead["seniority"] = guess_seniority(lead.get("title") or "")
    lead["industry_guess"] = guess_industry(lead.get("company") or "", lead.get("website") or "")
    return lead
