"""Clasificación y descripción de las variables de base_consolidada.csv (Grupo C)."""

# Referencia: identificadores, fechas originales y controles de calidad (no son predictoras)
VARS_REFERENCIA = [
    'order_id', 'customer_id', 'customer_unique_id', 'vendedor_principal',
    'order_status', 'estado_pedido',
    'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
    'order_delivered_customer_date', 'order_estimated_delivery_date', 'fecha_limite_despacho',
    'momento_prediccion', 'despacho_observado', 'fecha_inconsistente',
]

# Lo que se predice
VAR_OBJETIVO = 'insatisfecho'

# Solo EDA: se conocen DESPUÉS del momento de predicción (fuga de información)
VARS_FUGA = [
    'review_score', 'tiene_comentario', 'largo_comentario',
    'review_creation_date', 'review_answer_timestamp',
    'dias_entrega_real', 'dias_retraso',
]

# Predictoras
VARS_BINARIAS = ['entrega_tardia', 'despacho_tardio', 'mismo_estado', 'misma_region']

VARS_CATEGORICAS = ['categoria_principal', 'tipo_pago', 'customer_state', 'customer_region',
                    'seller_state', 'seller_region', 'mes_compra', 'dia_semana_compra']

VARS_NUMERICAS = [
    # tiempos
    'dias_entrega_observados', 'dias_anticipacion', 'dias_entrega_estimada',
    'horas_aprobacion', 'dias_hasta_transportista', 'dias_despacho_vs_limite',
    # pedido y productos
    'cant_items', 'cant_productos', 'cant_vendedores', 'precio_total', 'flete_total',
    'ratio_flete_precio', 'peso_total_g', 'volumen_total_cm3', 'fotos_promedio',
    'largo_descripcion_promedio',
    # pago
    'cant_medios_pago', 'cuotas', 'valor_pagado',
    # historial del vendedor
    'vendedor_pedidos_previos', 'vendedor_tasa_retraso_previa', 'vendedor_tasa_insatisf_previa',
]

VARS_PREDICTORAS = VARS_BINARIAS + VARS_CATEGORICAS + VARS_NUMERICAS

DESCRIPCION = {
    'insatisfecho': 'Variable objetivo: 1 si review_score es 1-3, 0 si es 4-5',
    # fuga
    'review_score': 'Puntuación de la reseña (1 a 5)',
    'tiene_comentario': '1 si el cliente escribió un comentario',
    'largo_comentario': 'Cantidad de caracteres del comentario',
    'review_creation_date': 'Fecha de creación de la encuesta',
    'review_answer_timestamp': 'Fecha de respuesta de la encuesta',
    'dias_entrega_real': 'Días reales entre la compra y la entrega',
    'dias_retraso': 'Entrega real - fecha estimada, en días (>0 = tarde)',
    # binarias
    'entrega_tardia': '1 si el pedido llegó después del día estimado',
    'despacho_tardio': '1 si el vendedor despachó después de su fecha límite',
    'mismo_estado': '1 si cliente y vendedor principal están en el mismo estado',
    'misma_region': '1 si cliente y vendedor principal están en la misma región',
    # categóricas
    'categoria_principal': 'Categoría del ítem más caro del pedido',
    'tipo_pago': 'Medio de pago de mayor monto',
    'customer_state': 'Estado (sigla) del cliente',
    'customer_region': 'Región de Brasil del cliente',
    'seller_state': 'Estado (sigla) del vendedor principal',
    'seller_region': 'Región de Brasil del vendedor principal',
    'mes_compra': 'Mes de la compra (1-12)',
    'dia_semana_compra': 'Día de la semana de la compra (0 = lunes)',
    # numéricas
    'dias_entrega_observados': 'Días de entrega hasta el momento de predicción',
    'dias_anticipacion': 'Días que llegó antes de la fecha estimada (0 si se atrasó)',
    'dias_entrega_estimada': 'Plazo de entrega prometido, en días',
    'horas_aprobacion': 'Horas entre la compra y la aprobación del pago',
    'dias_hasta_transportista': 'Días entre la compra y el despacho al transportista',
    'dias_despacho_vs_limite': 'Despacho - fecha límite de despacho, en días (>0 = tarde)',
    'cant_items': 'Cantidad de ítems del pedido',
    'cant_productos': 'Cantidad de productos distintos',
    'cant_vendedores': 'Cantidad de vendedores distintos',
    'precio_total': 'Suma de precios de los ítems (R$)',
    'flete_total': 'Suma del flete (R$)',
    'ratio_flete_precio': 'Flete total / precio total',
    'peso_total_g': 'Peso total de los productos (g)',
    'volumen_total_cm3': 'Volumen total de los productos (cm³)',
    'fotos_promedio': 'Promedio de fotos de los productos',
    'largo_descripcion_promedio': 'Promedio de caracteres de la descripción',
    'cant_medios_pago': 'Cantidad de medios de pago usados',
    'cuotas': 'Cantidad máxima de cuotas',
    'valor_pagado': 'Monto total pagado (R$)',
    'vendedor_pedidos_previos': 'Pedidos previos del vendedor principal',
    'vendedor_tasa_retraso_previa': 'Proporción de entregas tardías previas del vendedor',
    'vendedor_tasa_insatisf_previa': 'Proporción de clientes insatisfechos previos del vendedor',
}