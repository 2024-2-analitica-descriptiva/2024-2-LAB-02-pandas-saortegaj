"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_10():

    import pandas as pd

    
    ruta_archivo = "files/input/tbl0.tsv"  

    try:
        
        tabla = pd.read_csv(ruta_archivo, sep='\t')
        
        
        if 'c1' in tabla.columns and 'c2' in tabla.columns:
            
            pregunta_10 = tabla.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()

            
            pregunta_10.columns = ['c1', 'c2']

            
            pregunta_10.set_index('c1', inplace=True)

           
            print("Tabla con 'c1' y lista de valores de 'c2' separados por ':'")
            print(pregunta_10)
            
        else:
            print("Las columnas 'c1' y/o 'c2' no existen en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_10
        
pregunta_10()
    # """
    # Construya una tabla que contenga `c1` y una lista separada por ':' de los
    # valores de la columna `c2` para el archivo `tbl0.tsv`.

    # Rta/
    #                              c2
    # c1
    # A               1:1:2:3:6:7:8:9
    # B                 1:3:4:5:6:8:9
    # C                     0:5:6:7:9
    # D                   1:2:3:5:5:7
    # E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    # """
