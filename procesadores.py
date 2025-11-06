import pandas as pd

from graficadores import (
    armar_tabla_frecuencias_cualitativa_nominal,
    armar_tabla_frecuencias_cualitativa_ordinal,
    armar_tabla_frecuencias_cuantitativa_discreta
)
#-------------------------------------FUNCIONES ESPECIFICAS------------------------------------------
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

# Prepara los datos para la variable de "Nivel de dificultad en el uso de la aplicacion PAMI"
def procesar_variable_rubro_emprendedores(df):
    df_emprendedores = df[df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].notna()];
    armar_tabla_frecuencias_cualitativa_nominal(df_emprendedores,"INICIATIVA_EMPRENDIMIENTO_RUBRO");

# Prepara los datos para la variable de "Cantidad de personas con ingresos en la vivienda"
def procesar_variable_ingresos_por_persona(df):
    armar_tabla_frecuencias_cuantitativa_discreta(df,"PERSONAS_CON_INGRESOS")

