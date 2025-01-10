"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():

    import pandas as pd

    # Ruta al archivo tbl0.tsv en la carpeta "files"
    ruta_1 = "files\input/tbl0.tsv"
    ruta_2="files\input/tbl2.tsv"
    try:
    # Leer el archivo usando pandas
        tabla_1 = pd.read_csv(ruta_1, sep='\t')
        tabla_2=pd.read_csv(ruta_2,sep='\t')
        
        if 'c0' in tabla_2.columns and 'c5b' in tabla_2.columns:

            tabla=tabla_2.groupby('c0')['c5b'].sum()
            tabla_comb = pd.merge(tabla_1, tabla, on='c0')

            if 'c0' in tabla_comb.columns and 'c1' in tabla_comb.columns:

                pregunta_13=tabla_comb.groupby('c1')['c5b'].sum()
                print(pregunta_13)
                
            else:
                print("no se encontraron archivos")
        else:
            print("no se encontraron archivos")

                
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    return pregunta_13
pregunta_13()

    # """
    # Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    # compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    # Rta/
    # c1
    # A    146
    # B    134
    # C     81
    # D    112
    # E    275
    # Name: c5b, dtype: int64
    # """
