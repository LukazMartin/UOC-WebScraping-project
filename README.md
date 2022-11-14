# UOC-WebScrapping-project

Práctica 1: ¿Cómo podemos capturar los datos de la web?

Asignatura: Tipología y ciclo de vida de los datos

Autores: _**Lukaz Martin Doehne** & _**Pablo Vadillo Berganza**

Profesora: Laia Subirats Maté


## Descripción

El objetivo de este proyecto es realizar WebScraping en una página web y guardar la información relevante dentro de un csv.

La página web objetivo es www.engelvoelkers.com y los datos guardados son sobre todas las casas que tienen en venta en barcelona.


## Dataset

El dataset consta de 1250 filas que representan cada casa en venta. El formato es el siguiente:

· id: Identificador de Engel&Voelkers

· title: Título de la vivienda

· location: Ubicación dentro de Barcelona

· location_status: Valoración categórica de la ubicación (Excelente, muy bien, regular...)

· status: Valoración categórica del estado de la vivienda (Necesita renovación, buena, excelente...)

· year: Año de construcción

· area: Superfície de la vivienda

· bathrooms: Cantidad de lavabos

· bedrooms: Cantidad de dormitorios

· heating_type: Tipo de calefacción (Bomba de calor, Gas, Suelo ardiente...)

· energy_class: Eficiencia energética (D, E, G...)

· price: Precio de la vivienda en EUR


## COMO CONSTRUIR / PARTICIPAR

· Abrir una terminal en el sitio donde quieras localizar el proyecto. En mi caso: /Lukaz/Desktop/

· Escribir (en la terminal): git clone https://github.com/LukazMartin/UOC-WebScraping-project.git

· Se crea el proyecto y lo puedes abrir con Pycharm

· Crear una nueva rama (en la terminal): git checkout -b nombre-de-la-rama

· Realizar cambios de código

· Elegir los cambios que quieres añadir. Si no creas nuevas clases es asi (en la terminal): git add source/scraper.py

· Añadir un mensaje (terminal). git commit -m "Aqui va el mensaje entre comillas"

· Subir al repositorio (terminal). git push origin nombre-de-la-rama


El script a ejecutar se encuentra en source/scraper.py

El dataset se genera en dataset/engelvoelkers_houses_bcn.csv

Los requisitos a instalar estan en requirements.txt
