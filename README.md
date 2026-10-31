# Proyecto-Mineria-de-datos

**Predicción de Insatisfacción del Cliente — Olist (Grupo C)**

Minería de Datos y Aprendizaje Automático — UNLP
Integrantes: Vivas Escobar, Cinthia · Bailon Trujillo, Carolina

## Objetivo
Clasificación binaria: predecir si un cliente quedará insatisfecho (review_score 1–3).

## Datos
Fuente: [Olist Brazilian E-Commerce Public Dataset (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Archivos utilizados (carpeta `data/`):

| Archivo | Contenido |
|---|---|
| `olist_orders_dataset.csv` | Pedidos: estado y fechas de compra, aprobación y entrega |
| `olist_order_items_dataset.csv` | Ítems de cada pedido: producto, vendedor, precio y flete |
| `olist_order_payments_dataset.csv` | Pagos: medio de pago, cuotas y monto |
| `olist_order_reviews_dataset.csv` | Reseñas: puntuación 1–5 (origen de la variable objetivo) |
| `olist_customers_dataset.csv` | Clientes: ciudad y estado |
| `olist_products_dataset.csv` | Productos: categoría, dimensiones, peso y fotos |

Descartados: `olist_geolocation_dataset.csv`, `olist_sellers_dataset.csv` y
`product_category_name_translation.csv`.

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
