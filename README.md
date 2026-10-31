# Proyecto-Mineria-de-datos

**Predicción de Insatisfacción del Cliente — Olist (Grupo C)**

Minería de Datos y Aprendizaje Automático — UNLP
Integrantes: Vivas Escobar, Cinthia · Bailon Trujillo, Carolina

## Objetivo
Clasificación binaria: predecir si un cliente quedará insatisfecho (review_score 1–3).

## Datos
Olist Brazilian E-Commerce (Kaggle). Tablas usadas: orders, order_items,
order_payments, order_reviews, customers, products (carpeta `data/`).

## Estructura
- `data/` — CSV originales · `data/procesado/` — salidas de los notebooks (no se suben)
- `notebooks/` — 01 carga y traducción → 02 consolidación → 03 EDA → 04 preprocesamiento → 05 modelado
- `src/` — funciones reutilizables
- `informe/` — informe final en PDF y figuras
- `docs/` — propuesta y enunciado del TP

## Cómo ejecutar
```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```
Correr los notebooks de `notebooks/` en orden (01 → 05).
