import pandas as pd
import matplotlib.pyplot as plt

barrios = ["BELGRANO", "VILLA LAZA", "CHARITOS"]

#-------------------------------------FUNCIONES GENERALES--------------------------------------------
def procesar_variable_doble_respuesta_nominal(df, columnas_estado, columnas_detalle, titulo_estado, titulo_detalle, barras=True, desagregar_por_barrio=False, torta = False):
    """
    Procesa un conjunto de columnas tipo 'estado' y 'detalle', 
    generando dos distribuciones:
      1. Distribución de si presenta o no la condición
      2. Distribución de los detalles (solo para quienes presentan la condición)
    """

    def ejecutar(sub_df, titulo=""):
        # ---Distribución de estado---
        datos_estado = []
        for col in columnas_estado:
            datos_estado.extend(sub_df[col].dropna().astype(str).tolist())

        df_estado = pd.DataFrame({titulo_estado: datos_estado})
        graficar_cualitativa_nominal(df_estado, titulo_estado, f"{titulo} - Presencia", barras,torta)

        # --- Distribución de detalle ---
        datos_detalle = []
        for col_estado, col_detalle in zip(columnas_estado, columnas_detalle):
            mask = sub_df[col_estado].astype(str).str.lower() == "sí"
            # Explota respuestas múltiples separadas por comas
            detalles = (
                sub_df.loc[mask, col_detalle]
                .dropna()
                .astype(str)
                .str.split(',')
                .explode()
                .str.strip()
                .loc[lambda s: s != ""]
            )
            datos_detalle.extend(detalles.tolist())

        if len(datos_detalle) > 0:
            df_detalle = pd.DataFrame({titulo_detalle: datos_detalle})
            graficar_cualitativa_nominal(
                df_detalle, titulo_detalle, f"{titulo} - Detalles", barras
            )
        else:
            print(f"No se encontraron datos válidos para {titulo_detalle} en {titulo}")

    # Ejecutar análisis global o por barrio
    procesar_variable_generica(df, titulo_estado, ejecutar, desagregar_por_barrio)

#--- funcion selectora para la desagregacion por barrio, un handler
def procesar_variable_generica(df, titulo_base, funcion_ejecucion, desagregar_por_barrio=False):
    """
    Aplica una función de análisis y graficado a un DataFrame completo
    y opcionalmente desagrega por barrio.

    Parámetros:
    - df: DataFrame completo
    - barrios: lista de barrios
    - titulo_base: título general
    - funcion_ejecucion: función que recibe (sub_df, titulo)
    - desagregar_por_barrio: si True, aplica la función por barrio
    """
    if desagregar_por_barrio:
        por_barrio(df, funcion_ejecucion, titulo_base=titulo_base)
    else:
        funcion_ejecucion(df, titulo=titulo_base)

# - casos donde cada columna representa la misma pregunta repetida en varias personas.
def procesar_variable_multi_columna_cualitativa(
                                                df,
                                                columnas,
                                                nombre_variable,
                                                titulo_base,
                                                barras=True,
                                                mostrar_torta=False,
                                                desagregar_por_barrio=False
                                            ):
    """
    Procesa variables cualitativas nominales donde los datos están distribuidos
    en varias columnas que contienen respuestas individuales (no cantidades numéricas).

    Ejemplo: SERVICIO_INTERNET_PERSONA_1, SERVICIO_INTERNET_PERSONA_2, ...

    Parámetros:
    - df: DataFrame completo.
    - columnas: lista de nombres de columnas.
    - nombre_variable: nombre de la nueva variable cualitativa.
    - titulo_base: título general para gráficos/tablas.
    - barras: si se grafican barras.
    - mostrar_torta: si se grafican tortas.
    - desagregar_por_barrio: si se hace análisis por barrio.
    """

    def ejecutar(sub_df, titulo=""):
        # Recolectar todos los valores no nulos de las columnas dadas
        datos = []
        for col in columnas:
            datos.extend(sub_df[col].dropna().astype(str).tolist())

        if len(datos) == 0:
            print(f"No hay datos válidos para {titulo}")
            return

        df_resultado = pd.DataFrame({nombre_variable: datos})

        # Generar tabla y gráficos
        graficar_cualitativa_nominal(
            df_resultado,
            nombre_variable,
            titulo,
            barras,
            mostrar_torta
        )

    # Ejecutar el procesamiento global o por barrio
    procesar_variable_generica(df, titulo_base, ejecutar, desagregar_por_barrio)


