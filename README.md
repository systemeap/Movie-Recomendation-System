# <div align="center"><font style="color:red;">Movie-Recomendation-System</font></div>
# <div align="center">PROYECTO INDIVIDUAL Nº1</div>
<div align="center">Esteban Ariel Parrón - Machine Learning Operations </div>

Bienvenido a mi proyecto. Aquí encontrarás todo lo necesario para comenzar.
<h2>
##<div><h2><font color="blue"><strong>TABLA DE CONTENIDO</strong></font></h2></div>

- [1- Introduccion](#Introduccion)
- [2- Objetivos (principales y secundarios)](#Objetivos (principales y secundarios))
- [3- Herramientas informaticas utilizadas](#Herramientas informaticas utilizadas)
- [4- Instalación y requerimientos ](#Instalación y requerimientos )
- [5- Desarrollo del proyecto](#Desarrollo del proyecto)
- [6- Video realización del proyecto](#Video realización del proyecto)
- [7- Deployado de la API en RENDER](#Deployado de la API en RENDER)
- [8- Terminologías utilizadas](#Terminologías utilizadas)
- [9- Despedida y agradecimientos](#Despedida y agradecimientos)
- [10- Licencia](#licencia)

1-	INTRODUCCION
Hola buenas a todos, nunca pensé que iba a llegar a esta instancia, ya que en el transcurso del cursado, por una u otra causa me sucedía algo, ya sea con la conectividad, con la subida de la tarea, revisión al servidor, o en su defecto algún problema personal, pero bueno acá estamos, y era de la COHORTE 07.
Acá por presentar mi primer PROYECTO INDIVUDUAL, el cual es un MVP, para un sistema de recomendación de películas.
Para este vamos a recordar tiempo atrás cuando comencé, con la CIENCIA DE DATOS y termine aprendiendo MACHINE LEARNING, para este utilizare distintas técnicas que aprendí en el transcurso del cursado.
Este proyecto simula un ambiente de trabajo real en una start-up que provee servicios de agregación de plataformas de streaming. 
Voy a desarrollar una API, con 5 endpoints en los cuales nos permiten consultar información detallada sobre ( las películas, los actores y directores), y por ultimo con estos datos (genero, actores principales, directores y otros), elegir los más representativos y obtener recomendaciones de películas basadas en ellos. 
Para este sistema que utiliza un enfoque de filtrado basado en contenido, se analiza el texto descriptivo de las películas.
Vamos a aplicar técnicas como la vectorización, este sistema de TF-IDF (Term Frequency-Inverse Document Frequency) se utiliza en procesamiento de lenguaje natural (NLP) para convertir texto en una representación numérica que refleja la importancia de las palabras en un conjunto de documentos. 
Además, el proyecto incluye una interfaz de usuario simple, ligera y amigable, deployada en FASTAPI.
Doy GRACIAS A MIS COMPAÑEROS que tuve en el transcurso de la cursada por la colaboración en cada cohorte y A TODO EL PLANTEL DE PROFESIONALES DE HENRY, que de una u otra manera, me ayudaron a demostrar y a aprender nuevas habilidades en la ciencia de la informática moderna con el LENGUAJE PYTHON.
OBJETIVOS
Objetivo principal
•	Deployar una API (Aplicattion Programing Interface), para un sistema de recomendación de películas.
Objetivo secundario
•	Realizar un proceso de ETL (Extract, Transform, Load)
•	Realizar el proceso de EDA ()
•	Crear 5 endpoints, para la API, donde se puede consultar datos específicos y hacer una recomendación de películas.
HERRAMIENTAS INFORMATICAS
1-	Visual Studio Code: Editor de texto plano, y IDE (interfaz de usuario). Para el desarrollo y utilización de herramienta secundaria como lo es jupyter notebook.
2-	Jupyter Notebook: Para poder desplegar los dataset y visualizarlos de mejor forma, también para hacer el ETL, el EDA y el ML.
3-	Github: Use esta plataforma para almacenar el proyecto. En el mismo se creó un repositorio (Sistema de Recomendación de Películas), cada cambio que hago en local, se actualiza en dicho repositorio. 
4-	Render: se utilizó esta plataforma para almacenar y deployar el proyecto. 
Se debe crear una cuenta (puede ser paga o gratuita), cuando tenemos grandes volúmenes de datos y uso de mucha memoria es aconsejable tener una cuenta paga, para que no nos surjan problemas, ni incompatibilidades a la hora de deployar el proyecto.
Luego hay que vincular el repositorio que subimos a github y la plataforma render. 
INSTALACIONES Y REQUERIMIENTOS
Para realizar dicho proyecto se hizo uso de las distintas librerías que posee PYTHON.
Se realizó un entorno virtual, para poder trabajar con programas específicos y usos de librerías de python como ser(pip, fastAPI, pandas, numpy, matplotlib, scikit-learn y otras).
DESARROLLO DEL PROYECTO
El proceso que realice fue:
1-	Comencé con el ETL: De los dos dataset que forman parte de los datos que teníamos.
2-	Desarrollo de la API y de los endpoints:
Los endpoints desarrollados fueron:
•	def cantidad_peliculas_mes(mes): Se ingresa el mes en minúscula, por ejemplo abril, y la función retorna la cantidad de películas que se estrenaron en ese mes.
Formato de salida: En el mes de {mes} se estrenaron {cantidad} películas.
•	def cantidad_peliculas_dia(dia): Se ingresa el día en minúscula, por ejemplo sábado, y la función retorna la cantidad de películas que se estrenaron ese día.  Formato de salida: En el día {dia} se estrenaron {cantidad} películas
•	def score_titulo(titulo): Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.
  Formato de salida: "Título de la película": resultado['title'], "Año":           resultado['release_year'], "Puntaje": resultado['vote_average'].
•	def votos_titulo(titulo): Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.
  Formato de salida: {
          'Título de la película': titulo, 
          'Año': year_es, 
          'Voto total': voto_tot, 
          'Voto promedio': voto_prom}
•	def get_actor(nombre_actor): Se ingresa el nombre de un actor, por ejemplo "Tom Hanks" y se retorna su éxito medido a través del retorno, cantidad de películas y promedio de retorno.
Formato de salida: {
  "Actor/Actriz": nombre_actor,
  "Cantidad de películas": cantidad_peliculas,
  "Retorno Total": total_retorno,
  "Retorno Promedio": promedio_retorno}
•	def get_director(nombre_director): Se ingresa el nombre de un director y se retorna su éxito medido a través del retorno, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.
Formato de salida: {
  "Director": nombre_director,
  "Retorno Total": total_retorno,
  "Películas": resultado}
        {
          "Título de la película":   ,
          "Fecha de lanzamiento":    ,
          "Retorno":      ,
          "Presupuesto":   ,
          "Ganancia":    }
3-	Análisis exploratorio de los datos EDA:
4-	Realización y estudio de modelo de ML:
VIDEO DEL PROYECTO
El video se realizó para demostrar y enseñar los pasos que se hicieron para realizar el proyecto, las herramientas que se utilizaron y que se instalaron y prueba en servidor local usando FASTAPI, y en producción usando la plataforma RENDER.
Link del video:
TERMINOLOGIA USADAS
ETL: Proceso de extracción, transformación y limpieza de los datos que se realizan, para poder entender o tomar decisiones con los mismos.
EDA:
FASTAPI:
ML:
RENDER
DESPEDIDA Y AGRADECIMIENTO
Me despido de todo el PLANTEL DE PROFESIONALES que estuvieron al lado mio enseñándonos, y de los compañeros maravillosos que también me acompañaron desde que inicie hasta llegar a esta primera instancia de los proyectos individuales.



Es una API, que tiene 5 ENDPOINTS, a la cual se le puede consultar, por distintos temas relacionados a las peliculas (Cantidad de peliculas filmadas en un dia en especial, En un mes en especial, 

</font></div>



 
