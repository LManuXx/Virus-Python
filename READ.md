## Proyecto Académico: Generación y Envío Automático de Correos Electrónicos de Spam

### Descripción del Proyecto

Este proyecto académico consiste en un programa escrito en Python que interactúa con el Registro de Windows para obtener información de correo electrónico asociada a una cuenta de usuario y luego envía múltiples correos electrónicos de spam a dicha cuenta. El propósito de este proyecto es demostrar la integración de varias técnicas de programación y el uso de bibliotecas estándar de Python para manipular el sistema operativo y realizar operaciones de red.


### Estructura del Código
El código se divide en tres secciones principales:

Obtención de Información del Registro de Windows
Configuración y Envío de Correos Electrónicos
Lógica Principal del Programa

#### 1. Obtención de Información del Registro de Windows
La función obtener_primera_carpeta_registro se encarga de acceder a una ruta específica en el Registro de Windows y devolver el nombre de la primera subclave encontrada. En este caso, se busca información en la clave Software\Microsoft\IdentityCRL\UserExtendedProperties.

#### 2. Configuración y Envío de Correos Electrónicos
La función send_email utiliza la biblioteca smtplib para enviar correos electrónicos a través del servidor SMTP de Gmail. Los mensajes se construyen utilizando la biblioteca email.mime.

#### 3. Lógica Principal del Programa
En la lógica principal, se define la ruta del Registro de Windows a leer y se obtienen los datos necesarios para enviar los correos electrónicos. Luego, se envía un número definido de correos electrónicos de spam.


### Advertencia
Este código tiene fines educativos y demuestra técnicas de programación y manipulación del sistema operativo. No debe ser utilizado para actividades maliciosas o ilegales. El uso indebido de este código puede tener consecuencias legales serias. Siempre asegúrese de tener permiso explícito para acceder y utilizar los recursos del sistema y enviar correos electrónicos.

### Ejecución del Programa
Clone este repositorio o copie el código en su editor de Python.
Configure las variables from_email y password con las credenciales de su cuenta de Gmail.
Ejecute el script de Python.
bash
Copiar código
python nombre_del_archivo.py
Contribuciones
Este proyecto fue desarrollado como parte de un ejercicio académico y no está destinado a ser mantenido o expandido. Las contribuciones no están actualmente abiertas.

### Licencia
Este proyecto no está bajo ninguna licencia y su uso debe ser restringido a propósitos educativos únicamente.