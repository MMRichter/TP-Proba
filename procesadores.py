import pandas as pd

from graficadores import (
    armar_tabla_frecuencias_cualitativa_nominal,
    armar_tabla_frecuencias_cualitativa_ordinal,
    armar_tabla_frecuencias_cuantitativa_discreta,
    procesar_variable_generica,
)

#-------------------------------------FUNCIONES ESPECIFICAS------------------------------------------
# Prepara los datos para la variable de "Dificultad en el uso de la App PAMI"
def procesar_variable_dificultad_app(df, barras=True, titulo="", desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):                 
        datos_validos = []

        adultos_app = ["ADULTO_MAYOR_1_APP_PAMI",
                    "ADULTO_MAYOR_2_APP_PAMI",
                    "ADULTO_MAYOR_3_APP_PAMI"]

        adultos_dificultad = ["ADULTO_MAYOR_1_NIVEL_DIFICULTAD_APP",
                            "ADULTO_MAYOR_2_NIVEL_DIFICULTAD_APP",
                            "ADULTO_MAYOR_3_NIVEL_DIFICULTAD_APP"]

        for app_col, dif_col in zip(adultos_app, adultos_dificultad):
            # Convertimos a string y rellenamos NaN con ""
            mask = sub_df[app_col].astype(str).str.lower() == "sí"
            datos_validos.extend(sub_df.loc[mask, dif_col].dropna().tolist())

        datos_validos = pd.Series(datos_validos)

        jerarquia = ["Fácil", "Moderada", "Difícil"]

        df_dificultad = pd.DataFrame({"Dificultad": datos_validos})
        armar_tabla_frecuencias_cualitativa_ordinal(
            df_dificultad,
            "Dificultad",
            titulo,
            jerarquia, barras
        )

    procesar_variable_generica(df, "Dificultad de uso de la App PAMI", ejecutar, desagregar_por_barrio)

# Prepara los datos para la variable de "Nivel de dificultad en el uso de la aplicacion PAMI"
def procesar_variable_rubro_emprendedores(df, barras=True, torta=True, desagregar_por_barrio=False):
    df_emprendedores = df[df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].notna()];
    def ejecutar(sub_df, titulo=""):
        armar_tabla_frecuencias_cualitativa_nominal(sub_df,"INICIATIVA_EMPRENDIMIENTO_RUBRO",titulo,barras, torta);

    procesar_variable_generica(df_emprendedores,"Rubros de emprendimientos", ejecutar,desagregar_por_barrio);

# Prepara los datos para la variable de "Cantidad de personas con ingresos en la vivienda"
def procesar_variable_ingresos_por_persona(df, barras=True, ojiva=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        armar_tabla_frecuencias_cuantitativa_discreta(sub_df,"PERSONAS_CON_INGRESOS",titulo,barras,ojiva)
    
    procesar_variable_generica(df,"Personas con ingresos",ejecutar,desagregar_por_barrio)


