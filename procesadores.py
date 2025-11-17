import pandas as pd

from graficadores import (
    graficar_cualitativa_nominal,
    graficar_cualitativa_ordinal,
    graficar_cuantitativa_discreta,
    procesar_variable_generica,
    procesar_variable_doble_respuesta_nominal,
    procesar_variable_multi_columna_nominal,
    procesar_variable_multi_columna_cualitativa,
    procesar_variable_multi_columna_ordinal
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

# Prepara los datos para la variable de "rubro emprendimientos"
def procesar_variable_rubro_emprendedores(df, barras=True, torta=True, desagregar_por_barrio=False):
    df_emprendedores = df[df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].notna()]
    def ejecutar(sub_df, titulo=""):
        graficar_cualitativa_nominal(sub_df,"INICIATIVA_EMPRENDIMIENTO_RUBRO",titulo,barras, torta)

    procesar_variable_generica(df_emprendedores,"Rubros de emprendimientos", ejecutar,desagregar_por_barrio)

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

def procesar_variable_habilitacion_emprendimientos(df, barras=False, torta=True, desagregar_por_barrio=False):
    """
    Genera la distribución de personas que disponen de habilitación/carnet de alimentos
    entre quienes declararon tener una iniciativa de emprendimiento en el rubro 'Alimentos'.
    """
    
    def ejecutar(sub_df, titulo=""):
        filtro_alimentos = sub_df["INICIATIVA_EMPRENDIMIENTO_RUBRO"].astype(str).str.lower() == "alimentos"
        df_filtrado = sub_df.loc[filtro_alimentos].copy()

        if df_filtrado.empty:
            print(f"No hay registros de emprendimientos del rubro Alimentos en {titulo}")
            return

        datos_habilitacion = df_filtrado["DISPONE_HABILITACION_CARNET_ALIMENTOS"].dropna().astype(str).tolist()

        if len(datos_habilitacion) == 0:
            print(f"No hay datos de habilitación disponibles en {titulo}")
            return

        df_habilitacion = pd.DataFrame({"Habilitación carnet alimentos": datos_habilitacion})
        graficar_cualitativa_nominal(
            df_habilitacion,
            "Habilitación carnet alimentos",
            f"{titulo} - Rubro Alimentos",
            barras,
            torta
        )

    procesar_variable_generica(df, "Habilitación en emprendimientos de alimentos", ejecutar, desagregar_por_barrio)

def procesar_variable_distribucion_edad_menores_rango(df, barras=True, desagregar_por_barrio=False):
    columnas_menores = {
        "MENORES_0_2": "0-2 años",
        "MENORES_3_5": "3-5 años",
        "MENORES_6_11": "6-11 años",
        "MENORES_12_18": "12-18 años"
    }

    jerarquia = ["0-2 años", "3-5 años", "6-11 años", "12-18 años"]

    procesar_variable_multi_columna_ordinal(
        df,
        columnas_menores,
        nombre_variable="Edad de menores",
        titulo_base="Distribución de edad de menores",
        jerarquia=jerarquia,
        barras=barras,
        desagregar_por_barrio=desagregar_por_barrio
    )