def procesar_variable_multi_columna_ordinal(
    df,
    columnas_dict,
    nombre_variable,
    titulo_base,
    jerarquia,
    barras=True,
    mostrar_torta=False,
    desagregar_por_barrio=False
):
    """
    Procesa variables cualitativas ordinales cuyos datos están distribuidos en varias columnas numéricas,
    donde cada columna representa una categoría ordenada y el valor indica la cantidad de personas
    en esa categoría por vivienda.
    """

    def ejecutar(sub_df, titulo=""):
        sub_df_num = sub_df[list(columnas_dict.keys())].apply(pd.to_numeric, errors="coerce").fillna(0)
        totales = sub_df_num.sum()

        registros = []
        for col, total in totales.items():
            registros.extend([columnas_dict[col]] * int(total))

        if len(registros) == 0:
            print(f"No hay datos válidos para {titulo}")
            return

        df_resultado = pd.DataFrame({nombre_variable: registros})

        # Generar tabla de frecuencias ordinal
        graficar_cualitativa_ordinal(
            df_resultado,
            nombre_variable,
            titulo,
            jerarquia,
            barras
        )

    procesar_variable_generica(df, titulo_base, ejecutar, desagregar_por_barrio)

#--- funcion para variables donde los datos provienen de varias columnas 
# columnas numéricas, donde cada columna representa una categoría y los valores indican cuántas personas hay en esa categoría----
def procesar_variable_multi_columna_nominal(
                                            df,
                                            columnas_dict,
                                            nombre_variable,
                                            titulo_base,
                                            barras=True,
                                            mostrar_torta=False,
                                            desagregar_por_barrio=False
                                        ):
    """
    Procesa variables cualitativas nominales cuyos datos están distribuidos en varias columnas numéricas,
    donde cada columna representa una categoría y el valor indica la cantidad de personas en esa categoría.

    Parámetros:
    - df: DataFrame completo.
    - columnas_dict: dict {nombre_columna: etiqueta_legible}.
    - nombre_variable: nombre de la nueva variable cualitativa (para el DataFrame resultante).
    - titulo_base: título general para gráficos/tablas.
    - barras: si se grafican barras.
    - mostrar_torta: si se grafican tortas.
    - desagregar_por_barrio: si se hace análisis por barrio.
    """

    def ejecutar(sub_df, titulo=""):
        sub_df_num = sub_df[list(columnas_dict.keys())].apply(pd.to_numeric, errors="coerce").fillna(0)

        totales = sub_df_num.sum()

        registros = []
        for col, total in totales.items():
            registros.extend([columnas_dict[col]] * int(total))

        if len(registros) == 0:
            print(f"No hay datos válidos para {titulo}")
            return

        df_resultado = pd.DataFrame({nombre_variable: registros})

        # Generar tabla de frecuencias
        graficar_cualitativa_nominal(
            df_resultado,
            nombre_variable,
            titulo,
            barras,
            mostrar_torta
        )

    # Llamar al procesador genérico
    procesar_variable_generica(df, titulo_base, ejecutar, desagregar_por_barrio)

#--- aplica la funcion enviada por parametro a un sub dataframe filtrado por barrio
def por_barrio(df, funcion, *args, titulo_base="", **kwargs):
    """
    Aplica una función a todo el DataFrame y opcionalmente a cada barrio dentro de él.
   
    Parámetros:
    - df: DataFrame completo
    - barrios: lista de barrios a recorrer
    - funcion: función a aplicar (por ej. armar_tabla_frecuencias_...)
    - *args, **kwargs: argumentos que recibe esa función
    - titulo_base: texto base del título (opcional)
    """
    # Análisis global
    funcion(df, *args, **kwargs, titulo=titulo_base)

    # Desagregación por barrio
    for barrio in barrios:
        df_barrio = df[df["BARRIO"] == barrio]
        titulo_barrio = f"{titulo_base}: {barrio}"
        funcion(df_barrio, *args, **kwargs, titulo=titulo_barrio)


