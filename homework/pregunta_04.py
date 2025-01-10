"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_04():

    import pandas as pd

    # Ruta al archivo tbl0.tsv en la carpeta "files"
    ruta_archivo = "files\input/tbl0.tsv"

    try:
    # Leer el archivo usando pandas
        tabla = pd.read_csv(ruta_archivo, sep='\t')
    
    # Verificar si existen las columnas 'c1' y 'c2'
        if 'c1' in tabla.columns and 'c2' in tabla.columns:
        # Calcular el promedio de 'c2' agrupado por 'c1'
            pregunta_04 = tabla.groupby('c1')['c2'].mean()
            print("Promedio de 'c2' por cada letra en la columna 'c1':")
            print(pregunta_04)
        else:
            print("Las columnas 'c1' y/o 'c2' no existen en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_04
        
pregunta_04()
