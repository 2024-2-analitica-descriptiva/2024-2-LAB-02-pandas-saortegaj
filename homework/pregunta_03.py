"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_03():
    import pandas as pd
    ruta_archivo="files/input/tbl0.tsv"

    try:
        
        tabla = pd.read_csv(ruta_archivo, sep='\t')
        
        
        if 'c1' in tabla.columns:
            
            pregunta_03 = tabla['c1'].value_counts().sort_index()
            print("Cantidad de registros por cada letra en la columna 'c1':")
            print(pregunta_03)
        else:
            print("La columna 'c1' no existe en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_03

pregunta_03()


