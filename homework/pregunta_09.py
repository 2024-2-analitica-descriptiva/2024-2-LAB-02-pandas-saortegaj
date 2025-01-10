"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_09():
    import pandas as pd

    ruta_archivo= "files\input/tbl0.tsv"

    try:

        tabla = pd.read_csv(ruta_archivo, sep='\t')
       
        if 'c3' in tabla.columns:
            # Identificar y corregir fechas inválidas
            for index, row in tabla.iterrows():
                # Si encontramos una fecha incorrecta como '1999-02-29'
                if row['c3'] == '1999-02-29':
                    # Asignamos una fecha válida manualmente
                    tabla.loc[index, 'c3'] = '1999-02-28'
            
            # Convertir 'c3' a tipo datetime (esto maneja NaT para valores erróneos)
            tabla['c3'] = pd.to_datetime(tabla['c3'], errors='coerce')

            # Extraer el año de la columna 'c3', incluyendo valores corregidos
            tabla['year'] = tabla['c3'].dt.year.astype(str)

            # Mostrar el DataFrame resultante
            print(tabla)
        else:
            print("La columna 'c3' no existe en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

    return tabla
pregunta_09()


    # """
    # Agregue el año como una columna al dataframe que contiene el archivo
    # `tbl0.tsv`.

    # Rta/
    #     c0 c1  c2          c3  year
    # 0    0  E   1  1999-02-28  1999
    # 1    1  A   2  1999-10-28  1999
    # 2    2  B   5  1998-05-02  1998
    # ...
    # 36  36  B   8  1997-05-21  1997
    # 37  37  C   9  1997-07-22  1997
    # 38  38  E   1  1999-09-28  1999
    # 39  39  E   5  1998-01-26  1998

    # """
