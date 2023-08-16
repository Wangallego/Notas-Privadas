Aplicación MVC de Notas Privadas
Esta es una aplicación web basada en el framework Flask que te permite crear y gestionar notas privadas utilizando códigos QR. Las notas pueden ser creadas, leídas y eliminadas, y también puedes acceder a un historial de notas recientes.

Instalación
Clona este repositorio en tu máquina local:
 -git clone https://github.com/tuusuario/tuproyecto.git
Accede al directorio del proyecto:
 -cd tuproyecto

Uso:
    Asegúrate de que tienes una base de datos SQLite3 configurada y accesible. Puedes modificar la conexión a la base de datos en el archivo modelo.py si es necesario.

Ejecuta el siguiente comando para crear la tabla necesaria en la base de datos:

python app.py

Inicia la aplicación Flask:
python app.py

Abre tu navegador web y accede a la URL http://localhost:5000/ para comenzar a utilizar la aplicación.

Rutas:
GET /: Página principal para crear una nueva nota.
POST /: Crea una nueva nota y muestra un código QR único para acceder a la nota.
GET /enlace/<codigo>: Muestra el enlace y el código QR para acceder a una nota específica.
GET /leernota/<codigo>: Muestra el contenido de una nota y su fecha de creación.
POST /historial: Página para ingresar un código de nota y acceder al historial.
GET /ver_historial/<codigo>: Muestra el historial de notas recientes correspondientes al código.

Características:

    Crear Nota:
        Puedes crear una nueva nota privada completando el formulario en la página principal. Simplemente ingresa el texto de la nota y haz clic en el botón "Crear Nota". Se generará un código único para la nota y se generará un código QR correspondiente que puedes escanear.

    Leer Nota
        Usando el código QR generado para una nota o ingresando manualmente el código en la página de historial, puedes acceder al contenido de una nota privada. La nota se mostrará junto con su fecha de creación.

    Historial de Notas
        Puedes acceder al historial de notas recientes visitando la página de historial. Aquí puedes ingresar el código de una nota para ver su contenido y fecha de creación. Esto te permite acceder rápidamente a las notas anteriores.

    Contribuciones
        Si encuentras algún problema o tienes sugerencias para mejorar esta aplicación, no dudes en abrir un problema en GitHub o enviar una solicitud de extracción.

    Créditos
        Esta aplicación fue desarrollada por Juan Basoa.

    Licencia
        Este proyecto está bajo la licencia MIT. Puedes consultar el archivo LICENSE para más detalles.

¡Disfruta gestionando tus notas privadas de manera sencilla y segura con esta aplicación MVC de Flask!