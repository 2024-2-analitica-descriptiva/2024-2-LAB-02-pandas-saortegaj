"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():

    import pandas as pd

    # Ruta al archivo tbl0.tsv en la carpeta "files"
    ruta_archivo = "files\input/tbl1.tsv"

    try:
    # Leer el archivo usando pandas
        tabla = pd.read_csv(ruta_archivo, sep='\t')
    
    # Verificar si existen las columnas 'c4'
        if 'c4' in tabla.columns:
        
            pregunta_06 = sorted(tabla['c4'].str.upper().unique())
            print("Promedio de 'c2' por cada letra en la columna 'c1':")
            print(pregunta_06)
        else:
            print("Las columnas 'c1' y/o 'c2' no existen en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_06 
        
pregunta_06()
