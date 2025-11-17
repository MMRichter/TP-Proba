import pandas as pd;

from procesadores import (
    procesar_variable_ingresos_por_persona,
    procesar_variable_rubro_emprendedores,
    procesar_variable_tipos_ingresos,
    procesar_variable_personas_buscando_trabajo,
    procesar_variable_personas_buscando_trabajo_tiempo,
)
from procesadores import (
    procesar_variable_dificultad_app,
    procesar_variable_dificultad_desplazamiento,
    procesar_variable_uso_aplicacion_pami,
    procesar_variable_acceso_internet,
    procesar_variable_uso_celular,
    procesar_variable_adultos_mayores,
    procesar_variable_adultos_mayores_lugares_referencia_categorias,
    procesar_variable_distribucion_jubilados_pensionados,
)
from procesadores import (
    procesar_variable_distribucion_cuidado_menores,
    procesar_variable_menores_actividades_recreativas,
    procesar_variable_actividades_extracurriculares_en_barrio,
    procesar_variable_parentesco_cuidadores,
    procesar_variable_cuidador_con_ingresos,
    procesar_variable_habilitacion_emprendimientos,
    procesar_variable_distribucion_menores,
    procesar_variable_distribucion_edad_menores_rango,
    procesar_variable_menores_escolarizados,
    procesar_variable_escolarizacion_en_barrio
)
#-------------------------------------CONSTANTES-----------------------------------------------------
# Ruta del archivo CSV de la base de datos
base_datos="encuesta.csv"

# Encabezados de las columnas del DataFrame
encabezados = ["MARCA_TEMPORAL",
               "ENCUESTADOR",
               "NRO_ENCUESTA",
               "DIRECCION",
               "BARRIO",
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
    ]

def carga_dataset():
    df = pd.read_csv(base_datos)
    df.columns = encabezados

    df["BARRIO"] = df["BARRIO"].str.split(" - ").str[1].fillna("").str.strip()

    df.drop(columns=["MARCA_TEMPORAL", "ENCUESTADOR", "NRO_ENCUESTA", "DIRECCION"], inplace=True)

    return df
#-----------------------------------------MAIN-------------------------------------------------------
def main(argv=None):

    df = carga_dataset()


    #-----------------------Variables: Descomentar la variable a tratar, configurar desde parametros---------------------------------

#------------------VARIABLES ASOCIADAS A LOS INGRESOS-----------------------------------------------
    #Variable: Numero de personas con ingresos por vivienda
    #procesar_variable_ingresos_por_persona(df,barras=True,ojiva=False, desagregar_por_barrio=False);

    #Variable: Tipos de ingresos de habitantes por vivienda
    #procesar_variable_tipos_ingresos(df,barras=True,desagregar_por_barrio=False)

    #Variable: Tiempo buscando trabajo por persona
    #procesar_variable_personas_buscando_trabajo_tiempo(df,barras=True,torta=False,desagregar_por_barrio=True)

    #Variable: Numero de personas buscando trabajo por vivienda
    #procesar_variable_personas_buscando_trabajo(df,barras=True,ojiva=False,desagregar_por_barrio=True)

#-----------------VARIABLES ASOCIADAS A EMPRENDIMIENTOS---------------------------------------------
   
    #Variable: Distribucion de rubros de los emprendimientos
    #procesar_variable_rubro_emprendedores(df,torta=False,desagregar_por_barrio=True) 

    #Variable: Habilitaciones para emprendimientos del rubro alimentos
    #procesar_variable_habilitacion_emprendimientos(df,barras=False,torta=True, desagregar_por_barrio=False)
    
#-------------------VARIABLES EJE MENORES--------------------------------
    #Variable: Distribucion de edades de menores por vivienda
    #procesar_variable_distribucion_menores(df,barras=True,ojiva=True,desagregar_por_barrio=False)

    #Variable: Distribucion de cantidad de menores por rango etario
    #procesar_variable_distribucion_edad_menores_rango(df,barras=True,desagregar_por_barrio=False)

    #Variable: Distribucion de # menores de edad escolarizados por vivienda
    #procesar_variable_menores_escolarizados(df,barras=True,torta=True,desagregar_por_barrio=False)

    #Variable: Distribucion de escolarizacion dentro del barrio
    #procesar_variable_escolarizacion_en_barrio(df,barras=False,torta=True,desagregar_por_barrio=False)

    #Variable: Cantidad de menores realizando actividades recreativas
    #procesar_variable_menores_actividades_recreativas(df,barras=False,ojiva=True,desagregar_por_barrio=True)

    #Variable: Distribucion de presencia barrial en las actividades recreativas realizadas por menores
    #procesar_variable_actividades_extracurriculares_en_barrio(df,barras=False, torta=True, desagregar_por_barrio=True)

    #Variable: Distribucion de cuidados de los menores por vivienda
    #procesar_variable_distribucion_cuidado_menores(df,barras=True, torta=True,desagregar_por_barrio=False)

    #Variable: Distribucion de parentesco del cuidador, siempre que el cuidado se centre en 1 persona
    #procesar_variable_parentesco_cuidadores(df,barras=False,torta=False,desagregar_por_barrio=False)

    #Variable: Distribucion de ingresos cuando el cuidado se centre en 1 persona
    #procesar_variable_cuidador_con_ingresos(df,barras=False,torta=False,desagregar_por_barrio=False);

#----------------VARIABLES EJE ADULTOS MAYORES-----------------------------
    
    #Variable: Presencia de lugares de referencia por adulto mayor
    #Variable: Distribucion de lugares de referencia por adulto mayor
    #procesar_variable_adultos_mayores_lugares_referencia_categorias(df,detalle_barras=True,desagregar_por_barrio=False,estado_torta=True)
    
    #Variable: Cantidad de jubilados y pensionados por vivienda -> Configurar si incluir o no los valores 0 desde incluir_cero= True | False
    #procesar_variable_distribucion_jubilados_pensionados(df,barras=True,ojiva=False,desagregar_por_barrio=False,incluir_cero=True)

    #Variable: Cantidad de Adultos mayores por vivienda
    #procesar_variable_adultos_mayores(df,barras=True,desagregar_por_barrio=False);
    
    #Variable: Presencia de uso de celular entre adultos mayores
    #procesar_variable_uso_celular(df,barras=False,torta=True,desagregar_por_barrio=True)

    #Variable: Presencia de acceso a internet entre adultos mayores
    #procesar_variable_acceso_internet(df,barras=False,torta=True,desagregar_por_barrio=True)

    #Variable: Distribucion de uso de la aplicacion PAMI
    #procesar_variable_uso_aplicacion_pami(df,barras=False,torta=True,desagregar_por_barrio=True)

    #Variable: Distribucion de dificultad en la utilizacion de la app PAMI
    #procesar_variable_dificultad_app(df,barras=True,desagregar_por_barrio=True);

    #Variable: Presencia de dificultad de desplazamiento entre adultos mayores
    #Variable: Detalle de dificultad de desplazamiento
    #procesar_variable_dificultad_desplazamiento(df,barras=True,desagregar_por_barrio=False)
    
    
    
    









if __name__ == "__main__":
    
    main()
