# Uninova

¡Bienvenido a Uninova! Esta es una plataforma web diseñada para facilitar la colaboración y la gestión de proyectos entre usuarios. Con Uninova, puedes crear, seguir y colaborar en proyectos de manera eficiente, todo desde una interfaz intuitiva y fácil de usar.

## Tabla de Contenidos

- [Acerca de Uninova](#acerca-de-uninova)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Configuración e Instalación](#configuración-e-instalación)
- [Desarrolladores](#desarrolladores)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Acerca de Uninova

Uninova es una plataforma web diseñada para facilitar la colaboración entre usuarios y la gestión de proyectos. Ofrece herramientas intuitivas y eficientes para crear, seguir y colaborar en proyectos de manera efectiva.

## Características

- **Gestión de Proyectos**: Crea y gestiona proyectos con descripciones detalladas, imágenes y documentación.
- **Colaboración**: Invita a otros usuarios a colaborar en tus proyectos y contribuye a proyectos existentes.
- **Mensajería**: Comunícate con otros usuarios a través de mensajes privados y notificaciones.
- **Búsqueda Avanzada**: Encuentra fácilmente proyectos y usuarios utilizando la función de búsqueda avanzada.
- **Diseño Responsivo**: Optimizado para su uso en dispositivos de escritorio, tabletas y smartphones.

## Tecnologías Utilizadas

Uninova utiliza las siguientes tecnologías:

- **Backend**: Django, un framework web de alto nivel escrito en Python.
- **Frontend**: HTML, CSS y JavaScript para la interfaz de usuario.
- **Base de Datos**: PostgreSQL, un sistema de gestión de bases de datos relacional.
- **Autenticación**: Django's User Authentication System para la autenticación de usuarios.

## Configuración e Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1. **Clonar el Repositorio**:
    ```sh
    git clone https://github.com/tu-usuario/uninova.git
    cd uninova
    ```

2. **Instalar Dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configurar la Base de Datos**:
    - Crea una base de datos PostgreSQL.
    - Actualiza la configuración de la base de datos en el archivo settings.py.
    - Ejecuta las migraciones de Django:
      ```sh
      python manage.py migrate
      ```

4. **Ejecutar el Servidor**:
    ```sh
    python manage.py runserver
    ```

5. **Acceder a la Aplicación**:
    Abre tu navegador web y visita `http://localhost:8000` para acceder a Uninova.

## Desarrolladores

Uninova es desarrollado por un equipo de desarrolladores apasionados:

- **Juan Pérez** - Desarrollador Backend
- **María Gómez** - Desarrolladora Frontend
- **Alejandro Martínez** - Administrador de Base de Datos

## Contribuciones

¡Las contribuciones son bienvenidas y apreciadas! Si deseas contribuir al desarrollo de Uninova, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu función (`git checkout -b feature/nueva-funcion`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega una nueva función'`).
4. Sube tus cambios a tu repositorio (`git push origin feature/nueva-funcion`).
5. Abre una solicitud de extracción en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por tu interés en Uninova! Esperamos que disfrutes utilizando nuestra plataforma para colaborar en proyectos y conectar con otros usuarios. Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.
