
import argparse, os, sys, pandas as pd
from .pipeline import load_leads, clean_and_enrich, freshsales_export

def main(argv=None):
    parser = argparse.ArgumentParser(description="LeadGen CLI — clean, enrich, score, and export leads for CRM import.")
    parser.add_argument("input_csv", help="Path to raw leads CSV (columns: name,email,company,title,website,country,source,...)")
    parser.add_argument("-o","--outdir", default="leadgen_out", help="Output directory (default: leadgen_out)")
    args = parser.parse_args(argv)

    os.makedirs(args.outdir, exist_ok=True)
    print(f"[LeadGen] Loading {args.input_csv} ...")
    df = load_leads(args.input_csv)
    print(f"[LeadGen] {len(df)} rows loaded")

    print("[LeadGen] Cleaning, enriching, scoring...")
    df2 = clean_and_enrich(df)
    print(f"[LeadGen] {len(df2)} valid leads after cleaning")

    # Save intermediate
    cleaned_path = os.path.join(args.outdir, "cleaned_enriched.csv")
    df2.to_csv(cleaned_path, index=False)
    print(f"[LeadGen] Wrote {cleaned_path}")

    # Export for Freshsales/ActiveCampaign-like import
    export_df = freshsales_export(df2)
    export_path = os.path.join(args.outdir, "freshsales_import.csv")
    export_df.to_csv(export_path, index=False)
    print(f"[LeadGen] Wrote {export_path}")

    # Also write per-segment CSVs
    seg_dir = os.path.join(args.outdir, "segments")
    os.makedirs(seg_dir, exist_ok=True)
    for seg, sub in df2.groupby("segment"):
        safe = seg.replace(":","-")
        sub.to_csv(os.path.join(seg_dir, f"{safe}.csv"), index=False)
    print(f"[LeadGen] Wrote per-segment CSVs to {seg_dir}")

    print("[LeadGen] Done.")

if __name__ == "__main__":
    main()
