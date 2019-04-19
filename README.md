# Chatbot de E-commerce (test) by Bosch

## Introducción 

En este proyecto se mostrará cómo conectar un chatbot creado en DialogFlow con Facebook Messenger, haciendo uso de un API externa para brindar información adicional al usuario.

Existen cuatro elementos importantes que debemos considerar

- Aplicación de Facebook Messenger. Necesitaremos crear una aplicación en [Facebook for Developers](https://developers.facebook.com). Esta aplicación se encargará de hacer la integración entre Facebook Messenger y DialogFlow para poder comunicarnos con nuestro usuario final.

- Agente de DialogFlow. DialogFlow incorpora algoritmos de Machine Learning y [Natural Language Processing](https://towardsdatascience.com/an-easy-introduction-to-natural-language-processing-b1e2801291c1) para detectar qué es lo que nuestros usuarios nos quieren decir. Nos apoyaremos de DialogFLow para integrar la aplicación web creada por nosotros con nuestro usuario final desde Facebook Messenger. 

- Web Application. Crearemos una aplicación web con ayuda de Python y Flask para poder recibir las solicitudes de DialogFlow, conectarnos con el API de E-Commerce de Bosch y mandar una respuesta de regreso a DialogFlow. Usaremos Ngrok , que es una herramienta que crear un túnel desde nuestro servidor local, para poder comunicarnos con DialogFlow. 

- API de E-Commerce de Bosch. Esta API nos permite acceder a la información de los productos de [www.boschenlinea.com](https://www.boschenlinea.com/) conociendo el ID del producto. 

## Requerimientos previos

Antes de iniciar, asegúrate de tener los siguientes requerimientos:

- Tener [Python 3](https://www.python.org/downloads/) instalado en tu compuradora.
- Descargar [ngrok](https://ngrok.com/download) y crear una cuenta.
- Acceder a  [DialogFlow](https://console.dialogflow.com/api-client/#/login) con una cuenta de Google.
- Tener una [página de Facebook](https://www.facebook.com/help/104002523024878?helpref=about_content) creada. 
- El editor de textos de su preferencia. 


## Configuración de DialogFlow

1. Accedemos a la consola de DialogFlow y creamos un nuevo agente. Debemos asegurarnos de seleccionar "español" como idioma principal. 
2. Vamos a la pestaña de ***Export and import*** dentro de la configuración del agente.
3. Seleccionamos ***RESTORE FROM ZIP*** y subimos el archivo ***bot_test.zip*** que se encuentra dentro de la carpeta de este repositorio. 

## Configuración del API de E-commerce.
1. Ingresamos a [www.boschenlinea.com](https://www.boschenlinea.com/)
2. Creamos una cuenta.
3. En el archivo ***config.py*** colocamos nuestro usuario y contraseña en la parte de LOGON_ID y LOGON_PASSWORD
4. Además de eso, necesitaremos colocar un usuario y contraseña para el Basic Auth en la parte de BASIC_AUTH. Nosotros les brindaremos estas credenciales.

## Configuración de nuestra apliación web.

#### Creación de ambiente virtual (muy recomendable)

1. Nos vamos a la carpeta donde se encuentra el repositorio.
2. En la consola ejecutamos el siguiente comando para crear nuestro ambiente virtual:

```bash
python -m venv venv
```

3. Instalamos los requirements con el siguiente comando:

```bash
pip install -r requierements.txt
```

4. Activamos nuestro ambiente virtual (comando para Windows):

```bash
.\venv\Scripts\activate
```
5. Corremos nuestra aplicación 
```bash
python main.py
```

6. Ejecutamos ngrok.exe (previamente descargado y configurado)
7. Creamos el túnel a nuestro local host:

```bash
ngrok http 5000
```

8. Copiamos y guardamos la url https que nos brinda Ngrok.

## Configuración del Fullfiment en DialogFlow

1. En la consola de DialogFlow nos dirigimos a la parte de ***Fulfillment***
2. Habilitamos el botón de ***Webhook***.




https://medium.com/cmaquera/como-crea-un-chatbot-para-facebook-messenger-con-dialogflow-8fddd17ea230

https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment




https://console.dialogflow.com/api-client/#/agent/dc447f35-c732-4eba-81a3-d36a303171fe/fulfillment

https://developers.facebook.com/apps/565756710612454/roles/roles/

https://dialogflow.com/docs/integrations/facebook



https://medium.com/swlh/how-to-build-a-chatbot-with-dialog-flow-chapter-4-external-api-for-fulfilment-3ab934fd7a00


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
# Chatbot de E-commerce (test) by Bosch

## Introducción 

En este proyecto se mostrará cómo conectar un chatbot creado en DialogFlow con Facebook Messenger, haciendo uso de un API externa para brindar información adicional al usuario.

Existen cuatro elementos importantes que debemos considerar

- Aplicación de Facebook Messenger. Necesitaremos crear una aplicación en [Facebook for Developers](https://developers.facebook.com). Esta aplicación se encargará de hacer la integración entre Facebook Messenger y DialogFlow para poder comunicarnos con nuestro usuario final.

- Agente de DialogFlow. DialogFlow incorpora algoritmos de Machine Learning y [Natural Language Processing](https://towardsdatascience.com/an-easy-introduction-to-natural-language-processing-b1e2801291c1) para detectar qué es lo que nuestros usuarios nos quieren decir. Nos apoyaremos de DialogFLow para integrar la aplicación web creada por nosotros con nuestro usuario final desde Facebook Messenger. 

- Web Application. Crearemos una aplicación web con ayuda de Python y Flask para poder recibir las solicitudes de DialogFlow, conectarnos con el API de E-Commerce de Bosch y mandar una respuesta de regreso a DialogFlow. Usaremos Ngrok , que es una herramienta que crear un túnel desde nuestro servidor local, para poder comunicarnos con DialogFlow. 

- API de E-Commerce de Bosch. Esta API nos permite acceder a la información de los productos de [www.boschenlinea.com](https://www.boschenlinea.com/) conociendo el ID del producto. 

## Requerimientos previos

Antes de iniciar, asegúrate de tener los siguientes requerimientos:

- Tener [Python 3](https://www.python.org/downloads/) instalado en tu compuradora.
- Descargar [ngrok](https://ngrok.com/download) y crear una cuenta.
- Acceder a  [DialogFlow](https://console.dialogflow.com/api-client/#/login) con una cuenta de Google.
- Tener una [página de Facebook](https://www.facebook.com/help/104002523024878?helpref=about_content) creada. 
- El editor de textos de su preferencia. 


## Configuración de DialogFlow

1. Accedemos a la consola de DialogFlow y creamos un nuevo agente. Debemos asegurarnos de seleccionar "español" como idioma principal. 
2. Vamos a la pestaña de ***Export and import*** dentro de la configuración del agente.
3. Seleccionamos ***RESTORE FROM ZIP*** y subimos el archivo ***bot_test.zip*** que se encuentra dentro de la carpeta de este repositorio. 

## Configuración del API de E-commerce.

1. Ingresamos a [www.boschenlinea.com](https://www.boschenlinea.com/)
2. Creamos una cuenta.
3. En el archivo ***config.py*** colocamos nuestro usuario y contraseña en la parte de LOGON_ID y LOGON_PASSWORD
4. Además de eso, necesitaremos colocar las credenciales de Basic Auth en la parte de BASIC_AUTH. Nosotros les brindaremos estas credenciales.

## Configuración de nuestra apliación web.

#### Creación de ambiente virtual (muy recomendable)

1. Nos vamos a la carpeta donde se encuentra el repositorio.
2. En la consola ejecutamos el siguiente comando para crear nuestro ambiente virtual:

```bash
python -m venv venv
```

3. Instalamos los requirements con el siguiente comando:

```bash
pip install -r requierements.txt
```

4. Activamos nuestro ambiente virtual (comando para Windows):

```bash
.\venv\Scripts\activate
```
5. Corremos nuestra aplicación 
```bash
python main.py
```

6. Ejecutamos ngrok.exe (previamente descargado y configurado)
7. Creamos el túnel a nuestro local host:

```bash
ngrok http 5000
```

8. Copiamos y guardamos la url https que nos brinda Ngrok.

## Configuración del Fullfiment en DialogFlow

1. En la consola de DialogFlow nos dirigimos a la parte de ***Fulfillment***
2. Habilitamos el botón de ***Webhook***.
3. Pegamos la url generada por Ngrok donde doce ***Enter URL***.
4. Provamos que nuestro chatbot funcione en la parte que dice ***try it now***, en la esquina superior derecha. 

## Integración con Facebook Messenger

1. En DialogFlow nos vamos a la parte de ***Integrations*** 
2. Habilitamos la integración con Facebook Messenger
3. Colocamos un token de Verificación. (Puede ser cualquier palabra)
4. Ahora entramos a [developers.facebook.com](https://developers.facebook.com)
5. En la parte superior damos click a ***Mis Apps***
6. Seleccionamos ***Agregar una nueva App***
7. Colocamos el nombre de nuestra app y un correo de contacto
8. En la columna izquierda dar click a  ***PRODUCTOS*** 
9. Buscar ***Messenger*** en la parte de ***Agregar productos*** y dar click en ***Configurar***
10. En la parte de ***Tokens de acceso*** seleccionar la página de Facebook en la que quieres integrar el chatbot y dar click en ***Editar permisos***. 
11. Colocar el Token de acceso a la página generado en la Integración con Messenger de DialogFlow.
12. Dar click a ***Sucribirse a eventos*** en la parte de ***Webhooks*** y colocar el URL de devolución de llamada y el token que aparecen en DialogFlow.

## Agregar Evaluadores

El chatbot creado se encuentra en Status de desarrollo hasta que el equipo de Facebook lo verifique. Por esta razón es necesario agregar usuarios como evaluadores de la app de facebook. 

Para esto debemos ir a la parte de ***Roles*** en la columna izquierda de la página y agregar personas como Evaluadores.

Estas personas deberán ingresar a la página de Facebook para desarrolladores y aceptar la solicitud para poder empezar a usar el bot. 


## License
[MIT](https://choosealicense.com/licenses/mit/)