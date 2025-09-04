
import pandas as pd
from leadgen_cli.pipeline import clean_and_enrich

def test_clean_and_enrich_basic():
    df = pd.DataFrame([
        {"name":"Ada Lovelace","email":"ada@analyticalengine.org","company":"Analytical Engine","title":"Chief Scientist","website":"analyticalengine.org","country":"GB","source":"demo"},
        {"name":"Alan Turing","email":"turing@gmail.com","company":"Bletchley","title":"Researcher","website":"bletchley.uk","country":"GB","source":"demo"},
        {"name":"Grace Hopper","email":"grace@navy.mil","company":"US Navy","title":"Director","website":"navy.mil","country":"US","source":"demo"},
        {"name":"Bad Email","email":"not-an-email","company":"X","title":"","website":"","country":"US","source":"demo"},
    ])
    out = clean_and_enrich(df)
    # invalid email removed
    assert len(out) == 3
    # scores exist
    assert out["lead_score"].notna().all()
    # segments exist
    assert out["segment"].str.len().gt(0).all()
