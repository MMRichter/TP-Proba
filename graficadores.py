import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------FUNCIONES GENERALES--------------------------------------------
# Funcion para mostrar tablas renderizadas con matplotlib
def mostrar_tabla_renderizada(tabla, titulo="Tabla"):
    filas = len(tabla)
    columnas = len(tabla.columns)

    alto = max(3, filas * 0.4)
    ancho = max(6, columnas * 2)

    fig, ax = plt.subplots(figsize=(ancho, alto))
    ax.axis('off')
    ax.set_title(titulo, fontsize=14, pad=15)

    tabla_plot = ax.table(
        cellText=tabla.values,
        colLabels=tabla.columns,
        cellLoc='center',
        loc='center'
    )

    # Ajuste de tamaños
    tabla_plot.auto_set_font_size(False)
    tabla_plot.set_fontsize(12)
    tabla_plot.scale(1, 1.4)
    tabla_plot.auto_set_column_width(range(columnas))

    plt.tight_layout()
    plt.show()

# Tabla de frecuencias cuantitativa discreta
def armar_tabla_frecuencias_cuantitativa_discreta(df, encabezado):
    columnas_tabla = [encabezado, "fi", "fir", "Fa ↑", "Fa ↑(%)"]
    
    # Orden natural de valores
    frec_abs = df[encabezado].value_counts().sort_index()
    frec_rel = frec_abs / frec_abs.sum()
    frec_abs_acum = frec_abs.cumsum()
    frec_rel_acum = frec_rel.cumsum() * 100

    tabla = pd.DataFrame({
        columnas_tabla[0]: frec_abs.index,
        columnas_tabla[1]: frec_abs.values,
        columnas_tabla[2]: frec_rel.round(4),
        columnas_tabla[3]: frec_abs_acum,
        columnas_tabla[4]: frec_rel_acum.round(2)
    })

    print(f"\nTabla de frecuencias: {encabezado}")
    print(tabla.to_string(index=False))
    mostrar_tabla_renderizada(tabla, f"Tabla de frecuencias: {encabezado}")

    # ================================
    #  Medidas de resumen
    serie = df[encabezado].dropna()
    medidas = {
        "Muestra": serie.count(),
        "Media": serie.mean(),
        "Mediana": serie.median(),
        "Moda": serie.mode().iloc[0] if not serie.mode().empty else None,
        "Varianza": serie.var(),
        "Desvío estándar": serie.std(),
        "Mínimo": serie.min(),
        "Máximo": serie.max(),
        "Rango": serie.max() - serie.min(),
        "Q1": serie.quantile(0.25),
        "Q2": serie.quantile(0.50),
        "Q3": serie.quantile(0.75),
        "Q4": serie.quantile(1.0)
    }
    resumen = pd.DataFrame(medidas, index=["Resumen"]).T
    resumen_reset = resumen.reset_index()

    print(f"\nMedidas de resumen {encabezado}")
    print(resumen.to_string(header=False))
    resumen_reset.columns = ["Medida", "Valor"]
    mostrar_tabla_renderizada(resumen_reset, f"Medidas de resumen: {encabezado}")

    # ================================
    #  Gráfico de barras (frecuencia absoluta)
    plt.figure(figsize=(8,5))
    bars = plt.bar(frec_abs.index, frec_abs.values)

    # Etiquetas arriba de barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                 ha='center', va='bottom')

    plt.title(f"Distribución de {encabezado}")
    plt.xlabel(encabezado)
    plt.ylabel("Frecuencia absoluta")
    plt.tight_layout()
    plt.show()

    # ================================
    #  Ojiva (frecuencia relativa acumulada)
    plt.figure(figsize=(8,5))
    plt.plot(frec_rel_acum.index, frec_rel_acum.values, marker='o', linestyle='-', linewidth=2)
    plt.title(f"Ojiva de {encabezado}")
    plt.xlabel(encabezado)
    plt.ylabel("Frecuencia relativa acumulada (%)")
    plt.grid(alpha=0.3)
    plt.ylim(0, 105)
    plt.tight_layout()
    plt.show()

    return tabla, resumen


