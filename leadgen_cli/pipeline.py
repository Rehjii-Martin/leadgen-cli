
import pandas as pd
from typing import List, Dict, Any
from .utils import is_valid_email, split_name
from .enrichers import enrich_lead
from .scoring import lead_score
from .segment import segment_bucket

REQUIRED_COLS = ["name","email","company","title","website","country","source"]

def load_leads(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Normalize expected columns
    for c in REQUIRED_COLS:
        if c not in df.columns:
            df[c] = ""
    # Create first/last names if missing
    if "first_name" not in df.columns: df["first_name"] = ""
    if "last_name" not in df.columns: df["last_name"] = ""
    name_splits = df["name"].apply(split_name)
    df["first_name"] = df["first_name"].mask(df["first_name"].eq(""), name_splits.apply(lambda x: x[0]))
    df["last_name"] = df["last_name"].mask(df["last_name"].eq(""), name_splits.apply(lambda x: x[1]))
    return df

def clean_and_enrich(df: pd.DataFrame) -> pd.DataFrame:
    # Drop rows with invalid emails
    df = df[df["email"].apply(is_valid_email)].copy()
    # Deduplicate by email (keep highest-completeness row)
    df = df.sort_values(by=["company","title","website"], ascending=[False, False, False])
    df = df.drop_duplicates(subset=["email"], keep="first")
    # Enrich + score + segment
    records: List[Dict[str, Any]] = df.to_dict(orient="records")
    enriched = []
    for r in records:
        r = enrich_lead(r)
        r["lead_score"] = lead_score(r)
        r["segment"] = segment_bucket(r)
        enriched.append(r)
    return pd.DataFrame(enriched)

def freshsales_export(df: pd.DataFrame) -> pd.DataFrame:
    """
    Map to a Freshsales (or similar) import template.
    Minimal fields used for a clean import.
    """
    out = pd.DataFrame({
        "First name": df["first_name"],
        "Last name": df["last_name"],
        "Email": df["email"],
        "Company": df["company"],
        "Job title": df["title"],
        "Website": df["website"],
        "Country": df["country"],
        "Lead score": df["lead_score"],
        "Lifecycle stage": "Lead",
        "Source": df.get("source", ""),
        "Tags": df["segment"]
    })
    return out.sort_values(by="Lead score", ascending=False)
