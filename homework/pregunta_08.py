"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_08():
     import pandas as pd

     ruta_archivo= "files/input/tbl0.tsv"
     try:
          tabla = pd.read_csv(ruta_archivo, sep='\t')
    

          if 'c0' in tabla.columns and 'c2' in tabla.columns:
               tabla['suma'] = tabla['c0'] + tabla['c2']
               
               print("DataFrame con la columna 'suma' agregada:")  
        
          else:
               print("Las columnas 'c0' y/o 'c2' no existen en el archivo.")
            
     except FileNotFoundError:
          print(f"El archivo '{ruta_archivo}' no existe.")
     except Exception as e:
          print(f"Se produjo un error: {e}")
     print(tabla)
     return tabla
pregunta_08()
