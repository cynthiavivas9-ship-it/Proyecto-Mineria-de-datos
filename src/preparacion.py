"""Funciones de preparación de datos del proyecto Olist (Grupo C)."""
import os
import numpy as np
import pandas as pd

from diccionarios import CATEGORIAS_ES, ESTADO_PEDIDO_ES, TIPO_PAGO_ES, ESTADOS_BR

ARCHIVOS = {
    'orders':    'olist_orders_dataset.csv',
    'items':     'olist_order_items_dataset.csv',
    'payments':  'olist_order_payments_dataset.csv',
    'reviews':   'olist_order_reviews_dataset.csv',
    'customers': 'olist_customers_dataset.csv',
    'products':  'olist_products_dataset.csv',
    'sellers':   'olist_sellers_dataset.csv',
}

# Columnas de fecha de cada tabla
FECHAS = {
    'orders':  ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                'order_delivered_customer_date', 'order_estimated_delivery_date'],
    'items':   ['shipping_limit_date'],
    'reviews': ['review_creation_date', 'review_answer_timestamp'],
}

# Códigos postales como texto para no perder los ceros de adelante ("01037")
TEXTO = {'customer_zip_code_prefix': str, 'seller_zip_code_prefix': str}


def cargar_crudos(ruta):
    """Lee los 7 CSV originales, con las fechas ya convertidas a tipo fecha."""
    dfs = {}
    for nombre, archivo in ARCHIVOS.items():
        dfs[nombre] = pd.read_csv(os.path.join(ruta, archivo), dtype=TEXTO,
                                  parse_dates=FECHAS.get(nombre, []))
    return dfs


def traducir(dfs):
    """Agrega columnas traducidas al español (se conservan las originales)."""
    dfs = {nombre: df.copy() for nombre, df in dfs.items()}

    dfs['products']['categoria_producto'] = (dfs['products']['product_category_name']
                                             .map(CATEGORIAS_ES).fillna('sin_categoria'))
    dfs['orders']['estado_pedido'] = dfs['orders']['order_status'].map(ESTADO_PEDIDO_ES)
    dfs['payments']['tipo_pago'] = dfs['payments']['payment_type'].map(TIPO_PAGO_ES)

    # Región de clientes y vendedores a partir de la sigla del estado
    region = {sigla: datos[1] for sigla, datos in ESTADOS_BR.items()}
    dfs['customers']['customer_region'] = dfs['customers']['customer_state'].map(region)
    dfs['sellers']['seller_region'] = dfs['sellers']['seller_state'].map(region)
    return dfs


def historial_vendedor(g):
    """Historial de un vendedor para cada uno de sus pedidos,
    usando solo eventos ocurridos ANTES de la fecha de compra (sin fuga de información)."""
    g = g.copy()
    compra = g['order_purchase_timestamp'].values

    # 1) Pedidos recibidos antes de esta compra
    g['vendedor_pedidos_previos'] = np.searchsorted(np.sort(compra), compra, side='left')

    # 2) Tasa de retraso: entre los pedidos ya entregados al momento de la compra
    ord_ent = g.sort_values('order_delivered_customer_date')
    tardias_acum = np.concatenate([[0], np.cumsum(ord_ent['entrega_tardia'].values)])
    k = np.searchsorted(ord_ent['order_delivered_customer_date'].values, compra, side='left')
    g['vendedor_tasa_retraso_previa'] = np.where(k > 0, tardias_acum[k] / np.maximum(k, 1), np.nan)

    # 3) Tasa de insatisfacción: entre las reseñas ya respondidas al momento de la compra
    ord_res = g.sort_values('review_answer_timestamp')
    insat_acum = np.concatenate([[0], np.cumsum(ord_res['insatisfecho'].values)])
    k = np.searchsorted(ord_res['review_answer_timestamp'].values, compra, side='left')
    g['vendedor_tasa_insatisf_previa'] = np.where(k > 0, insat_acum[k] / np.maximum(k, 1), np.nan)
    return g


# Fechas de la base consolidada (para leerla desde otros notebooks)
FECHAS_BASE = FECHAS['orders'] + ['fecha_limite_despacho', 'review_answer_timestamp',
                                  'momento_prediccion', 'despacho_observado']


def leer_base(ruta_archivo):
    """Lee base_consolidada.csv con las fechas convertidas."""
    return pd.read_csv(ruta_archivo, parse_dates=FECHAS_BASE)