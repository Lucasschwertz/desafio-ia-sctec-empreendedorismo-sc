from __future__ import annotations
import pandas as pd

def add_year_month(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    df = df.copy()
    df["ano_mes"] = df[date_col].dt.to_period("M").astype(str)
    return df

def monthly_series(df: pd.DataFrame, date_col: str, value_col: str) -> pd.DataFrame:
    df = df.copy()
    if "ano_mes" not in df.columns:
        df = add_year_month(df, date_col)
    out = df.groupby("ano_mes", as_index=False)[value_col].sum()
    out = out.sort_values("ano_mes")
    return out

def compute_balance(open_df: pd.DataFrame, close_df: pd.DataFrame, key_col: str = "ano_mes",
                    open_col: str = "aberturas", close_col: str = "fechamentos") -> pd.DataFrame:
    merged = open_df.merge(close_df, on=key_col, how="outer").fillna(0)
    merged["saldo"] = merged[open_col] - merged[close_col]
    return merged.sort_values(key_col)
