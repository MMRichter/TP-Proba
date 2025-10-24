import pandas as pd
import matplotlib.pyplot as plt

base_datos="encuesta.csv"
encabezados = ["MARCA_TEMPORAL",
               "ENCUESTADOR",
               "NRO_ENCUESTA",
               "DIRECCION",
               "MANZANA",
               "PERSONAS_CON_INGRESOS",
               "INGRESOS_RELACION_DEPENDENCIA",
               "INGRESOS_INFORMAL_COMPLETO",
               "INGRESOS_INFORMAL_TEMPORARIO",
               "INGRESOS_JUBILADOS_PENSIONADOS",
               "INGRESOS_AUTONOMOS",
               "INGRESOS_EMPRENDEDORES",
               "INGRESOS_PLANES_SOCIALES",
               "INGRESOS_OTRAS_FUENTES",
               "DETALLE_INGRESOS_OTRAS_FUENTES",
               "PERSONAS_BUSCANDO_TRABAJO",
               "TIEMPO_BUSCANDO_TRABAJO_PERSONA_1",
               "TIEMPO_BUSCANDO_TRABAJO_PERSONA_2",
               "TIEMPO_BUSCANDO_TRABAJO_PERSONA_3",
               "TIEMPO_BUSCANDO_TRABAJO_PERSONA_4",
               "INICIATIVA_EMPRENDIMIENTO_RUBRO",
               "DISPONE_HABILITACION_CARNET_ALIMENTOS",
               "APOYOS_NECESARIOS_PARA_EMPRENDER",
               "PERSONAS_MENORES_EN_HOGAR",
               "MENORES_0_2",
               "MENORES_3_5",
               "MENORES_6_11",
               "MENORES_12_18",
               "MENORES_INSTITUCIONES_EDUCATIVAS_EN_BARRIO",
               "MENORES_INSTITUCIONES_EDUCATIVAS_FUERA_BARRIO",
               "MENORES_ACTIVIDADES_EXTRACURRICULARES",
               "MENORES_ACTIVIDADES_EXTRACURRICULARES_EN_BARRIO",
               "MENORES_DISTRIBUCION_CUIDADO",
               "MENORES_PARENTESCO_CUIDADOR",
               "MENORES_CUIDADOR_INGRESOS",
               "ADULTO_MAYOR_1_REFERENCIA_BARRIAL",
               "ADULTO_MAYOR_1_DETALLE_REFERENCIA",
               "ADULTO_MAYOR_1_POSEE_CELULAR",
               "ADULTO_MAYOR_1_SERVICIO_INTERNET",
               "ADULTO_MAYOR_1_APP_PAMI",
               "ADULTO_MAYOR_1_NIVEL_DIFICULTAD_APP",
               "ADULTO_MAYOR_1_DIFICULTADES_DESPLAZAMIENTO",
               "ADULTO_MAYOR_1_DETALLE_DIFICULTADES",
               "ADULTO_MAYOR_2_REFERENCIA_BARRIAL",
               "ADULTO_MAYOR_2_DETALLE_REFERENCIA",
               "ADULTO_MAYOR_2_POSEE_CELULAR",
               "ADULTO_MAYOR_2_SERVICIO_INTERNET",
               "ADULTO_MAYOR_2_APP_PAMI",
               "ADULTO_MAYOR_2_NIVEL_DIFICULTAD_APP",
               "ADULTO_MAYOR_2_DIFICULTADES_DESPLAZAMIENTO",
               "ADULTO_MAYOR_2_DETALLE_DIFICULTADES",
               "ADULTO_MAYOR_3_REFERENCIA_BARRIAL",
               "ADULTO_MAYOR_3_DETALLE_REFERENCIA",
               "ADULTO_MAYOR_3_POSEE_CELULAR",
               "ADULTO_MAYOR_3_SERVICIO_INTERNET",
               "ADULTO_MAYOR_3_APP_PAMI",
               "ADULTO_MAYOR_3_NIVEL_DIFICULTAD_APP",
               "ADULTO_MAYOR_3_DIFICULTADES_DESPLAZAMIENTO",
               "ADULTO_MAYOR_3_DETALLE_DIFICULTADES",
               "REGISTROS_RELEVANTES"
    ];

def mostrar_tabla_renderizada(tabla, titulo="Tabla"):
    filas = len(tabla)
    columnas = len(tabla.columns)

    # Ajustes dinámicos
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

# -----------------------------
# Tabla de frecuencias cuantitativa discreta
def armar_tabla_frecuencias_cuantitativa_discreta(df, encabezado):
    columnas_tabla = [encabezado, "fi", "fir", "Fa ↑", "Fa ↑(%)"]
    
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

    # Medidas de resumen
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
    resumen_reset=resumen.reset_index()

    print(f"\nMedidas de resumen {encabezado}")
    print(resumen.to_string(header=False))
    resumen_reset.columns = ["Medida", "Valor"]
    mostrar_tabla_renderizada(resumen_reset, f"Medidas de resumen: {encabezado}")

    # Gráfico
    frec_abs.plot(kind='bar', title=f"Distribución de {encabezado}", xlabel='Valor', ylabel='Frecuencia absoluta')
    plt.show()

    return tabla, resumen

