import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, Markdown
from matplotlib.ticker import FuncFormatter
 
# Constantes que usan las funciones de gráficos
OSCURO = "#2E3440"
miles = FuncFormatter(lambda v, _: f"{v:,.0f}")
 
 
def hist_nominal(ax, s, color, titulo, xlabel="", bins=50, pct=0.99, dos_colas=False):
    """Histograma en escala original, acotado al percentil indicado para que se vea el cuerpo de la distribución."""
    s = s.dropna()
    hi = s.quantile(pct)
    lo = s.quantile(1 - pct) if dos_colas else s.min()
    visible = s[(s >= lo) & (s <= hi)]
    sns.histplot(visible, bins=bins, color=color, edgecolor="white", linewidth=0.4, ax=ax)
    ax.axvline(s.median(), color=OSCURO, ls="--", lw=1.4, label=f"Mediana {s.median():,.1f}")
    ax.axvline(s.mean(), color=OSCURO, ls=":", lw=1.9, label=f"Media {s.mean():,.1f}")
    ax.set_title(titulo)
    ax.set_xlabel(f"{xlabel} | {len(s) - len(visible):,} valores extremos fuera de la vista")
    ax.set_ylabel("Frecuencia")
    ax.xaxis.set_major_formatter(miles)
    ax.yaxis.set_major_formatter(miles)
    ax.legend(frameon=False)
 
 
def barras(ax, serie, color, titulo, horizontal=False, fmt="{:,.0f}", xlabel="", ylabel="", valores=True):
    """Barras con etiquetas de valor."""
    nombres = [str(i) for i in serie.index]
    etiquetas = [fmt.format(v) for v in serie.values]
    if horizontal:
        b = ax.barh(nombres, serie.values, color=color, edgecolor="white")
        ax.invert_yaxis()
        ax.margins(x=0.16)
    else:
        b = ax.bar(nombres, serie.values, color=color, edgecolor="white")
        ax.margins(y=0.13)
    if valores:
        ax.bar_label(b, labels=etiquetas, padding=3, fontsize=9, color=OSCURO)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
 
 
def caja(ax, s, color, titulo, xlabel=""):
    """Boxplot horizontal en escala original."""
    sns.boxplot(x=s.dropna(), ax=ax, color=color, width=0.45, linewidth=1.2,
                flierprops=dict(marker="o", markerfacecolor=color, markeredgecolor="none", markersize=3.5, alpha=0.35))
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.xaxis.set_major_formatter(miles)
 
 
 
def perfil_columnas(df):
    return pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "únicos": df.nunique(),
    })
 
 
def resumen_nulos(dfs):
    filas = []
    for nombre, df in dfs.items():
        nulos = df.isna().sum()
        for col in df.columns:
            if nulos[col] > 0:
                filas.append({"dataset": nombre, "columna": col, "nulos": int(nulos[col]),
                              "pct_nulos": round(nulos[col] / len(df) * 100, 2)})
    return pd.DataFrame(filas)
 
 
def resumen_numerico(df, cols):
    out = df[cols].describe(percentiles=[0.01, 0.25, 0.5, 0.75, 0.99]).T
    out["asimetría"] = df[cols].skew()
    return out
 
 
def cobertura(hijo, col_hijo, padre, col_padre):
    return round(hijo[col_hijo].isin(padre[col_padre]).mean() * 100, 2)
 
 
def mostrar(lineas):
    display(Markdown("\n".join(lineas)))
 
 
def tabla_outliers(df, cols):
    filas = []
    for c in cols:
        s = df[c].dropna()
        q1, q3 = s.quantile([0.25, 0.75])
        iqr = q3 - q1
        mod = (s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)
        ext = (s < q1 - 3 * iqr) | (s > q3 + 3 * iqr)
        filas.append({
            "variable": c, "n": len(s), "Q1": q1, "Q3": q3,
            "límite_inf (1,5)": q1 - 1.5 * iqr, "límite_sup (1,5)": q3 + 1.5 * iqr,
            "moderados": int(mod.sum()), "% moderados": round(mod.mean() * 100, 2),
            "extremos": int(ext.sum()), "% extremos": round(ext.mean() * 100, 2),
            "p99": s.quantile(0.99), "máximo": s.max(),
        })
    return pd.DataFrame(filas).set_index("variable")
 
 
def flag_outlier(s, k=3.0):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    return ((s < q1 - k * iqr) | (s > q3 + k * iqr)).fillna(False)
 
 
 