from __future__ import annotations
import os
import pandas as pd
import matplotlib.pyplot as plt

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def line_plot(df: pd.DataFrame, x: str, y: str, title: str, outpath: str) -> None:
    ensure_dir(os.path.dirname(outpath))
    plt.figure()
    plt.plot(df[x], df[y])
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()

def bar_plot(df: pd.DataFrame, x: str, y: str, title: str, outpath: str, top_n: int = 15) -> None:
    ensure_dir(os.path.dirname(outpath))
    d2 = df.sort_values(y, ascending=False).head(top_n)
    plt.figure()
    plt.bar(d2[x].astype(str), d2[y])
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
