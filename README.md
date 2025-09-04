
# LeadGen CLI
Clean, enrich, score, and segment B2B leads for CRM import 

## Features
- Email validation + de-duplication
- Offline-friendly enrichment (email domain/business email, seniority guess from title, heuristic industry guess)
- Rule-based lead scoring (business emails, seniority, ICP industries)
- Segmentation by region/industry/seniority
- Freshsales-ready CSV export + per-segment CSVs

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python -m leadgen_cli.cli sample/sample_leads.csv -o out
```

Outputs:
- `out/cleaned_enriched.csv`
- `out/freshsales_import.csv` (import-ready)
- `out/segments/*.csv`

## CSV Schema
Minimum input columns (extra columns are allowed):
- `name`, `email`, `company`, `title`, `website`, `country`, `source`

## Roadmap
- API enrichers (Apollo/Clearbit/Cognism/ZoomInfo) via env vars
- Freshsales API write
- Google Ads/SEO performance bridge
- Configurable scoring weights
