import pandas as pd
import joblib
import os



# Obtener el directorio actual donde se encuentra este archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta correcta al modelo (ajusta los niveles según tu estructura de carpetas)
ruta_modelo = os.path.join(BASE_DIR, '..', '..', 'ml_models', 'modelo_entrenado.pkl')
ruta_csv = os.path.join(BASE_DIR, '..', 'constants', 'columnas.csv')

# Verificar la ruta (opcional)
print("Ruta del CSV:", os.path.abspath(ruta_csv))



def handle_linear_regression(data):

    print("data si entra aqui")

    predictionData = data["data"]["predictionData"]
    print("datos_entrada", predictionData)
    # modelo_cargado = joblib.load(os.path.abspath(ruta_modelo))
    # df_columnas = pd.read_csv(os.path.abspath(ruta_csv)) 

    # columnas_clientes = [col for col in df_columnas.columns if col.startswith('cliente_')]
    # columnas_predio = [col for col in df_columnas.columns if col.startswith('predio_')]

    # arr_final = []

    # for datos in datos_entrada:
    #     obj = {}
    #     obj["kilos"] = datos["kilos"]

    #     for predio in columnas_predio:
    #         iDComp = "predio_" + datos["_id"]
    #         if iDComp == predio: 
    #             obj[predio] = 1
    #         else:
    #             obj[predio] = 0
    #     for cliente in columnas_clientes:
    #         if cliente in datos["client"]:
    #             obj[cliente] = 1
    #         else:
    #             obj[cliente] = 0
    #     arr_final.append(obj)


    # df = pd.DataFrame(arr_final)

    # # Realizar las predicciones
    # predicciones = modelo_cargado.predict(df)

    # # Las predicciones tienen dos columnas: exportación y descarte
    # resultados = pd.DataFrame(predicciones, columns=['exportacion_predicha', 'descarte_predicho'])

    # # Combinar los datos originales con las predicciones para verlos juntos
    # resultados_finales = pd.concat([df, resultados], axis=1)

    # print("\nResultados de las predicciones:")
    # print(resultados_finales)

    # # Sumar la columna 'exportacion_predicha' en una variable
    # exportacion_total = resultados['exportacion_predicha'].sum()

    # # Sumar la columna 'descarte_predicho' en otra variable
    # descarte_total = resultados['descarte_predicho'].sum()

    # print("\nSuma total de exportacion_predicha:", exportacion_total)
    # print("Suma total de descarte_predicho:", descarte_total)

    # return {
    #     "exportacion_total":exportacion_total,
    #     "descarte_total":descarte_total
    # }
    return {}

handlers_modelos = {
    "get_python_data_porcentageExportacion": handle_linear_regression,
}