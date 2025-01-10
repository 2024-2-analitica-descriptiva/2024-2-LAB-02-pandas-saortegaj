"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_12():


    import pandas as pd

    # Ruta al archivo tbl0.tsv en la carpeta "files"
    ruta_archivo = "files\input/tbl2.tsv"

    try:
    # Leer el archivo usando pandas
        tabla = pd.read_csv(ruta_archivo, sep='\t')
    
        # Verificar si existen las columnas 'c4'
        
        tabla['c5'] = tabla['c5a'].astype(str) + ':' + tabla['c5b'].astype(str)
        tabla['c5']=tabla['c5']
        pregunta_12=tabla.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
        
        
        # Renombrar las columnas para mayor claridad
      
        
        # Mostrar el resultado
        print("Tabla con 'c1' y lista de valores de 'c2' separados por ':'")
        print(pregunta_12)
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_12
        
pregunta_12()

#     """
#     Construya una tabla que contenga `c0` y una lista separada por ','
#     de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
#     tabla `tbl2.tsv`.

#     Rta/
#          c0                                   c5
#     0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
#     1     1              aaa:3,ccc:2,ddd:0,hhh:9
#     2     2              ccc:6,ddd:2,ggg:5,jjj:1
#     ...
#     37   37                    eee:0,fff:2,hhh:6
#     38   38                    eee:0,fff:9,iii:2
#     39   39                    ggg:3,hhh:8,jjj:5
#     """
