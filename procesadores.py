import pandas as pd

from graficadores import (
    graficar_cualitativa_nominal,
    graficar_cualitativa_ordinal,
    graficar_cuantitativa_discreta,
    procesar_variable_generica,
    procesar_variable_doble_respuesta_nominal,
    procesar_variable_multi_columna_nominal,
    procesar_variable_multi_columna_cualitativa
)

#-------------------------------------FUNCIONES ESPECIFICAS------------------------------------------

# Prepara los datos para la variable de "Dificultad en el uso de la App PAMI"
def procesar_variable_dificultad_app(df, barras=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):                 
        datos_validos = []
        
        adultos_app = ["ADULTO_MAYOR_1_APP_PAMI","ADULTO_MAYOR_2_APP_PAMI","ADULTO_MAYOR_3_APP_PAMI"]
        adultos_dificultad = ["ADULTO_MAYOR_1_NIVEL_DIFICULTAD_APP","ADULTO_MAYOR_2_NIVEL_DIFICULTAD_APP","ADULTO_MAYOR_3_NIVEL_DIFICULTAD_APP"]

        for app_col, dif_col in zip(adultos_app, adultos_dificultad):
            # Convertimos a string y rellenamos NaN con ""
            mask = sub_df[app_col].astype(str).str.lower() == "sí"
            datos_validos.extend(sub_df.loc[mask, dif_col].dropna().tolist())

        datos_validos = pd.Series(datos_validos)

        jerarquia = ["Fácil", "Moderada", "Difícil"]

        df_dificultad = pd.DataFrame({"Dificultad": datos_validos})
        graficar_cualitativa_ordinal(
            df_dificultad,
            "Dificultad",
            titulo,
            jerarquia, barras
        )

    procesar_variable_generica(df, "Dificultad de uso de la App PAMI", ejecutar, desagregar_por_barrio)

#Variable Uso de aplicacion PAMI Si/No
def procesar_variable_uso_aplicacion_pami(df, barras=False, torta=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        columnas_estado = ["ADULTO_MAYOR_1_APP_PAMI","ADULTO_MAYOR_2_APP_PAMI","ADULTO_MAYOR_3_APP_PAMI"]
        datos_estado = []
        for col in columnas_estado:
            datos_estado.extend(sub_df[col].dropna().astype(str).tolist())

        df_estado = pd.DataFrame({titulo: datos_estado})
        graficar_cualitativa_nominal(df_estado, titulo, f"{titulo} - Presencia", barras,torta)

    procesar_variable_generica(df,"Uso de la APP Pami",ejecutar,desagregar_por_barrio)

# Prepara los datos para la variable de "Nivel de dificultad en el uso de la aplicacion PAMI"
def procesar_variable_rubro_emprendedores(df, barras=True, torta=True, desagregar_por_barrio=False):
    df_emprendedores = df[df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].notna()];
    def ejecutar(sub_df, titulo=""):
        graficar_cualitativa_nominal(sub_df,"INICIATIVA_EMPRENDIMIENTO_RUBRO",titulo,barras, torta);

    procesar_variable_generica(df_emprendedores,"Rubros de emprendimientos", ejecutar,desagregar_por_barrio);

