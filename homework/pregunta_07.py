"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_07():

    import pandas as pd
    ruta_archivo = "files/input/tbl0.tsv"
    
    tabla = pd.read_csv(ruta_archivo, sep='\t')

    if 'c1'  in tabla.columns and 'c2' in tabla.columns:
        
        pregunta_07 = tabla.groupby('c1')['c2'].sum()
        print("la suma por cada letra de 'c1':")
        print(pregunta_07)
    else:
        print("Las columnas 'c1' y/o 'c2' no existen en el archivo.")

    return pregunta_07
        
pregunta_07()

