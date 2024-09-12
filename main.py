from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn

app=FastAPI()
@app.get('/')
def home():
    return "Aca estoy pagina principal"
#---------------------------------------
df = pd.read_csv('DataSet_MVP/MoviesDesanidado.csv')
#print(df.head(10))
#print(df.info())
#---------------------------------------
#@app.get("/Peliculas por MES/{mes}")
#async def contar_peliculas_mes(mes:str):
'''
    Me defino una función llamada contar_peliculas_mes, que recibe un parametro
       un mes, esta funcion devuelve la cantidad de peliculas que se estrenaron,
       en el mes, pasado como parametro.
       Parameters
          mes: str
       Return
          pelicula_en_mes: int  
    '''
    # Diccionario para convertir meses en español a números de mes
#    meses = {
#        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
#        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
#}
#    if mes not in meses:
#        raise HTTPException(status_code=400, detail=f"El mes {mes} no es válido")
    # Obtener el número correspondiente al mes
#    mes_nro = meses.get(mes.lower())
#    if mes_nro is None:
#        return f"El mes '{mes}' no existe."
#    # Filtrar las filas donde el mes de 'release_date' sea igual a mes_numero
#    peliculas_en_mes = df[df['release_date'].dt.month == mes_nro]
#    # Contar el número de películas en el mes
#    return len(peliculas_en_mes)
# Llamar a la función con el mes deseado
#mes = 'diciembre'
#cantidad_peliculas = contar_peliculas_mes(mes)
#print(f"Cantidad de películas estrenadas en {mes}: {cantidad_peliculas}")
#-------------------------------------------------------
@app.get("/cantidad_peliculas_dia/{dia}")
async def cantidad_filmaciones_dia(dia):
    '''
    Esta funcion me devuelve la cantidad de peliculas que fueron filmadas en un dia especial
    PARAMETRO
    dia:str # Dia para el que se quiere encontrar la cantidad de filmaciones
    DEVUELVE
    cantidad_peliculas:int # Cantidad de peliculas filmadas
    Ejemplo
    dia = "Domingo" 
    cantidad_peliculas = 3613
    '''
    # Diccionario para convertir días en español a números de día de la semana
    dias = {
        'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3, 
        'viernes': 4, 'sabado': 5, 'domingo': 6
    }
    # Convertir el nombre del día a minúsculas para asegurar la coincidencia
    dia = dia.lower()
    # Obtener el número del día de la semana basado en el nombre en español
    dia_nro = dias.get(dia)
    if dia_nro is None:
        return f"El día '{dia}' no es válido."
    # Convertir la columna 'release_date' a tipo datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    # Filtrar las filas donde el día de la semana de 'release_date' sea igual a dia_numero
    peliculas_en_dia = df[df['release_date'].dt.weekday == dia_nro]
    # Contar el número de películas en el día
    return len(peliculas_en_dia)
# Llamar a la función con el dataframe y el día deseado
dia = 'domingo'
cantidad_peliculas = cantidad_filmaciones_dia(dia)
print(f"Cantidad de películas estrenadas en {dia}: {cantidad_peliculas}")




    