# Prepara los datos para la variable de "Cantidad de personas con ingresos en la vivienda"
def procesar_variable_ingresos_por_persona(df, barras=True, ojiva=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        graficar_cuantitativa_discreta(sub_df,"PERSONAS_CON_INGRESOS",titulo,barras,ojiva)
    
    procesar_variable_generica(df,"Personas con ingresos",ejecutar,desagregar_por_barrio)

#Variable Dificultad de desplazamiento SI/NO y Variable Detalle de dificultad
def procesar_variable_dificultad_desplazamiento(df, barras=True, desagregar_por_barrio=False):
    columnas_estado = [
        "ADULTO_MAYOR_1_DIFICULTADES_DESPLAZAMIENTO",
        "ADULTO_MAYOR_2_DIFICULTADES_DESPLAZAMIENTO",
        "ADULTO_MAYOR_3_DIFICULTADES_DESPLAZAMIENTO"
    ]
    columnas_detalle = [
        "ADULTO_MAYOR_1_DETALLE_DIFICULTADES",
        "ADULTO_MAYOR_2_DETALLE_DIFICULTADES",
        "ADULTO_MAYOR_3_DETALLE_DIFICULTADES"
    ]

    procesar_variable_doble_respuesta_nominal(df,columnas_estado,columnas_detalle,titulo_estado="Dificultad para desplazarse",titulo_detalle="Causa de la dificultad",
        barras=barras, desagregar_por_barrio=desagregar_por_barrio)

#Variable Acceso a internet Si-No
def procesar_variable_acceso_internet(df, barras=False, torta=True, desagregar_por_barrio=False):
    columnas_estado = [
        "ADULTO_MAYOR_1_SERVICIO_INTERNET",
        "ADULTO_MAYOR_2_SERVICIO_INTERNET",
        "ADULTO_MAYOR_3_SERVICIO_INTERNET"
    ]

    procesar_variable_multi_columna_cualitativa(
        df,
        columnas=columnas_estado,
        nombre_variable="Acceso a servicio de Internet",
        titulo_base="Acceso a servicio de Internet",
        barras=barras,
        mostrar_torta=torta,
        desagregar_por_barrio=desagregar_por_barrio
    )


#Variable Usa celular Si-No
def procesar_variable_uso_celular(df, barras=False, torta=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        columnas_estado = ["ADULTO_MAYOR_1_POSEE_CELULAR","ADULTO_MAYOR_2_POSEE_CELULAR","ADULTO_MAYOR_3_POSEE_CELULAR"]
        datos_estado = []
        for col in columnas_estado:
            datos_estado.extend(sub_df[col].dropna().astype(str).tolist())

        df_estado = pd.DataFrame({titulo: datos_estado})
        graficar_cualitativa_nominal(df_estado, titulo, f"{titulo} - Presencia", barras,torta)

    procesar_variable_generica(df,"Posee Celular",ejecutar,desagregar_por_barrio)

#variable tipo de ingresos por vivienda
def procesar_variable_tipos_ingresos(df, barras=True, torta=False, desagregar_por_barrio=False):
    columnas_ingresos = {
        "INGRESOS_RELACION_DEPENDENCIA": "Relación de dependencia",
        "INGRESOS_INFORMAL_COMPLETO": "Informal completo",
        "INGRESOS_INFORMAL_TEMPORARIO": "Informal temporal",
        "INGRESOS_JUBILADOS_PENSIONADOS": "Jubilados / Pensionados",
        "INGRESOS_AUTONOMOS": "Autónomos",
        "INGRESOS_EMPRENDEDORES": "Emprendedores",
        "INGRESOS_PLANES_SOCIALES": "Planes sociales",
        "INGRESOS_OTRAS_FUENTES": "Otras fuentes"
    }

    # Procesamiento global o por barrio, reutilizando tu función estándar
    procesar_variable_multi_columna_nominal(df,columnas_ingresos,"Tipos de Ingresos","Tipos de Ingresos",barras,torta,desagregar_por_barrio)

#Variable personas buscando trabajo por vivienda
def procesar_variable_personas_buscando_trabajo(df, barras=True, ojiva=True, desagregar_por_barrio = False):
    def ejecutar(sub_df, titulo=""):
        graficar_cuantitativa_discreta(sub_df,"PERSONAS_BUSCANDO_TRABAJO", titulo, barras,ojiva)

    procesar_variable_generica(df,"Personas buscando trabajo por vivienda",ejecutar,desagregar_por_barrio)

#Variable tiempo buscando trabajo por persona
def procesar_variable_personas_buscando_trabajo_tiempo(df, barras=True, ojiva=True,torta=False, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        columnas_tiempo = [
            "TIEMPO_BUSCANDO_TRABAJO_PERSONA_1",
            "TIEMPO_BUSCANDO_TRABAJO_PERSONA_2",
            "TIEMPO_BUSCANDO_TRABAJO_PERSONA_3",
            "TIEMPO_BUSCANDO_TRABAJO_PERSONA_4"
        ]
        
        # Recolectar todos los valores numéricos válidos
        datos_tiempo = []
        for col in columnas_tiempo:
            datos_tiempo.extend(
                pd.to_numeric(sub_df[col], errors="coerce").dropna().tolist()
            )

        # Crear DataFrame
        df_tiempo = pd.DataFrame({"Meses buscando trabajo": datos_tiempo})

        # Ordenar de menor a mayor
        df_tiempo.sort_values(by="Meses buscando trabajo", inplace=True)

        # Generar tabla (discreta, porque es numérica)
        graficar_cuantitativa_discreta(
            df_tiempo,
            "Meses buscando trabajo",
            titulo,
            barras,
            ojiva
        )

    procesar_variable_generica(df, "Tiempo buscando trabajo (En Meses)", ejecutar, desagregar_por_barrio)
