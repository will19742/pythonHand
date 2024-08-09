
Este proyecto proporciona archivos en Python que permiten controlar una conexión por Firmata a un Arduino y utilizar una cámara para la detección de manos. El Arduino puede ser utilizado para interactuar con dispositivos físicos, mientras que la detección de manos a través de la cámara puede ser utilizada para realizar acciones basadas en gestos.

## Características 🛠️
 
 Utiliza la biblioteca pyfirmata de Python para establecer una conexión por Firmata con un Arduino, permitiendo el control de dispositivos físicos conectados al Arduino desde el programa en Python.
 
 Utiliza una biblioteca de detección de objetos o gestos basada en visión por computadora para detectar manos en tiempo real a través de una cámara.
 
 Proporciona una interfaz entre el programa en Python y el Arduino, permitiendo enviar comandos y recibir datos para controlar dispositivos conectados.

## Primeros pasos 📦

Instala VScode

Instala Python 3.9 ó 3.10 instalado en tu computadora, ojo no funciona con Python 3.11 o reciente pues la libreria firmata no ha sido actualizada. En la pantalla de inicio de Python pedirá añadir Python al PATH, IMPORTANTE MARCAR LA PALOMITA.

Instala las bibliotecas Python: pyfirmata para la conexión con Arduino y la biblioteca de detección de manos (p. ej., opencv, mediapipe, tensorflow, etc.) para la detección de manos.

Instala el ID de Arduino y agrega la libreria llamada firmata, investiga directamente con un prompt de CHATGPT como agregar librerias a IDArduino. 


## Listado de librerias y extensiones que debes instalar manualmente a través de la terminal de VSCODE, investiga usando prompts en CHATGPT como instalar estas extensiones a través de la terminal de vsCode.

cvzone
mediapipe
pyfirmata
python (Ext)
openCV
tensorflow
mediapipeUso 

## 📝Clonar el Repositorio: 

1. Descarga o clona el proyecto en tu sistema local utilizando Git.

2. Conectar Arduino: Conecta tu Arduino al ordenador y carga el sketch de Firmata, se encuentra en ejemplos, StandarFirmdata en el ID de arduino.

3. Ejecutar el Programa: Ejecuta el programa Python proporcionado. Asegúrate de seleccionar el puerto COM correcto para la conexión con el Arduino.

4. Detección de Manos: La cámara se activará y comenzará a detectar manos en tiempo real. Puedes interactuar con el Arduino enviando comandos desde el programa Python.

## Video de Funcionamiento 📹

-Proximamente

Este proyecto está bajo la licencia MIT.

## Créditos 🙌

Este proyecto fue creado oroginalmente por PICAIO SAS y está inspirado en proyectos similares de la comunidad de visión por computadora y Arduino.

Retomado y modificado por Prof. Wiliam Mejía Instituto Nacional de San Miguel Tepezones, El Salvador.

## Licencia 📝

Este proyecto está bajo la licencia [MIT](LICENSE).