# ------------------------------
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

    # Gráfico de torta
    plt.figure(figsize=(6,6))
    plt.pie(frec_abs, labels=frec_abs.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Distribución de {encabezado}")
    plt.show()

    # Medidas resumen ordinales
    jerarquia_map = {valor: i+1 for i, valor in enumerate(jerarquias)}
    valores_numericos = df[encabezado].map(jerarquia_map).dropna()
    if not valores_numericos.empty:
        mediana = valores_numericos.median()
        moda = df[encabezado].mode().values
        
        # Armamos el DataFrame de resumen con formato visual más claro
        resumen = pd.DataFrame({
            "Medida": ["Cantidad de datos válidos", "Moda", "Mediana (escala jerárquica)"],
            "Valor": [valores_numericos.count(), ', '.join(moda), mediana]
        })
        
        print(f"\nMedidas de resumen para {encabezado}:")
        print(resumen.to_string(index=False))
        mostrar_tabla_renderizada(resumen, f"Medidas de resumen: {encabezado}")
    else:
        print(f"\nNo hay datos válidos para calcular medidas de resumen en {encabezado}")


    return tabla

# -----------------------------
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

    # Gráfico de barras
    plt.figure(figsize=(8,5))
    plt.bar(frec_abs.index, frec_abs.values)
    plt.title(f"Distribución de {encabezado}")
    plt.xlabel(encabezado)
    plt.ylabel("Frecuencia absoluta")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # Medidas resumen
    moda = frec_abs.idxmax()
    frecuencia_moda = frec_abs.max()
    proporcion_moda = frecuencia_moda / frec_abs.sum()
    cantidad_categorias = len(frec_abs)

    resumen = pd.DataFrame({
        "Moda": [moda],
        "Frecuencia absoluta de la moda": [frecuencia_moda],
        "Proporción de la moda": [proporcion_moda],
        "Cantidad de categorías": [cantidad_categorias]
    })

    print("\nMedidas de resumen:")
    print(resumen.to_string(index=False))
    mostrar_tabla_renderizada(resumen, f"Medidas de resumen: {encabezado}")

    return tabla


#-------------------------------
# Prepara los datos para la variable de "Dificultad en el uso de la App PAMI"
def procesar_variable_dificultad_app(df):
    datos_validos = []

    adultos_app = ["ADULTO_MAYOR_1_APP_PAMI",
                "ADULTO_MAYOR_2_APP_PAMI",
                "ADULTO_MAYOR_3_APP_PAMI"]

    adultos_dificultad = ["ADULTO_MAYOR_1_NIVEL_DIFICULTAD_APP",
                        "ADULTO_MAYOR_2_NIVEL_DIFICULTAD_APP",
                        "ADULTO_MAYOR_3_NIVEL_DIFICULTAD_APP"]

    for app_col, dif_col in zip(adultos_app, adultos_dificultad):
        # Convertimos a string y rellenamos NaN con ""
        mask = df[app_col].astype(str).str.lower() == "sí"
        datos_validos.extend(df.loc[mask, dif_col].dropna().tolist())

    datos_validos = pd.Series(datos_validos)

    jerarquia = ["Fácil", "Moderada", "Difícil"]

    armar_tabla_frecuencias_cualitativa_ordinal(
        pd.DataFrame({"Dificultad": datos_validos}),
        "Dificultad",
        jerarquia
    )

#-------------------------------
# Prepara los datos para la variable de "Nivel de dificultad en el uso de la aplicacion PAMI"
def procesar_variable_rubro_emprendedores(df):
    df_emprendedores = df[df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].notna()];
    armar_tabla_frecuencias_cualitativa_nominal(df_emprendedores,"INICIATIVA_EMPRENDIMIENTO_RUBRO");

#-------------------------------
# Prepara los datos para la variable de "Cantidad de personas con ingresos en la vivienda"
def procesar_variable_ingresos_por_persona(df):
    armar_tabla_frecuencias_cuantitativa_discreta(df,"PERSONAS_CON_INGRESOS")

def main(argv=None):
    
    df = pd.read_csv(base_datos);
    df.columns = encabezados
    
    df.drop(columns=["MARCA_TEMPORAL", "ENCUESTADOR", "NRO_ENCUESTA", "DIRECCION", "MANZANA"], inplace=True)

    procesar_variable_ingresos_por_persona(df);
    procesar_variable_rubro_emprendedores(df); 
    procesar_variable_dificultad_app(df);


if __name__ == "__main__":
    
    main()
