"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_11():

    import pandas as pd

    ruta_archivo = "files/input/tbl1.tsv"

    try:
        tabla = pd.read_csv(ruta_archivo, sep='\t')
    
        pregunta_11 = tabla.groupby('c0')['c4'].apply(lambda x: ','.join(map(str,sorted (x)))).reset_index()
        
    
        pregunta_11.columns = ['c0', 'c4']
        
        print("Tabla con 'c1' y lista de valores de 'c2' separados por ':'")
        print(pregunta_11)
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_11 
        
pregunta_11()
#     """
#     Construya una tabla que contenga `c0` y una lista separada por ',' de
#     los valores de la columna `c4` del archivo `tbl1.tsv`.

#     Rta/
#          c0       c4
#     0     0    b,f,g
#     1     1    a,c,f
#     2     2  a,c,e,f
#     3     3      a,b
#     ...
#     37   37  a,c,e,f
#     38   38      d,e
#     39   39    a,d,f
#     """