def procesar_variable_distribucion_menores(df,barras=True,ojiva=False,desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        graficar_cuantitativa_discreta(sub_df,"PERSONAS_MENORES_EN_HOGAR",titulo,barras,ojiva)
    
    procesar_variable_generica(df,"Menores de edad por vivienda", ejecutar, desagregar_por_barrio)

def procesar_variable_menores_escolarizados(df, barras=False, torta=True, desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        columnas_estado = ["MENORES_INSTITUCIONES_EDUCATIVAS_EN_BARRIO","MENORES_INSTITUCIONES_EDUCATIVAS_FUERA_BARRIO"]
        datos_estado = []
        for col in columnas_estado:
            datos_estado.extend(sub_df[col].dropna().astype(str).tolist())

        df_estado = pd.DataFrame({titulo: datos_estado})
        graficar_cualitativa_nominal(df_estado, titulo, f"{titulo} - Presencia", barras,torta)

    procesar_variable_generica(df,"Escolarizacion",ejecutar,desagregar_por_barrio)

def procesar_variable_escolarizacion_en_barrio(df, barras=False, torta=True, desagregar_por_barrio=False):
    columnas={"MENORES_INSTITUCIONES_EDUCATIVAS_EN_BARRIO" : "Escolarizados en el Barrio",
                "MENORES_INSTITUCIONES_EDUCATIVAS_FUERA_BARRIO" : "Escolarizados fuera del Barrio"}

    procesar_variable_multi_columna_nominal(df,columnas,"ESC","Lugar de escolarizacion",barras,torta,desagregar_por_barrio)

def procesar_variable_adultos_mayores(df, barras=True, desagregar_por_barrio=False):

    def ejecutar(sub_df, titulo=""):

        # 1. Detectamos las columnas de cada adulto
        grupos = {
            1: [col for col in sub_df.columns if col.startswith("ADULTO_MAYOR_1_")],
            2: [col for col in sub_df.columns if col.startswith("ADULTO_MAYOR_2_")],
            3: [col for col in sub_df.columns if col.startswith("ADULTO_MAYOR_3_")]
        }

        # 2. Estimamos la cantidad por vivienda (fila por fila)
        estimaciones = []
        for i, row in sub_df.iterrows():
            count = 0
            for adult_id, cols in grupos.items():
                if len(cols) == 0:
                    continue
                
                # Adulto existe si:
                # - Tiene algún dato no NaN
                # - No todos los datos están vacíos / "0" / "no"
                if row[cols].notna().any():
                    valores = row[cols].astype(str).str.strip().str.lower()
                    if not valores.isin(["", "0", "no", "nan"]).all():
                        count += 1

            estimaciones.append(count)

        df_temp = pd.DataFrame({
            "Cantidad de adultos mayores": estimaciones
        })

        # 3. Generamos la tabla de frecuencias nominal
        graficar_cualitativa_nominal(
            df_temp,
            "Cantidad de adultos mayores",
            titulo,
            barras,
            mostrar_torta=False
        )

    # Mantengo tu framework genérico
    procesar_variable_generica(
        df,
        "Adultos mayores por vivienda",
        ejecutar,
        desagregar_por_barrio
    )

def procesar_variable_adultos_mayores_lugares_referencia_categorias(df, detalle_barras=True, estado_torta=True, desagregar_por_barrio=False):
    columnas_estado = [
        "ADULTO_MAYOR_1_REFERENCIA_BARRIAL",
        "ADULTO_MAYOR_2_REFERENCIA_BARRIAL",
        "ADULTO_MAYOR_3_REFERENCIA_BARRIAL"
    ]
    columnas_detalle = [
        "ADULTO_MAYOR_1_DETALLE_REFERENCIA",
        "ADULTO_MAYOR_2_DETALLE_REFERENCIA",
        "ADULTO_MAYOR_3_DETALLE_REFERENCIA"
    ]

    procesar_variable_doble_respuesta_nominal(df,columnas_estado,columnas_detalle,titulo_estado="Presencia de referencia barrial",titulo_detalle="Lugar de referencia",
        barras=detalle_barras, desagregar_por_barrio=desagregar_por_barrio)

def procesar_variable_distribucion_jubilados_pensionados(df,barras=True,ojiva=False,desagregar_por_barrio=False):
    def ejecutar(sub_df, titulo=""):
        graficar_cuantitativa_discreta(sub_df,"INGRESOS_JUBILADOS_PENSIONADOS",titulo,barras,ojiva) 

    procesar_variable_generica(df,"Jubilados/Pensionados por vivienda", ejecutar, desagregar_por_barrio)

# Prepara los datos para la variable de "distribucion de cuidados de menores"
def procesar_variable_distribucion_cuidado_menores(df, barras=True, torta=True, desagregar_por_barrio=False):
    df_cuidadores = df[df["MENORES_DISTRIBUCION_CUIDADO"].notna()]
    def ejecutar(sub_df, titulo=""):
        graficar_cualitativa_nominal(sub_df,"MENORES_DISTRIBUCION_CUIDADO",titulo,barras, torta)

    procesar_variable_generica(df_cuidadores,"Distribucion de cuidados de menores", ejecutar,desagregar_por_barrio)

def procesar_variable_menores_actividades_recreativas(df, barras=False, ojiva=True, desagregar_por_barrio=False):
    #df_recretivas=df[df["MENORES_ACTIVIDADES_EXTRACURRICULARES"].notna()]
    def ejecutar(sub_df, titulo=""):
        graficar_cuantitativa_discreta(sub_df,"MENORES_ACTIVIDADES_EXTRACURRICULARES",titulo,barras,ojiva)

    procesar_variable_generica(df,"Menores recreativas por vivienda", ejecutar, desagregar_por_barrio)

def procesar_variable_actividades_extracurriculares(df,
                                                    barras=True,
                                                    torta=True,
                                                    desagregar_por_barrio=False):
    
    def ejecutar(sub_df, titulo=""):
        col_total = "MENORES_ACTIVIDADES_EXTRACURRICULARES"
        col_barrio = "MENORES_ACTIVIDADES_EXTRACURRICULARES_EN_BARRIO"

        # Convertir a numérico
        total = pd.to_numeric(sub_df[col_total], errors="coerce").fillna(0)
        en_barrio = pd.to_numeric(sub_df[col_barrio], errors="coerce").fillna(0)

        # Calcular los fuera del barrio
        fuera_barrio = (total - en_barrio).clip(lower=0)

        # Crear registros individuales
        registros = (
            ["En el barrio"] * int(en_barrio.sum()) +
            ["Fuera del barrio"] * int(fuera_barrio.sum())
        )

        if len(registros) == 0:
            print(f"No hay actividades extracurriculares registradas en {titulo}")
            return

        df_resultado = pd.DataFrame({"Lugar": registros})

        graficar_cualitativa_nominal(
            df_resultado,
            "Lugar",
            f"{titulo} - Actividades extra-escolares",
            barras,
            torta
        )

    procesar_variable_generica(
        df,
        "Distribución de actividades extra-escolares",
        ejecutar,
        desagregar_por_barrio
    )


def procesar_variable_roles_cuidadores(df,
                                       barras=True,
                                       torta=True,
                                       desagregar_por_barrio=False):
    
    def ejecutar(sub_df, titulo=""):
        col_distrib = "MENORES_DISTRIBUCION_CUIDADO"
        col_parentesco = "MENORES_PARENTESCO_CUIDADOR"

        # Filtramos SOLO los casos relevantes
        mask = sub_df[col_distrib].astype(str).str.strip().str.lower() == "principalmente en una persona"

        # Extraemos los roles
        roles = (
            sub_df.loc[mask, col_parentesco]
            .dropna()
            .astype(str)
            .str.strip()
        )

        if roles.empty:
            print(f"No hay datos válidos de cuidadores principales en {titulo}")
            return

        df_roles = pd.DataFrame({"Rol cuidador": roles})

        graficar_cualitativa_nominal(
            df_roles,
            "Rol cuidador",
            f"{titulo} - Distribución de roles de cuidadores",
            barras,
            torta
        )

    procesar_variable_generica(
        df,
        "Distribución de roles de cuidadores",
        ejecutar,
        desagregar_por_barrio
    )

def procesar_variable_cuidador_con_ingresos(df,
                                            barras=True,
                                            torta=True,
                                            desagregar_por_barrio=False):
    
    def ejecutar(sub_df, titulo=""):
        col_distrib = "MENORES_DISTRIBUCION_CUIDADO"
        col_ingresos = "MENORES_CUIDADOR_INGRESOS"

        # Filtrar solo los casos donde el cuidado es "Principalmente una persona"
        mask = sub_df[col_distrib].astype(str).str.strip().str.lower() == "principalmente en una persona"

        # Extraer la información de ingresos del cuidador
        ingresos = (
            sub_df.loc[mask, col_ingresos]
            .dropna()
            .astype(str)
            .str.strip()
        )

        if ingresos.empty:
            print(f"No hay datos válidos de ingresos del cuidador en {titulo}")
            return

        df_ingresos = pd.DataFrame({"Cuidador con ingresos": ingresos})

        graficar_cualitativa_nominal(
            df_ingresos,
            "Cuidador con ingresos",
            f"{titulo} - Ingresos del cuidador principal",
            barras,
            torta
        )

    procesar_variable_generica(
        df,
        "Ingresos cuidador principal",
        ejecutar,
        desagregar_por_barrio
    )


