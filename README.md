# <div align="center"><font style="color:red;">Movie-Recomendation-System</font></div>
# <div align="center">PROYECTO INDIVIDUAL Nº1</div>
![Captura de Pantalla](Images/mlops_cycle.png)

## <div align="center">Esteban Ariel Parrón - Machine Learning Operations </div>

Bienvenido a mi proyecto. Aquí encontrarás todo lo necesario para comenzar.
<h2>
<div><h2><font color="blue"><strong>TABLA DE CONTENIDO</strong></font></h2></div>

- [1- Introduccion](#INTRODUCCION)
- [2- Objetivos principales y secundarios](#OBJETIVOS)
- [3- Herramientas informaticas utilizadas](#HERRAMIENTAS)
- [4- Instalación y requerimientos ](#Instalación)
- [5- Desarrollo del proyecto](#Desarrollo)
- [6- Video realización del proyecto](#Video)
- [7- Deployado de la API en RENDER](#Deployado)
- [8- Terminologías utilizadas](#Terminologías)
- [9- Despedida y agradecimientos](#Despedida)
- [10- Licencia](#licencia)

# 1-	INTRODUCCION
Hola buenas a todos, nunca pensé que iba a llegar a esta instancia, ya que en el transcurso del cursado, por una u otra causa me sucedía algo, ya sea con la conectividad, con la subida de la tarea, revisión al servidor, o en su defecto algún problema personal, pero bueno acá estamos,(PERCEVERAS Y TRIUNFARAS) comence en la COHORTE 07.
Y ahora acá por presentar mi primer <strong><font color="red">PROYECTO INDIVUDUAL</font></strong>, el cual es un MVP, para un sistema de recomendación de películas.
Para este vamos a recordar tiempo atrás cuando comencé, con la CIENCIA DE DATOS y termine aprendiendo MACHINE LEARNING, para este utilizare distintas técnicas y librerias que aprendí en el transcurso del cursado como (numpy, pandas, ETL, EDA, ML).
Este proyecto simula un ambiente de trabajo real en una start-up que provee servicios de agregación de plataformas de streaming. 
Para este ´proyecto voy a desarrollar una API, con 5 endpoints en los cuales nos permiten consultar información detallada sobre ( las películas, los actores y directores), y por ultimo con estos datos (genero, actores principales, directores y otros), elegir los más representativos y obtener recomendaciones de películas basadas en ellos. Para asi hacer un MACHINE LEARNING. 
Para este sistema que utiliza un enfoque de filtrado basado en contenido, se analiza el texto descriptivo de las películas.
Vamos a aplicar técnicas como la vectorización, este sistema de TF-IDF (Term Frequency-Inverse Document Frequency) se utiliza en procesamiento de lenguaje natural (NLP) para convertir texto en una representación numérica que refleja la importancia de las palabras en un conjunto de documentos. 
Además, el proyecto incluye una interfaz de usuario simple, ligera y amigable, deployada en FASTAPI.

# 2- OBJETIVOS
## Objetivos principales
•	Deployar una API (Aplicattion Programing Interface), para un sistema de recomendación de películas.
## Objetivos secundarios
•	Realizar un proceso de ETL (Extract, Transform, Load).

•	Realizar el proceso de EDA (Exploratory Data Analysis).

•	Crear 5 endpoints, para la API, donde se puede consultar datos específicos y hacer una recomendación de películas.

# 3- HERRAMIENTAS INFORMATICAS
1-	<strong>Visual Studio Code:</strong> Editor de texto plano, y IDE (interfaz de usuario). Para el desarrollo y utilización de herramienta secundaria como lo es jupyter notebook.

2-	<strong>Jupyter Notebook:</strong> Para poder desplegar los dataset y visualizarlos de mejor forma, también para hacer el ETL, el EDA y el ML.

3-	<strong>Github:</strong> Use esta plataforma para almacenar el proyecto. En el mismo se creó un repositorio (Sistema de Recomendación de Películas), cada cambio que hago en local, se actualiza en dicho repositorio. 

4-	<strong>Render:</strong> se utilizó esta plataforma para almacenar y deployar el proyecto. 
Se debe crear una cuenta (puede ser paga o gratuita), cuando tenemos grandes volúmenes de datos y uso de mucha memoria es aconsejable tener una cuenta paga, para que no nos surjan problemas, ni incompatibilidades a la hora de deployar el proyecto.
Luego hay que vincular el repositorio que subimos a github y la plataforma render. 

# 4- INSTALACIONES Y REQUERIMIENTOS
Para realizar dicho proyecto se hizo uso de las distintas librerías que posee PYTHON.

Se realizó un entorno virtual (virtualenv), para poder trabajar con programas específicos y usos de librerías de python como ser(pip, fastAPI, pandas, numpy, matplotlib, scikit-learn y otras).

# 5- DESARROLLO DEL PROYECTO
El proceso que realice fue:

<strong>1)	Comencé con el ETL:</strong> De los dos dataset que forman parte de los datos que teníamos.
## ETL (Extracion Transformacion y Limpieza de datos)
<strong>Etapa de Extraccion:</strong> Comenzaremos extrayendo los datos de dos archivos csv, los cuales son "movies_dataset.csv" y "credits.csv", que nos pasaron.
Vamoos a comenzar a analizar, de acuerdo al diccionario de datos que nos dieron, que atributos posee cada uno y ver que tipos de datos tienen, (int, float, str, listas, diccionario,etc.).

<strong>Etapa de Transformacion:</strong> En esta etapa haremos las transformaciones solicitadas, desanidar belongs_to_collection y production_companies, ya que son diccionario que estan adentro de una lista.
Tambien ver los valores nulos de los campos revenue y budget y rellenarlos con 0 y los de release_date eliminarlos.
Formatear las fecha del atributo, release_date con el formato AAAA-mm-dd, y crear la columna release_year, del cual se extraera el año de la fecha de extreno.
Crear una columna con el nombre return, para devolver el retorno de inversion de revenue y budget, dividiendolas. Y si no hay datos disponibles que tome el valor 0.

<strong>Etapa de Eliminacion de datos:</strong> Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.

<strong>2)	Desarrollo de la API y de los endpoints:</strong>
Los endpoints desarrollados fueron:

•	<code><strong>def</strong> cantidad_peliculas_mes(mes):</code> Se ingresa el mes en minúscula, por ejemplo abril, y la función retorna la cantidad de películas que se estrenaron en ese mes.

<strong>Formato de salida:</strong> En el mes de {mes} se estrenaron {cantidad} películas.

•	<code><strong>def</strong> cantidad_peliculas_dia(dia):</code> Se ingresa el día en minúscula, por ejemplo sábado, y la función retorna la cantidad de películas que se estrenaron ese día.

<strong>Formato de salida:</strong> En el día {dia} se estrenaron {cantidad} películas.

•	<code><strong>def</strong> score_titulo(titulo):</code> Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.

  <strong>Formato de salida:</strong> "Título de la película": resultado['title'], "Año":           resultado['release_year'], "Puntaje": resultado['vote_average'].
  
• <code><strong>def</strong> votos_titulo(titulo):</code> Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.

</strong>Formato de salida:</strong> {
          'Título de la película': titulo, 
          'Año': year_es, 
          'Voto total': voto_tot, 
          'Voto promedio': voto_prom}
          
•	<code><strong>def</strong> get_actor(nombre_actor):</code> Se ingresa el nombre de un actor, por ejemplo "Tom Hanks" y se retorna su éxito medido a través del retorno, cantidad de películas y promedio de retorno.

</strong>Formato de salida:</strong> {
  "Actor/Actriz": nombre_actor,
  "Cantidad de películas": cantidad_peliculas,
  "Retorno Total": total_retorno,
  "Retorno Promedio": promedio_retorno}
  
•	<code><strong>def</strong> get_director(nombre_director):</code> Se ingresa el nombre de un director y se retorna su éxito medido a través del retorno, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.

<strong>Formato de salida:</strong> {
  "Director": nombre_director,
  "Retorno Total": total_retorno,
  "Películas": resultado}
        {
          "Título de la película":   ,
          "Fecha de lanzamiento":    ,
          "Retorno":      ,
          "Presupuesto":   ,
          "Ganancia":    }
          
<strong>3)	Análisis exploratorio de los datos EDA:</strong>
El EDA (Exploratory Data Analysis) Es un proceso fundamental en ciencia de datos cuyo objetivo es comprender las características principales de un conjunto de datos antes de aplicar cualquier modelo predictivo o análisis estadístico avanzado. 

A través del EDA, se buscan patrones, relaciones entre variables, distribuciones, valores atípicos, y características relevantes de los datos para una mejor toma de decisiones.
Vamos a revisar cada uno de los datos.

<code>df.shape</code>  # Este metodo me devuelve una tupla (filas, columnas)

<code>df.info()</code>  # Revisa el tipo de cada columna (int, float, object, etc.).

<code>df.describe()</code> # Muestra estadísticas básicas de las columnas numéricas.

<code>df.isnull().sum()</code> # Identifica si existen valores nulos y su distribución.

Con este proceso vamos a detectar errores, anomalias en los datos, identificar patrones y relaciones que no se ven a simple vista. 



<strong>4-	Realización y estudio de modelo de ML:</strong>

# 6- VIDEO DEL PROYECTO
El video se realizó para demostrar y enseñar los pasos que se hicieron para realizar el proyecto, las herramientas que se utilizaron y que se instalaron y prueba en servidor local usando FASTAPI, y en producción usando la plataforma RENDER.
Link del video: https://youtu.be/qagiZHI1s1Q

# 7- DEPLOYADO DE LA API
La API, fue deployada en RENDER, pero antes se utilizo FASTAPI, para hacerlo en forma local y probar si funcionaban los endpoints antes de subirlo a la pataforma RENDER.
Link de la plataforma: <a href="https://movie-recomendation-system-miyk.onrender.com/docs"> Sistema Recomendacion - Esteban Parrón</a>

# 8- TERMINOLOGIA USADAS
ETL: Proceso de extracción, transformación y limpieza de los datos que se realizan, para poder entender o tomar decisiones con los mismos.
EDA: Proceso que cuando una vez que se hizo el ETL, mediante este proceso se puede analizar relaciones entre las variables, identificar outliers, y valores atipicos
FASTAPI: Es un framework moderno de python, el cual nos permite construir API en PYTHON, donde se puede deployar, en forma local.
ML: Es lo que se llama modelo de machine learning.
RENDER: Es una plataforma en la nube para desplegar aplicaciones web, APIs, servicios estáticos y bases de datos. Ofrece un servicio completo de hosting y deployment que facilita a los desarrolladores desplegar sus aplicaciones.

# 9- DESPEDIDA Y AGRADECIMIENTO
Me despido de todo el PLANTEL DE PROFESIONALES que estuvieron al lado mio enseñándonos, y de los compañeros maravillosos que también me acompañaron desde que inicie hasta llegar a esta primera instancia de los proyectos individuales.

# 10- LICENCIA
Este tipo de LICENCIA, es una MIT, es de software de codigo abierto, abrir el archivo.
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 








 
