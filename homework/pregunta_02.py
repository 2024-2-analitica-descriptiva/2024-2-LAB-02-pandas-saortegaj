"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_02():
    import pandas as pd
    ruta_archivo = "files/input/tbl0.tsv"

    try:
        # Leer el archivo usando pandas
        tabla = pd.read_csv(ruta_archivo, sep='\t')
        # Contar las columnas
        pregunta_02 = len(tabla.columns)
        print(f"La cantidad de filas en la tabla es: {pregunta_02}")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_02
pregunta_02()
