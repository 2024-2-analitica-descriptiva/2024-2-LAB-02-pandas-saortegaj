"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():

    import pandas as pd

    
    ruta_archivo = "files/input/tbl0.tsv"
        
    tabla = pd.read_csv(ruta_archivo, sep='\t')
    pregunta_01 = len(tabla)
    print(pregunta_01)

    return pregunta_01
pregunta_01()




    