# Tabla de frecuencias cualitativa ordinal
def armar_tabla_frecuencias_cualitativa_ordinal(df, encabezado, jerarquias):
    columnas_tabla = [encabezado, "fi", "fir", "Fa ↑", "Fa ↑(%)"]
    
    frec_abs = df[encabezado].value_counts().reindex(jerarquias).fillna(0)
    frec_rel = frec_abs / frec_abs.sum()
    frec_abs_acum = frec_abs.cumsum()
    frec_rel_acum = frec_rel.cumsum() * 100

    tabla = pd.DataFrame({
        columnas_tabla[0]: frec_abs.index,
        columnas_tabla[1]: frec_abs.values,
        columnas_tabla[2]: frec_rel.round(4),
        columnas_tabla[3]: frec_abs_acum,
        columnas_tabla[4]: frec_rel_acum.round(2)
    })

    print(f"\nTabla de frecuencias: {encabezado}")
    print(tabla.to_string(index=False))
    mostrar_tabla_renderizada(tabla, f"Tabla de frecuencias: {encabezado}")

    # ===========================
    # Gráfico de barras ordenado
    plt.figure(figsize=(8,5))
    bars = plt.bar(frec_abs.index, frec_abs.values)

    # Etiquetas encima de las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                 ha='center', va='bottom', fontsize=9)

    plt.title(f"Distribución de {encabezado}")
    plt.xlabel(encabezado)
    plt.ylabel("Frecuencia absoluta (fi)")
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    plt.show()

    # ===========================
    #  Medidas resumen ordinales
    jerarquia_map = {valor: i+1 for i, valor in enumerate(jerarquias)}
    valores_numericos = df[encabezado].map(jerarquia_map).dropna()
    if not valores_numericos.empty:
        mediana = valores_numericos.median()
        categoria_mediana = jerarquias[int(mediana)-1] if 0 < mediana <= len(jerarquias) else "N/A"
        moda = df[encabezado].mode().values
        
        resumen = pd.DataFrame({
            "Medida": ["Cantidad de datos válidos", "Moda", "Mediana"],
            "Valor": [valores_numericos.count(), ', '.join(moda), categoria_mediana]
        })
        
        print(f"\nMedidas de resumen para {encabezado}:")
        print(resumen.to_string(index=False))
        mostrar_tabla_renderizada(resumen, f"Medidas de resumen: {encabezado}")
    else:
        print(f"\nNo hay datos válidos para calcular medidas de resumen en {encabezado}")

    return tabla


# Tabla de frecuencias cualitativa nominal
def armar_tabla_frecuencias_cualitativa_nominal(df, encabezado):
    columnas_tabla = [encabezado, "fi", "fir"]

    frec_abs = df[encabezado].value_counts(dropna=False)
    frec_rel = frec_abs / frec_abs.sum()

    tabla = pd.DataFrame({
        columnas_tabla[0]: frec_abs.index,
        columnas_tabla[1]: frec_abs.values,
        columnas_tabla[2]: frec_rel.round(4)
    })

    print(f"\nTabla de frecuencias: {encabezado}")
    print(tabla.to_string(index=False))
    mostrar_tabla_renderizada(tabla, f"Tabla de frecuencias: {encabezado}")

    # ================================
    # Gráfico de barras
    plt.figure(figsize=(8,5))
    bars = plt.bar(frec_abs.index, frec_abs.values)

    # Valores encima de cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                 ha='center', va='bottom', fontsize=9)

    plt.title(f"Distribución de {encabezado}")
    plt.xlabel(encabezado)
    plt.ylabel("Frecuencia absoluta (fi)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # ================================
    #  Gráfico de torta
    plt.figure(figsize=(6,6))
    plt.pie(frec_abs,
            labels=frec_abs.index,
            autopct="%1.1f%%",
            startangle=90,
            pctdistance=0.85)
    plt.title(f"Distribución porcentual de {encabezado}")
    plt.tight_layout()
    plt.show()

    # ================================
    # Medidas resumen

    moda = frec_abs.idxmax()
    frecuencia_moda = frec_abs.max()
    proporcion_moda = frecuencia_moda / frec_abs.sum()
    cantidad_categorias = len(frec_abs)

    resumen = pd.DataFrame({
        "Medida": ["Moda", "Frecuencia absoluta de la moda", "Proporción de la moda", "Cantidad de categorías"],
        "Valor": [moda, frecuencia_moda, round(proporcion_moda, 4), cantidad_categorias]
    })

    print("\nMedidas de resumen:")
    print(resumen.to_string(index=False))
    mostrar_tabla_renderizada(resumen, f"Medidas de resumen: {encabezado}")

    return tabla