#------------------------------------FUNCIONES DE GRAFICOS Y TABLAS----------------------------------
# Funcion para mostrar tablas renderizadas con matplotlib
def mostrar_tabla(tabla, titulo="Tabla"):
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
def graficar_cuantitativa_discreta(df, encabezado, titulo, 
                                   mostrar_barras = True,
                                   mostrar_ojiva = True):
    
    columnas_tabla = [titulo, "fi", "fir", "Fa ↑", "Fa ↑(%)"]
    
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

    print(f"\nTabla de frecuencias: {titulo}")
    print(tabla.to_string(index=False))
    mostrar_tabla(tabla, f"Tabla de frecuencias: {titulo}")

    # ================================
    #  Medidas de resumen
    serie = df[encabezado].dropna()
    medidas = {
        "Muestra": serie.count(),
        "Media": serie.mean().round(4),
        "Mediana": serie.median(),
        "Moda": serie.mode().iloc[0] if not serie.mode().empty else None,
        "Varianza": round(serie.var(),4),
        "Desvío estándar": round(serie.std(),4),
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

    print(f"\nMedidas de resumen {titulo}")
    print(resumen.to_string(header=False))
    resumen_reset.columns = ["Medida", "Valor"]
    mostrar_tabla(resumen_reset, f"Medidas de resumen: {titulo}")
    
    # ================================
    #  Gráfico de barras (frecuencia absoluta)
    if mostrar_barras:
        plt.figure(figsize=(8,5))
        bars = plt.bar(frec_abs.index, frec_abs.values)

        # Etiquetas arriba de barras
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                    ha='center', va='bottom')

        plt.title(f"Distribución de {titulo}")
        plt.xlabel(titulo)
        plt.ylabel("Frecuencia absoluta")
        plt.tight_layout()
        plt.show()

    # ================================
    #  Ojiva (frecuencia relativa acumulada)
    if mostrar_ojiva:
        plt.figure(figsize=(8,5))
        plt.plot(frec_rel_acum.index, frec_rel_acum.values, marker='o', linestyle='-', linewidth=2)
        plt.title(f"Ojiva de {titulo}")
        plt.xlabel(titulo)
        plt.ylabel("Frecuencia relativa acumulada (%)")
        plt.grid(alpha=0.3)
        plt.ylim(0, 105)
        plt.tight_layout()
        plt.show()

    return tabla, resumen

# Tabla de frecuencias cualitativa ordinal
def graficar_cualitativa_ordinal(df, encabezado, titulo, jerarquias,
                                  mostrar_barras = True):
    columnas_tabla = [titulo, "fi", "fir", "Fa ↑", "Fa ↑(%)"]
    
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

    print(f"\nTabla de frecuencias: {titulo}")
    print(tabla.to_string(index=False))
    mostrar_tabla(tabla, f"Tabla de frecuencias: {titulo}")

    # ===========================
    # Gráfico de barras ordenado
    if mostrar_barras:
        plt.figure(figsize=(8,5))
        bars = plt.bar(frec_abs.index, frec_abs.values)

        # Etiquetas encima de las barras
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                    ha='center', va='bottom', fontsize=9)

        plt.title(f"Distribución de {titulo}")
        plt.xlabel(titulo)
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
        
        print(f"\nMedidas de resumen para {titulo}:")
        print(resumen.to_string(index=False))
        mostrar_tabla(resumen, f"Medidas de resumen: {titulo}")
    else:
        print(f"\nNo hay datos válidos para calcular medidas de resumen en {titulo}")

    return tabla

# Tabla de frecuencias cualitativa nominal
def graficar_cualitativa_nominal(df, encabezado,titulo, 
                                 mostrar_barras = True, 
                                 mostrar_torta = False):
    columnas_tabla = [titulo, "fi", "fir"]

    frec_abs = df[encabezado].value_counts(dropna=False)
    frec_rel = frec_abs / frec_abs.sum()

    tabla = pd.DataFrame({
        columnas_tabla[0]: frec_abs.index,
        columnas_tabla[1]: frec_abs.values,
        columnas_tabla[2]: frec_rel.round(4)
    })

    print(f"\nTabla de frecuencias: {titulo}")
    print(tabla.to_string(index=False))
    mostrar_tabla(tabla, f"Tabla de frecuencias: {titulo}")

    # ================================
    # Gráfico de barras
    if mostrar_barras:
        plt.figure(figsize=(8,5))
        bars = plt.bar(frec_abs.index, frec_abs.values)

        # Valores encima de cada barra
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval),
                    ha='center', va='bottom', fontsize=9)

        plt.title(f"Distribución de {titulo}")
        plt.xlabel(titulo)
        plt.ylabel("Frecuencia absoluta (fi)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    # ================================
    #  Gráfico de torta
    if mostrar_torta:
        plt.figure(figsize=(6,6))
        plt.pie(frec_abs,
                labels=frec_abs.index,
                autopct="%1.1f%%",
                startangle=90,
                pctdistance=0.85)
        plt.title(f"Distribución porcentual de {titulo}")
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
    mostrar_tabla(resumen, f"Medidas de resumen: {titulo}")

    return tabla

