from __future__ import annotations
import pandas as pd

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def coerce_dates(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    df = df.copy()
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    return df

def filter_sc(df: pd.DataFrame, uf_col: str = "uf") -> pd.DataFrame:
    df = df.copy()
    if uf_col in df.columns:
        df = df[df[uf_col].astype(str).str.upper().str.strip() == "SC"]
    return df

def basic_missing_treatment(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(how="all")
    df = df.replace(r"^\s*$", pd.NA, regex=True)
    return df

def save_processed(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False, encoding="utf-8")
