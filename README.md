
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

### Example Output (`freshsales_import.csv`)

| First name | Last name | Email                    | Company           | Job title       | Website              | Country | Lead score | Lifecycle stage | Source     | Tags             |
|------------|-----------|--------------------------|-------------------|-----------------|----------------------|---------|------------|-----------------|------------|-----------------|
| Ada        | Lovelace  | ada@analyticalengine.org | Analytical Engine | Chief Scientist | analyticalengine.org | GB      | 53         | Lead            | web-scrape | EU:other:c_level |
| Grace      | Hopper    | grace@navy.mil           | US Navy           | Director        | navy.mil             | US      | 53         | Lead            | referral   | NA:other:c_level |
| Rick       | Sanchez   | rick@rickandmorty.com    | Citadel Labs      | VP Engineering  | rickandmorty.com     | US      | 48         | Lead            | partner    | NA:other:vp      |
| Morty      | Smith     | morty@outlook.com        | Citadel Labs      | Intern          | rickandmorty.com     | US      | 16         | Lead            | partner    | NA:other:ic      |
| Alan       | Turing    | turing@gmail.com         | Bletchley Park    | Researcher      | bletchley.org        | GB      | 13         | Lead            | conference | EU:other:other   |


## CSV Schema
Minimum input columns (extra columns are allowed):
- `name`, `email`, `company`, `title`, `website`, `country`, `source`

## Roadmap
- API enrichers (Apollo/Clearbit/Cognism/ZoomInfo) via env vars
- Freshsales API write
- Google Ads/SEO performance bridge
- Configurable scoring weights
